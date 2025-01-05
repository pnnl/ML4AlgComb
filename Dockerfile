# Dockerfile for a custom image that includes numpy, sympy, and sage
FROM python:3.12-bookworm

# Install any packages you need
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       curl \
    && rm -rf /var/lib/apt/lists/*

# Install Miniforge (recommended for SageMath installation)
RUN curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-$(uname -m).sh" \
    && bash Miniforge3-Linux-$(uname -m).sh -b -p /opt/conda \
    && rm Miniforge3-Linux-$(uname -m).sh

# Add conda to path
ENV PATH="/opt/conda/bin:${PATH}"

# Create and activate environment with sage
RUN conda create -n sage -c conda-forge sage python=3.9 -y \
    && conda run -n sage pip install --no-cache-dir numpy sympy

# Set the default conda environment
ENV CONDA_DEFAULT_ENV=sage
ENV CONDA_PREFIX=/opt/conda/envs/sage

# Keep the container alive during Inspect's evaluation
CMD ["tail", "-f", "/dev/null"] 