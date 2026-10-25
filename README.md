# Plant Disease Detection

A deep learning project that identifies plant diseases from leaf images using a CNN model. Users can upload an image or capture one using their camera to get a prediction with a confidence score.

## Features

- Upload a plant leaf image for disease detection
- Capture an image using the device camera
- Predict disease using a trained CNN model
- Display the predicted class and confidence score
- FastAPI backend with a simple web interface

## Technologies Used

- Python
- PyTorch
- CNN (Convolutional Neural Network)
- FastAPI
- HTML, CSS, JavaScript
- Pillow

## Project Structure

```text
Plant-Disease-Detection/
├── app/
│   ├── main.py
│   ├── model.py
│   └── predict.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── models/
│   ├── best_model.pth
│   └── class_to_idx.json
├── requirements.txt
└── .gitignore
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Rayhan043/Plant-Disease-Detection.git
cd Plant-Disease-Detection
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
uvicorn app.main:app --reload
```

Open the API documentation at:

http://127.0.0.1:8000/docs

Open `frontend/index.html` in your browser to use the web interface. Keep the backend running while using the frontend.

## Model Performance

- Test accuracy: **88.76%**
- Model: Convolutional Neural Network (CNN)
- Dataset: PlantVillage
- Number of classes: 15

*Accuracy may vary depending on image quality and the conditions of the uploaded image.*

## Limitations

The model was trained on plant leaf images from the PlantVillage dataset. It may produce incorrect predictions for images outside its training classes, including non-leaf images. Predictions should be treated as a reference, not a confirmed diagnosis.

## Future Improvements

- Improve detection of non-leaf images
- Add more diverse real-world leaf images
- Improve prediction reliability
- Deploy the application online

## Author

**Rayhan Chowdhury**

GitHub: [Rayhan043](https://github.com/Rayhan043)
