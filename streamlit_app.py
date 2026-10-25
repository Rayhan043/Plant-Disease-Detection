
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
    background: linear-gradient(180deg, #edf8ef 0%, #f8faf8 50%, #ffffff 100%);
    color: #1f2937;
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
    text-align: center;
    margin-bottom: 28px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 32px;
}

.hero p {
    color: #e4f5e8 !important;
    font-size: 16px;
}

.stApp h2,
.stApp h3,
.stApp h4,
.stApp p,
.stApp label {
    color: #1f2937;
}

.info-card {
    background: #ffffff;
    color: #1f2937;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #dce9df;
    margin: 12px 0;
}

.result-card {
    background: #e5f6e9;
    color: #14532d;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #a7d9b3;
    margin-top: 20px;
}

.result-card h2,
.result-card h3,
.result-card p {
    color: #14532d !important;
}

div.stButton > button {
    background: #198044;
    color: #ffffff !important;
    border: none;
    border-radius: 10px;
    min-height: 48px;
    font-weight: 600;
    width: 100%;
}

div.stButton > button:hover {
    background: #126534;
    color: #ffffff !important;
}

div[data-testid="stFileUploader"] {
    background: #ffffff;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #dce9df;
}

div[data-testid="stFileUploader"] * {
    color: #1f2937;
}

div[data-testid="stRadio"] label {
    color: #1f2937 !important;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# Header
st.markdown("""
<div class="hero">
    <h1>🌿 Plant Disease Detection</h1>
    <p>Check your plant's health with AI-powered image analysis.</p>
</div>
""", unsafe_allow_html=True)


# Image selection
st.markdown("### 🔍 Analyze Your Plant")
st.write("Upload a leaf image or take a photo using your camera.")

mode = st.radio(
    "Choose image source",
    ["📁 Upload Image", "📷 Use Camera"],
    horizontal=True,
    label_visibility="collapsed"
)

uploaded = None

if mode == "📁 Upload Image":
    uploaded = st.file_uploader(
        "Choose a plant leaf image",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG and PNG"
    )
else:
    uploaded = st.camera_input("Capture a plant leaf")


# Preview and prediction
if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")

    st.markdown("### 🖼️ Image Preview")
    st.image(image, use_container_width=True)

    st.markdown("""
    <div class="info-card">
        ✅ Image ready for analysis
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔬 Predict Disease", type="primary"):
        try:
            with st.spinner("Analyzing your plant image..."):
                result = predict_image(image)

            disease = (
                result["disease"]
                .replace("___", " - ")
                .replace("_", " ")
            )
            confidence = result["confidence"]

            st.markdown("### 📋 Prediction Result")

            st.markdown(
                f"""
                <div class="result-card">
                    <h3>🌱 Predicted Disease</h3>
                    <h2>{disease}</h2>
                    <p><b>Confidence:</b> {confidence}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                "The model supports 15 trained classes. "
                "It may misclassify non-leaf images or leaves "
                "captured under conditions unlike its training data. "
                "This prediction is not a confirmed diagnosis."
            )

        except Exception as error:
            st.error(f"Prediction failed: {error}")

else:
    st.markdown("""
    <div class="info-card">
        <h4>📸 Ready to get started?</h4>
        <p>Select a clear plant leaf image or use your camera.</p>
    </div>
    """, unsafe_allow_html=True)


st.divider()
st.caption("Plant Disease Detection · CNN · PyTorch · Streamlit")
