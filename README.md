# 🛒 Kafka Producer for E-Commerce Order Events

This project is a **Kafka producer application** that simulates e-commerce order events and streams them to a Kafka topic named `order-events`. It's designed to demonstrate a real-time data ingestion pipeline using Kafka and can serve as a starting point for analytics, fraud detection, or order processing systems.

---

## 🚀 Features

- ✅ Generates synthetic e-commerce order data (JSON)
- ✅ Streams events to Apache Kafka in real-time
- ✅ Dockerized setup with Kafka and Zookeeper
- ✅ Startup script waits for Kafka to be ready (`wait-for-kafka.sh`)

---

## 🧱 Tech Stack

- **Python 3.10**
- **Apache Kafka**
- **Docker & Docker Compose**
- **Confluent Kafka Python Client**

---

## 📁 Project Structure

```bash
Kafka_Producer_Ecommerce_sales_stream/
├── producer/
│   ├── producer.py
│   ├── wait-for-kafka.sh
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

- Docker & Docker Compose installed
- Python 3.10+ (if running locally)
- Git (optional)

---

## 🛠️ Setup and Run

### ✅ 1. Clone the repo

```bash
git clone https://github.com/your-username/Kafka_Producer_Ecommerce_sales_stream.git
cd Kafka_Producer_Ecommerce_sales_stream
```

### ✅ 2. Build and Run with Docker

```bash
docker-compose up --build
```

This will:
- Start Zookeeper and Kafka
- Build the Python producer image
- Wait for Kafka to be ready
- Start streaming `order-events` data

---

## 🧪 Sample Order Event

Each event is a JSON object structured like this:

```json
{
  "order_id": "ORD123456",
  "customer_id": "CUST987654",
  "timestamp": "2025-07-15T18:29:00Z",
  "amount": 259.99,
  "currency": "INR",
  "items": [
    {"sku": "SKU123", "quantity": 2, "price": 99.99},
    {"sku": "SKU789", "quantity": 1, "price": 59.99}
  ],
  "status": "PLACED"
}
```

---

## 🧹 Stop and Clean Up

```bash
docker-compose down
```

---

## 📡 Verify Kafka Topic (Optional)

Use Kafka CLI inside the container to view messages:

```bash
docker exec -it kafka kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic order-events \
  --from-beginning
```

---

## 🛠️ Customize

You can modify the `producer.py` to:
- Add more fields to the order
- Simulate failures, delays, or cancellations
- Change the Kafka topic name or frequency

---

## 🧾 Requirements

```txt
kafka-python==2.0.2
```

Install locally with:

```bash
pip install -r requirements.txt
```

---

## 📦 Future Improvements

- Add a Kafka Consumer for real-time analytics
- Store orders in a database (PostgreSQL, MongoDB)
- Expose REST APIs using FastAPI or Flask
- Add unit tests and logging

---

## 👨‍💻 Author

**Abhishek Tiwari**

---

## 📄 License

MIT License — feel free to use, fork, and contribute!
