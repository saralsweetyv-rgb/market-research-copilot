import streamlit as st

from src.ai_service import generate_market_analysis


st.set_page_config(
    page_title="Market Research Copilot",
    page_icon="📊"
)

st.title("📊 Market Research Copilot")

topic = st.text_input(
    "Enter a research topic:"
)

if st.button("Generate Report"):

    if topic:

        with st.spinner("Generating market research report..."):

            report = generate_market_analysis(topic)

        st.success("Report Generated!")

        st.markdown(report)

    else:
        st.warning("Please enter a topic.")