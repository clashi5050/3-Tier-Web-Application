# Use a lightweight Python base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /code

# Install dependencies (flask and redis)
RUN pip install flask redis

# Copy our python script into the container
COPY app.py .

# Command to run the application
CMD ["python", "app.py"]