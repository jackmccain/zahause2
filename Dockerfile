# Use the official Python image as a parent image
FROM python:3.10-slim

# Create a directory for the app
WORKDIR /app

# Copy requirements.txt first, install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port (for local testing, not strictly required by Cloud Run)
EXPOSE 8080

# The command to start your Flask app
CMD ["python", "app.py"]