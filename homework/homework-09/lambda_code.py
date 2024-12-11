import argparse
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

def preprocess_image(image_path):
    target_size = (200, 200)  # Replace with the target size 
    img = Image.open(image_path).resize(target_size)
    img = np.array(img) / 255.0  # Rescale pixel values
    img = np.expand_dims(img, axis=0).astype(np.float32)
    return img

def main(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        # Save the image as 'input_image.jpeg'
        img = Image.open(BytesIO(response.content))
        image_path = 'input_image.jpeg'  # Save in the current working directory
        img.save(image_path)
    else:
        print(f"Error: Failed to download the image. Status code: {response.status_code}")
        return
    
    # Load the TFLite model
    model_path = "model_2024_hairstyle_v2.tflite"  # Make sure model is in the container
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Get input and output tensor details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Preprocess the input image
    input_data = preprocess_image(image_path)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Get the model's output
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(f"Model Output: {output_data[0][0]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image URL input for TFLite model")
    parser.add_argument("image_url", help="URL of the image to process")
    args = parser.parse_args()
    main(args.image_url)
