import json
from dapr.clients import DaprClient

# Hardcoded order details
order = {
    'item_name': 'Laptop',
    'item_price': 899.99
}

print("Welcome to StoreService! Publishing a hardcoded order...")

with DaprClient() as client:
    client.publish_event(
        pubsub_name='pubsub',
        topic_name='orders',
        data=json.dumps(order),  # convert to JSON string
    )
    print(f"Published order: {order}")

print("Service completed. Thank you for using StoreService!")