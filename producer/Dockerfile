FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Install netcat (correct version)
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy app files
COPY . .

# Make wait script executable
RUN chmod +x wait-for-kafka.sh

CMD ["./wait-for-kafka.sh"]
