import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Step 1: Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights='imagenet')
class_names = tf.keras.applications.mobilenet_v2.decode_predictions

# Step 2: Function to preprocess and predict if an image contains a cat
def predict_image(image):
    # Resize and preprocess the image for MobileNetV2
    image = image.resize((224, 224))  # MobileNetV2 expects 224x224 images
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)

    # Make prediction
    predictions = model.predict(image_array)
    decoded_predictions = class_names(predictions, top=5)[0]

    # Check if any prediction is a cat (ImageNet has specific labels for cats)
    cat_labels = ['tabby', 'tiger_cat', 'Persian_cat', 'Siamese_cat', 'Egyptian_cat']
    for pred in decoded_predictions:
        label = pred[1].lower()
        confidence = pred[2]
        if any(cat_label in label for cat_label in cat_labels):
            return True, confidence, label
    return False, decoded_predictions[0][2], decoded_predictions[0][1]

# Step 3: Streamlit App Setup
st.title("🐾 Cat Spotter AI")
st.markdown("Welcome to Day 4 of the AI Toolbox Adventure! Let’s see how AI learns to recognize cats with machine learning!")

# Step 4: Educational Section
st.subheader("How Does AI Learn to Spot Cats? 🧠")
st.write("""
- **Machine Learning Magic:** AI learns by looking at examples—like thousands of photos of cats and non-cats!  
- **Training Process:**  
  1. We show the AI lots of pictures (e.g., cats, dogs, cars).  
  2. We tell it which ones are cats (“This is a cat!”) and which aren’t (“This is not a cat.”).  
  3. The AI learns patterns (e.g., cats have whiskers, pointy ears) to guess if a new picture is a cat.  
- **Fun Fact:** This AI was trained on a huge dataset called ImageNet, which has millions of labeled images!  
""")

# Step 5: Image Upload or Sample Selection
st.subheader("Test the Cat Spotter AI! 🐱")
option = st.radio("Choose an option:", ("Upload your own image", "Use a sample image"))

if option == "Upload your own image":
    uploaded_file = st.file_uploader("Upload an image (jpg, png):", type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Your uploaded image", use_column_width=True)
else:
    # Sample images (hosted URLs for demo purposes)
    sample_images = {
        "Cat": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg",
        "Dog": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/1200px-Cute_dog.jpg",
        "Car": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Red_Car.jpg/1200px-Red_Car.jpg"
    }
    sample_choice = st.selectbox("Pick a sample image:", list(sample_images.keys()))
    response = requests.get(sample_images[sample_choice])
    image = Image.open(BytesIO(response.content))
    st.image(image, caption=f"Sample image: {sample_choice}", use_column_width=True)

# Step 6: Make Prediction
if st.button("Spot the Cat!"):
    is_cat, confidence, label = predict_image(image)
    if is_cat:
        st.success(f"This is a cat! 🐾 (Confidence: {confidence:.2%}, Type: {label})")
    else:
        st.warning(f"This isn’t a cat. It’s a {label}. (Confidence: {confidence:.2%})")

# Step 7: Call to Action
st.subheader("Share Your Results! 📸")
st.write("Did the AI spot a cat in your image? Share your result in our Discord #cat-spotter-ai channel! #AILearning")

# Step 8: Footer
st.write("Built with ❤️ for AI beginners! #AIToolbox")