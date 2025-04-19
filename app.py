from flask import Flask, request, jsonify, render_template_string
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from sklearn.preprocessing import LabelEncoder
import numpy as np
from PIL import Image
import pickle
import io

app = Flask(__name__)

# Load model
model = load_model('fashion.h5')  # make sure the correct name is used

# Load label encoders
label_encoders = {}
for col in ['baseColour', 'articleType', 'season', 'gender']:
    with open(f'{col}_encoder.pkl', 'rb') as f:
        label_encoders[col] = pickle.load(f)

# Image processing
def process_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# HTML template
HTML_PAGE = '''
<!doctype html>
<title>Fashion Classifier</title>
<h1>Upload an image to predict fashion attributes</h1>
<form method=post enctype=multipart/form-data action="/predict">
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
{% if result %}
<h2>Prediction:</h2>
<ul>
  <li><strong>Color:</strong> {{ result['Color'] }}</li>
  <li><strong>Article Type:</strong> {{ result['Article Type'] }}</li>
  <li><strong>Season:</strong> {{ result['Season'] }}</li>
  <li><strong>Gender:</strong> {{ result['Gender'] }}</li>
</ul>
{% endif %}
'''

# Home route
@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template_string(HTML_PAGE, result={'error': 'No file uploaded'})

    file = request.files['file']
    img_bytes = file.read()
    img_input = process_image(img_bytes)

    predictions = model.predict(img_input)

    color_pred = label_encoders['baseColour'].inverse_transform([np.argmax(predictions[0][0])])[0]
    article_pred = label_encoders['articleType'].inverse_transform([np.argmax(predictions[1][0])])[0]
    season_pred = label_encoders['season'].inverse_transform([np.argmax(predictions[2][0])])[0]
    gender_pred = label_encoders['gender'].inverse_transform([np.argmax(predictions[3][0])])[0]

    result = {
        'Color': color_pred,
        'Article Type': article_pred,
        'Season': season_pred,
        'Gender': gender_pred
    }

    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
