from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the trained model
model = joblib.load('xgb.pkl')

# Add at the top of the file, after the app initialization
temp_predictions = None

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files.get('file')
        if file is None:
            return jsonify({'error': 'No file provided'}), 400

        # Read the CSV file
        df = pd.read_csv(file)
        print(f'Original columns: {df.columns.tolist()}')

        # Find and store IP column
        ip_column = None
        possible_ip_columns = ['ip', 'IP', 'ip_address', 'IP_Address', 'source_ip', 'src_ip']
        for col in possible_ip_columns:
            if col in df.columns:
                ip_column = col
                break

        if ip_column is None:
            raise ValueError(f"No IP address column found. Available columns: {df.columns.tolist()}")

        # Store IP addresses
        ip_addresses = df[ip_column].copy()
        
        # Drop IP column for model prediction
        df = df.drop(columns=[ip_column])
        print(f'Columns after dropping IP: {df.columns.tolist()}')
        print(f'DataFrame shape: {df.shape}')

        # Make predictions
        predictions = model.predict(df.to_numpy())
        print(f'Predictions shape: {predictions.shape}')

        # Store predictions with IP addresses for later use
        prediction_data = pd.DataFrame({
            'ip_address': ip_addresses,
            'prediction': predictions
        })
        # Store in Flask session or temporary file
        global temp_predictions
        temp_predictions = prediction_data

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

@app.route('/block', methods=['POST'])
def block():
    try:
        # Get the file from the request
        file = request.files.get('file')
        if file is None:
            return jsonify({'error': 'No file provided'}), 400

        # Read the CSV file
        df = pd.read_csv(file)
        print(f'Column names: {df.columns.tolist()}')  # Debug print

        # Make predictions
        predictions = model.predict(df.to_numpy())

        # Create a DataFrame with IP addresses and their classifications
        df['prediction'] = predictions
        
        # Get the IP address column name (assuming it might be 'IP' or 'ip_address' or similar)
        ip_column = None
        possible_ip_columns = ['ip', 'IP', 'ip_address', 'IP_Address', 'source_ip', 'src_ip']
        for col in possible_ip_columns:
            if col in df.columns:
                ip_column = col
                break
        
        if ip_column is None:
            raise ValueError(f"No IP address column found. Available columns: {df.columns.tolist()}")
        
        # Filter for low-rated (2) and high-rated (0) attacks
        blocked_ips = df[df['prediction'].isin([0, 2])][ip_column].unique()
        
        # Create a DataFrame with blocked IPs
        blocked_df = pd.DataFrame(blocked_ips, columns=['Blocked IP Address'])
        
        # Add attack type classification
        blocked_df['Attack Type'] = ['High-Rated Attack' if pred == 0 else 'Low-Rated Attack' 
                                   for pred in df[df[ip_column].isin(blocked_ips)]['prediction']]
        
        # Create an in-memory buffer
        buffer = io.StringIO()
        blocked_df.to_csv(buffer, index=False)
        buffer.seek(0)
        
        return send_file(
            io.BytesIO(buffer.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='blocked_ips.csv'
        )

    except Exception as e:
        print(f'Error details: {str(e)}')  # Detailed error logging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
     app.run(debug=True, port=5174)
