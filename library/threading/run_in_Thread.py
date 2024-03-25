import threading

class MyThread(threading.Thread):
    def run(self):
        print("My custom thread is running.")

# Create a new thread instance
my_thread = MyThread()

# Start the thread, which calls run() internally
my_thread.start()

# Wait for the thread to complete
my_thread.join()