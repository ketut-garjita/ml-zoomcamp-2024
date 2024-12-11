# Base image for AWS Lambda
FROM public.ecr.aws/lambda/python:3.10

# Set working directory
WORKDIR /var/task

# Copy TensorFlow Lite model and script
COPY model_2024_hairstyle_v2.tflite ./model_2024_hairstyle_v2.tflite
COPY predict.py ./predict.py

# Install required libraries
RUN pip install tensorflow==2.14.0 numpy==1.23.5 pillow requests

# Set the Lambda handler
CMD ["predict.lambda_handler"]
