# Base image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies only if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Necessary app files
COPY app/ ./app
COPY model/ ./model 
#COPY config/ ./config  

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI (no reload in production)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
