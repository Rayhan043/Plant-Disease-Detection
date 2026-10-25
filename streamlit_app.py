import streamlit as st
from PIL import Image
from app.predict import predict_image

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿"
)

st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image or capture one using your camera.")

tab1, tab2 = st.tabs(["📁 Upload Image", "📷 Camera"])

with tab1:
    uploaded = st.file_uploader(
        "Choose a leaf image",
        type=["jpg", "jpeg", "png"]
    )

with tab2:
    uploaded = st.camera_input("Capture a leaf image")

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Selected Leaf", use_container_width=True)

    if st.button("🔍 Detect Disease"):
        with st.spinner("Analyzing image..."):
            result = predict_image(image)

        st.success(f"Disease: {result['disease']}")
        st.write(f"Confidence: {result['confidence']}%")