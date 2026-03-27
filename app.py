import streamlit as st
import os
import time
from dotenv import load_dotenv
from core.crew import build_crew
from core.pdf_generator import generate_pdf

load_dotenv()

st.set_page_config(
    page_title="AI Multi-Agent Report Generator",
    page_icon="🤖",
    layout="centered"
)

# Session state initialization
if "report_content" not in st.session_state:
    st.session_state.report_content = None
if "pdf_bytes" not in st.session_state:
    st.session_state.pdf_bytes = None
if "report_done" not in st.session_state:
    st.session_state.report_done = False

st.title("🤖 AI Multi-Agent Report Generator")
st.markdown("Enter any topic and AI agents will **research, analyze and write** a full report for you!")

st.divider()

topic = st.text_input(
    "📝 Enter your topic:",
    placeholder="e.g. Impact of AI in Healthcare India"
)

col1, col2 = st.columns(2)
with col1:
    st.slider("🔍 Search results per query", 5, 15, 10)
with col2:
    st.metric("🤖 Agents", "3")

st.divider()

if st.button("🚀 Generate Report", use_container_width=True, type="primary"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        # Reset state
        st.session_state.report_done = False
        st.session_state.report_content = None
        st.session_state.pdf_bytes = None

        progress = st.progress(0)
        status = st.empty()

        try:
            status.info("🔍 Agent 1: Researching the web...")
            progress.progress(10)

            crew = build_crew(topic)
            progress.progress(30)

            with st.spinner("Agents are working... this takes 2-3 minutes ⏳"):
                result = crew.kickoff()

            progress.progress(80)
            status.info("📄 Generating PDF report...")

            report_content = str(result)
            st.session_state.report_content = report_content

            # Generate PDF directly to fixed path
            pdf_path = os.path.join(os.getcwd(), "final_report.pdf")
            generate_pdf(topic, report_content, pdf_path)
            time.sleep(2)

            # Read PDF bytes immediately
            with open(pdf_path, "rb") as f:
                st.session_state.pdf_bytes = f.read()

            # Cleanup
            if os.path.exists(pdf_path):
                os.remove(pdf_path)

            progress.progress(100)
            status.success("✅ Report generated successfully!")
            st.session_state.report_done = True

        except Exception as e:
            progress.progress(0)
            status.error(f"❌ Error: {str(e)}")
            st.exception(e)

# Show results from session state
if st.session_state.report_done and st.session_state.report_content:
    st.divider()
    st.subheader("📋 Report Preview")
    st.markdown(st.session_state.report_content)
    st.divider()

    if st.session_state.pdf_bytes:
        st.download_button(
            label="📥 Download PDF Report",
            data=st.session_state.pdf_bytes,
            file_name=f"{topic.replace(' ', '_')}_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.divider()
st.markdown(
    """
    <div style='text-align:center; color:gray; font-size:12px'>
    Powered by CrewAI · Groq · DuckDuckGo · ChromaDB · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)