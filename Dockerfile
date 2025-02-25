# Use Ubuntu as base image
FROM ubuntu:24.04

# Set environment variable to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update Ubuntu and install Python
RUN apt update && apt install -y python3

# Copy Python script into the container
COPY wd_storage_info.py /wd_storage_info.py

# Set working directory
WORKDIR /

# Run the script when the container starts
CMD ["python3", "/wd_storage_info.py"]
