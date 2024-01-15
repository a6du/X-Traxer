# Use the official Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire backend code to the working directory
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 5000

# Set environment variables (optional, adjust as needed)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Start the FastAPI server
CMD ["flask","run"]
