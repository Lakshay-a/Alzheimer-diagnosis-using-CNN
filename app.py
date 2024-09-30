import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained model
model = load_model('densenet_best (1).h5')  # Change this to your model path

# Define the image size expected by the model
IMG_SIZE = (224, 224)

# Preprocess the uploaded image
def preprocess_image(img):
    img = img.resize(IMG_SIZE)  # Resize the image to match model input size
    img = np.array(img)         # Convert to NumPy array
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0           # Normalize pixel values
    return img

# Define the prediction function
def predict(image):
    img = preprocess_image(image)
    prediction = model.predict(img)
    class_names = ["Alzheimer Disease", "Cognitive Normal","Mild Cognitive Impairment"]  # Modify class names as needed
    predicted_class = class_names[np.argmax(prediction)]  # Get predicted class
    return predicted_class

# Create a Gradio interface
interface = gr.Interface(fn=predict, 
                         inputs=gr.Image(type="pil"), 
                         outputs="text", 
                         title="Alzheimer's Disease Classifier",
                         description="Upload a brain scan image to classify Alzheimer's Disease.")

# Launch the app
interface.launch()
