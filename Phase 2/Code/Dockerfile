# Start with a clean Python environment
FROM python:3.14-slim

# Set the working folder inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our library code into the container
COPY . .

# Run our vision engine test when the container starts
CMD ["python", "-c", "from this_course_vision.processor import process_thermal; print(process_thermal('Docker_Test_Image.png'))"]