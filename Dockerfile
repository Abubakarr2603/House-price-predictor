# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements and install them
# (You will need a requirements.txt with: fastapi uvicorn pandas scikit-learn pydantic joblib)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your main.py and all the .joblib model files into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to keep the server running continuously
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]