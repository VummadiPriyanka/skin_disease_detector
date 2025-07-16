import streamlit as st
import numpy as np
from PIL import Image

st.title("🩺 Skin Disease Detection using ML")
st.write("Upload a skin image and the model will predict the disease type.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        # Placeholder logic (mock)
        prediction = "Psoriasis"  # Change this when model is integrated
        st.success(f"Predicted Disease: {prediction}")
