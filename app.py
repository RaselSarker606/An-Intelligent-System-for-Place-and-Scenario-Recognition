import streamlit as st
import google.generativeai as genai
import os
import PIL.Image

# Set API Key for Google Gemini
os.environ["GOOGLE_API_KEY"] = "Your API Here"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load the Gemini Model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


# Function to generate place/scenario info
def get_scene_info(image):
    prompt = """
    You are an expert AI trained in recognizing places, institutions, or public scenarios from images.

    Carefully analyze the uploaded image and provide detailed structured information.
    If the image depicts a known location, institution, or public scenario, return the following:

    - **Official Name**: (e.g., University of Oxford, Eiffel Tower, etc.)
    - **Type**: (e.g., University, Park, Landmark, Historical Site, etc.)
    - **Country or Context**: (e.g., United Kingdom, Academic Institution, etc.)
    - **Established**: (Founding year or approximate date if known)
    - **Owner / Authority**: (Organization or government body that operates or owns it)
    - **Description**: (A brief summary of the place or scenario)

    If no recognizable place or institution is found, return:
    - **Official Name**: Unknown
    - **Type**: Unknown
    - **Country or Context**: Unknown
    - **Established**: Unknown
    - **Owner / Authority**: Unknown
    - **Description**: Unknown
    """
    response = model.generate_content([prompt, image])
    return response.text.strip()



# Streamlit App
st.title("Place or Scenario Detection")
st.write("Upload an image, and the app will analyze and describe the place or scene.")

# Image Upload
uploaded_image = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

if uploaded_image:
    # Open image
    img = PIL.Image.open(uploaded_image)

    # Analyze with Gemini
    with st.spinner("Analyzing image..."):
        scene_info = get_scene_info(img)

    # Layout: Image and Info side-by-side
    col1, col2 = st.columns(2)

    with col1:
        st.image(img, caption="Uploaded Image", use_container_width=True)

    with col2:
        st.subheader("Detected Scene Information")
        st.markdown(scene_info)
