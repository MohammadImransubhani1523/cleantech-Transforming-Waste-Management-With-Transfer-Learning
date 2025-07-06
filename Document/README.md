# Municipal Waste Classification Web App

This is a Flask-based web application that classifies uploaded waste images into categories like **Biodegradable**, **Recyclable**, or **Trash** using a trained deep learning model.

## 🌐 Features

- Upload waste images and get real-time classification results.
- Deep learning model (e.g., VGG16-based) for accurate predictions.
- Responsive UI built with Bootstrap 5.
- Separate pages for Home, About, Predict, and Contact.

## 📁 Project Structure

```
project/
│
├── app.py                  # Main Flask application
├── vgg16.h5                # Trained Keras model file
├── README.md               # This file
│
├── templates/              # HTML templates
│   ├── index.html          # Home page
│   ├── about.html          # About page
│   ├── predict.html        # Image upload and result
│   └── contact.html        # Contact form (non-functional)
│
├── static/                 # Static files (CSS, JS, images)
│   ├── uploads/            # Where uploaded images are saved
│   └── assets/             # Optional: logos, hero background etc.
```

## ⚙️ How to Run

1. **Install dependencies**:
   ```bash
   pip install flask tensorflow pillow
   ```

2. **Run the Flask app**:
   ```bash
   python app.py
   ```

3. Open your browser and go to: [http://localhost:2222](http://localhost:2222)

## 🧠 Model Information

- The app loads a pre-trained Keras model (`vgg16.h5`).
- The model expects input size of **224x224**.
- Prediction output maps to labels:  
  `['Biodegradable', 'Recyclable', 'Trash']` *(can be customized)*

## 📷 Usage

1. Navigate to the **Predict** page.
2. Upload an image (JPEG/PNG).
3. Click **Predict**.
4. View classification result with image preview.

## 📬 Contact

For questions or suggestions, contact:
**NutriGaze Team**  
📧 NurriqazeCorp@example.com  
📍 Mediphatnam, Hyderabad

---

**Note**: This is a demo and not production-optimized. Secure file handling, error checking, and deployment hardening are recommended for public use.