# This is our PUB/SUB project using Dapr

# Two python files - "Sub" acts as the backend subscriber server that recieves and "storeservice" acts as the publisher that sends hardcoded json inputs to "Sub"

# Components folder includes our YAML config and pubsub file

# Python Interpreter: Conda Python

# Environment Prerequisites: Dapr, Flask, Conda

# Make sure Dapr is initialized in the environment using "dapr init"

# To run Dapr backend: docker run -d --name redis -p 6379:6379 redis

# Run Sub.py - dapr run --app-id sub --components-path ./components -- python Sub.py

# Run storeservice.py - dapr run --app-id storeservice --app-port 5000 -- python storeservice.py
