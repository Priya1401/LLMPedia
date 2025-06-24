import streamlit as st
from .generator import ask_airline

def airline_tab(openai, model):
    st.header("Airline AI Assistant")
    st.write("Ask flight-related questions or get a ticket price quote.")

    query = st.text_input("Your question or destination for pricing")
    if st.button("Ask"):
        if not query:
            st.warning("Please enter a question or destination.")
        else:
            with st.spinner("Contacting the Airline AI…"):
                answer = ask_airline(openai, model, query)
                st.markdown(answer)
