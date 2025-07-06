from flask import Flask, render_template, request, url_for
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import tensorflow as tf

app = Flask(__name__)

# Ensure upload directory exists
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load pre-trained model
model = tf.keras.models.load_model('vgg16.h5')

# Home route
@app.route('/')
def index():
    return render_template("index.html")

# Predict route
@app.route('/predict', methods=['POST'])
def output():
    if 'pc_image' not in request.files:
        return "No file part", 400

    f = request.files['pc_image']
    if f.filename == '':
        return "No selected file", 400

    img_path = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(img_path)

    # Preprocess the image
    img = load_img(img_path, target_size=(224, 224))
    image_array = img_to_array(img) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Predict
    pred = np.argmax(model.predict(image_array), axis=1)
    index = ['Biodegradable Images (0)', 'Recyclable Images (1)', 'Trash Images (2)']
    prediction = index[int(pred)]

    print("Prediction result:", prediction)

    return render_template("portfolio-details.html", predict=prediction, uploaded_file=img_path)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=2222)
