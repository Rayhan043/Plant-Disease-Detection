
import streamlit as st
from PIL import Image
from app.predict import predict_image

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #edf8ef 0%, #f8faf8 45%, #ffffff 100%);
}
.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    background: linear-gradient(135deg, #14532d, #228b50);
    padding: 35px 25px;
    border-radius: 22px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.hero h1 { color: white; font-size: 32px; }
.hero p { color: #e4f5e8; font-size: 16px; }
.info-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #dce9df;
    margin: 12px 0;
}
.result-card {
    background: #e5f6e9;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #a7d9b3;
    margin-top: 20px;
}
div.stButton > button {
    background: #198044;
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 48px;
    font-weight: 600;
    width: 100%;
}
div.stButton > button:hover {
    background: #126534;
    color: white;
    border: none;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌿 Plant Disease Detection</h1>
    <p>Check your plant's health with AI-powered image analysis.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🔍 Analyze Your Plant")
st.write("Upload a leaf photo or take a picture using your camera.")

mode = st.radio(
    "Choose image source",
    ["📁 Upload Image", "📷 Use Camera"],
    horizontal=True,
    label_visibility="collapsed"
)

uploaded = None

if mode == "📁 Upload Image":
    uploaded = st.file_uploader(
        "Choose a leaf image",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG and PNG"
    )
else:
    uploaded = st.camera_input("Take a picture of a plant leaf")

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")

    st.markdown("#### Image Preview")
    st.image(image, use_container_width=True)

    st.markdown(
        '<div class="info-card">✅ Image ready for analysis</div>',
        unsafe_allow_html=True
    )

    if st.button("🔬 Predict Disease", type="primary"):
        try:
            with st.spinner("Analyzing your plant image..."):
                result = predict_image(image)

            st.markdown("### 📋 Prediction Result")
            st.markdown(
                f"""
                <div class="result-card">
                    <h3>🌱 Predicted Class</h3>
                    <h2>{result['disease'].replace('___', ' - ').replace('_', ' ')}</h2>
                    <p><b>Confidence:</b> {result['confidence']}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                "Prediction is based on the model's 15 trained classes. "
                "Results may be inaccurate for unfamiliar images or "
                "real-world conditions."
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")

else:
    st.markdown("""
    <div class="info-card">
        <h4>📸 Ready to get started?</h4>
        <p>Select a clear image of a plant leaf to begin.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Plant Disease Detection · CNN · PyTorch · FastAPI")
