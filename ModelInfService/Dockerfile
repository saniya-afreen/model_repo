# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY ./ModelInfService/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./ModelInfService/main.py .

# Expose the default FastAPI port
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
