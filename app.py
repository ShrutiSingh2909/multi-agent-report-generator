import streamlit as st
import os
import time
import tempfile
from dotenv import load_dotenv
from core.crew import build_crew
from core.pdf_generator import generate_pdf

load_dotenv()

st.set_page_config(
    page_title="AI Multi-Agent Report Generator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Multi-Agent Report Generator")
st.markdown("Enter any topic and 4 AI agents will **research, analyze, write and review** a full report for you!")

st.divider()

# Input section
topic = st.text_input(
    "📝 Enter your topic:",
    placeholder="e.g. Impact of AI in Healthcare India"
)

col1, col2 = st.columns(2)
with col1:
    max_results = st.slider("🔍 Search results per query", 5, 15, 10)
with col2:
    st.metric("🤖 Agents", "4")

st.divider()

if st.button("🚀 Generate Report", use_container_width=True, type="primary"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        progress = st.progress(0)
        status   = st.empty()

        try:
            status.info("🔍 Agent 1: Researching the web...")
            progress.progress(10)

            crew = build_crew(topic)

            status.info("🔍 Agent 1: Researching... 📊 Agent 2: Analyzing... ✍️ Agent 3: Writing...")
            progress.progress(30)

            with st.spinner("Agents are working... this takes 2-3 minutes ⏳"):
                result = crew.kickoff()

            progress.progress(80)
            status.info("📄 Generating PDF report...")

            report_content = str(result)

            # Fixed PDF generation
            tmp = tempfile.NamedTemporaryFile(
                delete=False, suffix=".pdf", prefix="report_"
            )
            pdf_path = tmp.name
            tmp.close()

            generate_pdf(topic, report_content, pdf_path)
            time.sleep(1)

            progress.progress(100)
            status.success("✅ Report generated successfully!")

            st.divider()

            st.subheader("📋 Report Preview")
            st.markdown(report_content)

            st.divider()

            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_bytes,
                file_name=f"{topic.replace(' ', '_')}_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

            os.unlink(pdf_path)

        except Exception as e:
            progress.progress(0)
            status.error(f"❌ Error: {str(e)}")
            st.exception(e)

st.divider()
st.markdown(
    """
    <div style='text-align:center; color:gray; font-size:12px'>
    Powered by CrewAI · Groq · DuckDuckGo · ChromaDB · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)