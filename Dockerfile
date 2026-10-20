FROM python:3.12-slim

WORKDIR /app

# Prevent Python from writing bytecode files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python logs immediately
ENV PYTHONUNBUFFERED=1

# Install dependencies first to improve build caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY backend.py .
COPY mcp_client.py .
COPY frontend.py .
COPY pdf_generator.py .

# Streamlit configuration
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose Streamlit's port
EXPOSE 8501

# Start the application
CMD ["streamlit", "run", "frontend.py"]