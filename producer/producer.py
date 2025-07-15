from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_order_event():
    return {
        "order_id": f"ORD{random.randint(100000, 999999)}",
        "user_id": f"user_{random.randint(1000, 9999)}",
        "order_amount": round(random.uniform(100.0, 2000.0), 2),
        "currency": "INR",
        "order_status": random.choice(["confirmed", "shipped", "delivered"]),
        "order_time": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    while True:
        event = generate_order_event()
        producer.send('order-events', value=event)
        print(f"Produced: {event}")
        time.sleep(5)
