FROM python:3.10-slim

WORKDIR /app

COPY . /app
# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libespeak-dev \
    portaudio19-dev \
    && apt-get clean

COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt


CMD ["python", "chatbot5.py"]
