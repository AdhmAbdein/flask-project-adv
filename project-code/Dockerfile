# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY ./project-code /app

# Upgrade pip to ensure we have the latest version
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (Flask default is 5000)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

