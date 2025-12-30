# Base Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir inside the container
WORKDIR /app

# Install system deps (optional) and Python deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source
COPY . /app

# If it’s a web app, make the port visible (adjust if needed)
EXPOSE 8000

# Default command (change main.py to your entry file)
CMD ["python", "wordcount.py"]
