
let cameraStream = null;

async function startCamera() {
    const camera = document.getElementById("camera");
    const result = document.getElementById("result");

    try {
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: "environment" },
            audio: false
        });

        camera.srcObject = cameraStream;
        result.textContent = "Camera ready. Capture a leaf image.";
    } catch (error) {
        result.textContent = "Camera error: " + error.message;
    }
}

async function captureImage() {
    const camera = document.getElementById("camera");
    const canvas = document.getElementById("canvas");
    const preview = document.getElementById("preview");

    if (!cameraStream || !camera.videoWidth) {
        document.getElementById("result").textContent =
            "Please start the camera first.";
        return;
    }

    canvas.width = camera.videoWidth;
    canvas.height = camera.videoHeight;

    canvas.getContext("2d").drawImage(camera, 0, 0);

    canvas.toBlob(async function(blob) {
        if (!blob) return;

        preview.src = URL.createObjectURL(blob);
        preview.hidden = false;

        const formData = new FormData();
        formData.append("file", blob, "leaf.jpg");

        await sendImage(formData);
    }, "image/jpeg");
}

async function predictDisease() {
    const input = document.getElementById("imageInput");

    if (!input.files[0]) {
        document.getElementById("result").textContent =
            "Please select an image first.";
        return;
    }

    const preview = document.getElementById("preview");
    preview.src = URL.createObjectURL(input.files[0]);
    preview.hidden = false;

    const formData = new FormData();
    formData.append("file", input.files[0]);

    await sendImage(formData);
}

async function sendImage(formData) {
    const result = document.getElementById("result");
    result.textContent = "Detecting disease...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Prediction failed");
        }

        result.textContent =
            `Disease: ${data.disease} | Confidence: ${data.confidence}%`;
    } catch (error) {
        result.textContent = "Error: " + error.message;
    }
}
