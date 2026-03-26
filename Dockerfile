FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
# Build-essential is required for some C-extensions like chromadb
RUN apt-get update && apt-get install -y build-essential curl

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy course material
COPY . /app

EXPOSE 8888

# Launch Jupyter Lab indefinitely for student access
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]
