import streamlit as st
import sys
from pathlib import Path
from PIL import Image

sys.path.append(str(Path(__file__).parent))

from app.predict import predict_image

st.set_page_config(page_title="Plant Disease Detection", page_icon="🌿")

st.title("🌿 Plant Disease Detection")
st.write("Upload a plant leaf image to predict its disease.")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Detect Disease"):
        with st.spinner("Analyzing image..."):
            result = predict_image(image)

        st.success(f"Disease: {result['disease']}")
        st.write(f"Confidence: {result['confidence']}%")
