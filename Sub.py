from flask import Flask, request

app = Flask(__name__)

# Inform Dapr about the pub/sub subscription
@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    return [{
        "pubsubname": "pubsub",  # Matches the pubsub component name
        "topic": "orders",       # Matches the topic published by storeservice
        "route": "orders"        # Route to process messages
    }]

# Handle messages from the 'orders' topic
@app.route('/orders', methods=['POST'])
def orders():
    data = request.json  # Retrieve the order data
    print(f"Order data received: {data}", flush=True)  # Log the received order
    return '', 200  # Acknowledge successful processing

# Run the Flask app
app.run(port=5000)  # Run the Flask app on port 5000