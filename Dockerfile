# Dockerfile for a custom image that includes numpy and sympy
FROM python:3.12-bookworm

# Install any packages you need
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies here
RUN pip install --no-cache-dir numpy sympy

# Keep the container alive during Inspect’s evaluation
CMD ["tail", "-f", "/dev/null"] 