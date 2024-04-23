# Use the official Python image as a base image
FROM python:3.9-slim

# Install Flask
RUN pip install flask

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at ./src/. .
COPY ./src/. .

# Set the environment variable
ENV FLAG="CTF_SDaT{H3r3s_Your_Fl4g_Cryp70_M45t3rm1nd}"

# Expose the port on which your Flask app will run
EXPOSE 5000

# Define the command to run your Flask app when the container starts
CMD ["python3", "main.py"]

