import streamlit as st
from .generator import get_links, create_brochure, stream_brochure

def brochure_tab(client, model_name):
    st.header("Build your Company Brochure")

    company_name = st.text_input("Company Name")
    website_url     = st.text_input("Company Website URL", value="https://")

    # Initialize session state for links if not present
    if "links" not in st.session_state:
        st.session_state["links"] = None

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Find relevant links"):
            if not company_name or not website_url:
                st.warning("Enter both name and URL.")
            else:
                with st.spinner("Finding relevant links..."):
                    try:
                        links_json = get_links(client, model_name, website_url)
                        st.session_state["links"] = links_json
                        st.success("Links found and stored in session state.")
                    except Exception as e:
                        st.error(f"Error fetching links: {e}")

    # Display found links if available
    if st.session_state["links"]:
        st.subheader("Found Links:")
        st.json(st.session_state["links"])
        # Add UI for selecting links if needed, for now, assume all are used or selected implicitly

    st.write("---") # Separator for clarity

    if st.button("Create Brochure"):
        if not company_name or not website_url:
            st.warning("Please provide company name and website.")
        elif not st.session_state["links"]:
            st.warning("Please find relevant links first.")
        else:
            with st.spinner("Generating brochure..."):
                try:
                    # Assuming create_brochure also needs client, model_name, and links
                    md = create_brochure(client, model_name, company_name, website_url)
                    st.markdown(md)
                except Exception as e:
                    st.error(f"Error creating brochure: {e}")

    if st.button("Stream Brochure"):
        if not company_name or not website_url:
            st.warning("Please provide company name and website.")
        elif not st.session_state["links"]:
            st.warning("Please find relevant links first.")
        else:
            st.write("---")
            stream_container = st.empty()
            def update_brochure(text):
                stream_container.markdown(text)
            
            try:
                # Assuming stream_brochure also needs client, model_name, and links
                stream_brochure(client, model_name, company_name, website_url, update_brochure)
            except Exception as e:
                st.error(f"Error streaming brochure: {e}")
