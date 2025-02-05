# Official Python runtime as a parent image
FROM python:3.11

# Working directory
WORKDIR /app

# Current directory contents into the container
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]
