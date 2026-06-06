import streamlit as st
import requests

st.title("🚀 StartupLens AI")

idea = st.text_area(
    "Enter Your Startup Idea"
)

if st.button("Validate Idea"):
     with st.spinner("Analyzing..."):
        response = requests.post(
            "http://127.0.0.1:8000/validate",
            json={"idea": idea}
        )

        result = response.json()

        st.markdown(
            result["analysis"]
        )
        st.subheader("🏢 Competitor Analysis")

if st.button("Find Competitors"):

    with st.spinner("Finding competitors..."):

        response = requests.post(
            "http://127.0.0.1:8000/competitors",
            json={"idea": idea}
        )

        result = response.json()

        st.markdown("### Top Competitors")

        for comp in result["competitors"]:
            st.write("🏢", comp)

        st.markdown("### Market Gap")

        st.info(
            result["market_gap"]
        )

        st.markdown("### Opportunity Level")

        st.success(
            result["opportunity_level"]
        )