# Use the official Python image as the base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /django_app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the working directory
COPY . .

# RUN chmod +x start_web.sh start_celery.sh     ||if it enabled, the last line not required||

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the ASGI server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]
