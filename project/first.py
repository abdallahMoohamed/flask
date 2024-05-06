from flask import Flask, request, jsonify
# from flask_uploads import UploadSet, IMAGES, configure_uploads

import joblib

app = Flask(__name__)

# Load the pre-trained model
# model = joblib.load('your_model.pkl')
##############################################################
# Configure Flask-Uploads
# images = UploadSet('images', IMAGES)  # Set allowed extensions
# app.config['UPLOADED_IMAGES_DEST'] = 'uploads/'  # Specify a directory to store uploaded images
# configure_uploads(app, images)
##############################################################
@app.route('/')
def index():
    return 'Welcome to Model Deployment with Flask!'

@app.route('/predict', methods=['POST'])
def predict():
  
    # Get input data
    if 'image' not in request.files:
      return 'No file part in the request'
    image = request.files['image']
    
    # Check if file is None or empty filename
    if image.filename == '':
      return 'No selected file'
     
    # Check format of file
    if image and allowed_file(image.filename):
      print(image.filename)
      response = {"image":image.filename}
      return jsonify(response)
    else:
      return "Unsupported file format"

def allowed_file(filename):
    # Add allowed file extensions here
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)


# if file and allowed_file(file.filename):
#   # Read image file
#   image = image.open(file)
  
  
#   # # Make predictions
#   # prediction = model.predict(image)
#   print(image)
#   # Prepare response
#   response = {'prediction': image}
  
#   return jsonify(response)
# else:
#   return 'Unsupported file format'

# data = request.form
# print({file.path})
# Preprocess input data (if needed)
# For example, convert JSON data to features

# Make predictions
# prediction = model.predict(data)

# Prepare response
# response = {'prediction': prediction.tolist()}

# return (file)