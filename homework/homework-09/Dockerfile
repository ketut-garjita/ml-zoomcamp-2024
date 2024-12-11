FROM public.ecr.aws/lambda/python:3.10

# Install TensorFlow and compatible NumPy version
RUN pip install tensorflow==2.14.0
RUN pip install numpy==1.23.1
RUN pip install pillow
RUN pip install requests

# Copy the Lambda function code
COPY lambda_code.py /app/lambda_code.py
COPY model_2024_hairstyle_v2.tflite /app/model_2024_hairstyle_v2.tflite

# Set work directory
WORKDIR /app

ENTRYPOINT ["python", "lambda_code.py"]

