import streamlit as st
from PIL import Image
from .generator import ask_chef

def vision_chef_tab(client, model_name):
    st.header("👨‍🍳 Vision Chef")
    st.write("Upload a photo of your ingredients or fridge, and let our AI Chef suggest recipes!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    user_note = st.text_input("Any dietary restrictions or preferences? (Optional)")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', width=300)
        
        if st.button("Get Recipes"):
            with st.spinner("The Chef is brainstorming..."):
                try:
                    recipe_suggestions = ask_chef(client, model_name, image, user_note)
                    st.markdown(recipe_suggestions)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
