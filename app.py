from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your pre-trained model
model = joblib.load('path/to/your/model.pkl')

# Sample encoding dictionary for species (replace with your actual encoding)
species_encoding = {
    'Bream': 0,
    'Roach': 1,
    'Whitefish': 2,
    'Parkki': 3,
    'Perch': 4,
    'Pike': 5,
    'Smelt': 6
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    
    try:
        # Encode the species
        species = features[0]
        if species in species_encoding:
            species_encoded = species_encoding[species]
        else:
            return jsonify({"error": "Unknown species"}), 400

        # Replace species with its encoded value
        features[0] = species_encoded
        
        # Convert the features list to a numpy array
        features_array = np.array([features])
        
        # Make prediction
        prediction = model.predict(features_array)
        
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
