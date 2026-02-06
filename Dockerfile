# Use official Python image
FROM python:3.11-slim-stretch

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install pytest pydantic
    
# Default command runs tests
CMD ["pytest", "-q"]

