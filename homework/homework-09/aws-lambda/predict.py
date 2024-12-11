import tensorflow as tf
from PIL import Image
import numpy as np
import requests
from io import BytesIO

# Model file path
MODEL_PATH = "./model_2024_hairstyle_v2.tflite"

# Preprocess the input image
def preprocess_image(image_url, target_size=(200, 200)): 
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    img = img.resize(target_size)
    img = np.array(img, dtype=np.float32) / 255.0  # Rescale to [0, 1]
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Load TensorFlow Lite model
def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# Perform inference
def predict(image_url):
    interpreter = load_tflite_model(MODEL_PATH)
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Preprocess input
    input_data = preprocess_image(image_url)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    # Run inference
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data[0][0]

# AWS Lambda handler
def lambda_handler(event, context):
    try:
        image_url = event['image_url']
        result = predict(image_url)
        response = {
            "statusCode": 200,
            "body": {"prediction": round(float(result), 4)}
        }

        # Ensure that the body is printed with the result on the next line
        print(f"{response['statusCode']}")
        print(f"{response['body']}")
        
        return response
        
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": {"error": str(e)}
        }
        print(f"{response['statusCode']}")
        print(f"{response['body']}")
        
        return response
