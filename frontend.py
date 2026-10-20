import streamlit as st
from backend import workflow
from pdf_generator import generate_pdf

st.title(" AI Research Agent 🤖")

if "report" not in st.session_state:
    st.session_state.report=""
    
if "query" not in st.session_state: 
    st.session_state.query = ""  
      
def generate_report(query):
    try:
        with st.spinner("Researching your topic..."):
            result = workflow.invoke({
                "query": query,
                "subtopics": [],
                "search_results": [],
                "search_notes": [],
                "should_regenerate": False,
                "report": "",
                "errors": []
            },
            config={
        "run_name": "AI Research Agent"
    })
            

        report = result.get("report", "")

        if not report:
            st.warning("No report was generated. Please try again.")
            return

        st.session_state.report =result["report"][0]["text"]
        st.session_state.query = query

    except Exception as e:
        st.error(f"Failed to generate report: {e}")

st.markdown("""
<style>
[data-testid="stChatInput"] textarea {
    font-size: 20px;
    min-height: 25px;
    padding: 3px 5px;
}
</style>
""", unsafe_allow_html=True)

user_inp=st.chat_input("Enter topic to generate report")
if user_inp:
    generate_report(user_inp)

if st.session_state.report:
    st.markdown(st.session_state.report)   
    
    st.markdown("""
    <style>
    /* Regenerate button - Red */
    div.stButton > button {
        background-color: #dc3545;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    /* Regenerate button hover */
    div.stButton > button:hover {
        background-color: #bb2d3b;
        color: white;
        border: none;
        transform: translateY(-2px);
    }

    /* Download button - Green */
    div.stDownloadButton > button {
        background-color: #198754;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    /* Download button hover */
    div.stDownloadButton > button:hover {
        background-color: #146c43;
        color: white;
        border: none;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "🔄 Regenerate Research Report",
            use_container_width=True
        ):
            generate_report(st.session_state.query)
            st.rerun()

    with col2:
        pdf_file = generate_pdf(
            st.session_state.report,
            topic=st.session_state.query,
        )

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_file,
            file_name="AI_Research_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

