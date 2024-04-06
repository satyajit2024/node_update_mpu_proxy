# Use a base image with Python installed
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3-gpiozero && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install spidev gpiozero RPi.GPIO pycryptodome

# Copy the Python script and any other required files into the container
COPY . /app

# Command to run when the container starts
CMD [ "python", "./new_proxy.py" ]
