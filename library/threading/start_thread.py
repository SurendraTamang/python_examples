import threading
import time

# Define a function for the thread
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread has completed its execution.")