import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)  # Create a subscriber socket

# Connect to the publisher
publisher_ip = "10.13.40.93"  # Replace with your Jetson Nano's IP address
socket.connect(f"tcp://{publisher_ip}:5555")

# Choose topics to subscribe to (can subscribe to multiple topics)
topics = ["general", "cs131", "fun"]

# prompt user to enter topics
topic = ""
selected_topics = []
while topic != "done":
    topic = input("Enter topic to subscribe (general, cs131, fun) to or done to quit: ")
    if topic != "done" and topic in topics:
        selected_topics.append(topic)
    elif topic not in topics:
        print("Invalid topic")

for topic in selected_topics:
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)  # Subscribe to a topic

print(f"Subscriber started, listening to {selected_topics}...")

try:
    while True:
        message = socket.recv_string()  # Receive message
        print(f"Received: {message}")
except KeyboardInterrupt:
    print("\nSubscriber stopped.")
    socket.close()
    context.term()

