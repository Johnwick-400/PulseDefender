from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the trained model and scaler
model = joblib.load('xgb.pkl')
  # Load the same scaler used during training

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the file from the request
        file = request.files.get('file')
        if file is None:
            return jsonify({'error': 'No file provided'}), 400

        # Read the CSV file
        df = pd.read_csv(file)
        print(f'Column names: {df.columns.tolist()}')
        print(f'DataFrame shape: {df.shape}')

        # Expected features
    

       
        print(f'Features shape after scaling: {df.shape}')

        # Make predictions
        predictions = model.predict(df.to_numpy())  # Removes feature name No need for np.argmax here
        print(f'Predictions shape: {predictions.shape}')
        print(predictions)
        # Count predictions
        legitimate_count = np.sum(predictions == 1)
        low_rated_count = np.sum(predictions == 2)
        high_rated_count = np.sum(predictions == 0)

        return jsonify({
            'legitimate_count': int(legitimate_count),
            'low_rated_count': int(low_rated_count),
            'high_rated_count': int(high_rated_count)
        })

    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=10000)
