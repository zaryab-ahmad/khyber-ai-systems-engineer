
# Use an optimized Python 3.14.3 image
FROM python:3.14.3-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Command to run the production server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
