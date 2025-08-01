import json
import boto3
import joblib
import os
import tempfile
import numpy as np

# Load model from S3 on cold start
s3 = boto3.client('s3')
MODEL_BUCKET = 'your-s3-bucket-name'  # ✅ Replace with your actual S3 bucket
MODEL_KEY = 'health_model.pkl'        # ✅ Ensure this matches your uploaded key

# Use a temporary file to store model locally
model_path = os.path.join(tempfile.gettempdir(), 'health_model.pkl')

try:
    s3.download_file(MODEL_BUCKET, MODEL_KEY, model_path)
    model = joblib.load(model_path)
except Exception as e:
    model = None
    print(f"Model loading failed: {e}")

def lambda_handler(event, context):
    if model is None:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Model not loaded"})
        }

    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        # Extract input features from request
        age = float(body["age"])
        weight = float(body["weight"])
        body_temp = float(body["body_temp"])
        bp_systolic = float(body["bp_systolic"])
        cholesterol = float(body["cholesterol"])

        # Prepare input for prediction
        input_data = np.array([[age, weight, body_temp, bp_systolic, cholesterol]])

        # Perform prediction
        prediction = model.predict(input_data)[0]
        risk = "At Risk" if prediction == 1 else "Healthy"

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": int(prediction),
                "health_status": risk
            })
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
