# ✨ Place or Scenario Detection System

## 📖 Overview

This app recognize and describe places, institutions, or public scenes from uploaded images. Whether it's a photo of a university, historical monument, or public building, the app returns detailed structured information like its name, type, country, founding year, and more—all via a simple Streamlit interface.

---

## 📂 Features

- 🖼️ **Image-Based Scene Recognition**  
  Detects landmarks, buildings, parks, institutions, and more.

- 📋 **Structured Output Format**  
  Includes:
  - Official Name  
  - Type (e.g., University, Landmark)  
  - Country or Context  
  - Year Established  
  - Owner/Authority  
  - Description

- 💡 **Gemini-Powered AI**  
  Uses the Gemini 1.5 Flash model to interpret the image and generate the response.

- ⚡ **Streamlit Interface**  
  Easy-to-use app for image upload and result viewing.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **Google Generative AI SDK**
- **Pillow (PIL)** – Image handling

---

## 🚀 Setup Instructions

### 📦 Prerequisites

- Python 3.7 or higher
- Google API Key with access to Gemini

### 🔧 Installation

```bash
git clone https://github.com/your-username/place-scene-detector.git
cd place-scene-detector
pip install streamlit google-generativeai pillow
```

### 🔑 Add Your API Key

Update the `app.py` file:
```python
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Visit in your browser:  
`http://localhost:8501/`

---

## 📸 Example Use Cases

- Upload a photo of a landmark (e.g., Eiffel Tower)
- Upload a photo of a university building (e.g., MIT)
- Upload a street or park image for public space detection

The app will return structured details—or “Unknown” if it can't recognize the scene.

---

## 📌 Future Enhancements

- 🌍 **Interactive Map Integration**
- 🗣️ **Multilingual Output Support**
- 📥 **Drag & Drop + Camera Upload**
- 🔐 **User Authentication for Private Use**

---

🚀 **Discover what's in your photo—instantly.**
