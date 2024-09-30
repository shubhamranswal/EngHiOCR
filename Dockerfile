# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-hin && apt-get clean

# Copy the requirements file
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]