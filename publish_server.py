import zmq
import time

# Create a ZeroMQ context
context = zmq.Context()
socket = context.socket(zmq.PUB)  # Create a publisher socket

# Bind to TCP port
socket.bind("tcp://*:5555")  # Listen on all available IPs on port 5555

selected_topics = []
topic = ""
messages = []

topics = ["general", "cs131", "fun"]  # Predefined topics
while topic != 'done':
    topic = input('Enter the topic (#general, #cs131, #fun): ')
    
    if topic!= 'done' and topic in topics:
        selected_topics.append(topic)
        messages.append(input("Enter your message: "))
    else:
        print('Invalid topic')





print("Publisher started...")

try:
    while True:
        for i, topic in enumerate(selected_topics):
           # message = f"{topic} Hello from publisher at {time.time()}"
            socket.send_string(f"{selected_topics[i]} {messages[i]}")  # Send topic and message
            print(f"Sent: {messages[i]}")





            time.sleep(2)  # Send a message every 2 seconds

except KeyboardInterrupt:
    print("\nPublisher stopped.")
    socket.close()


context.term()

