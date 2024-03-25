# Threading in Python
Threading in Python allows for concurrent execution of code. This can be especially useful in **I/O-bound** or network-bound applications where the program spends a lot of time waiting for external events. Python's **threading** module provides a way to create and manage threads, allowing multiple threads to run concurrently in a single process.

### Key Concepts:

- **Thread**: A thread is a separate flow of execution. Each thread has its own stack but shares the global memory space with other threads.
- **Threading Module**: Python’s standard library provides the `threading` module which allows for the creation and management of threads.
- **Thread Creation**: Threads can be created by instantiating the `Thread` class from the `threading` module with a target function to be executed by the thread.
- **Starting a Thread**: After creating a thread, it must be started by calling its `start()` method.
- **Joining a Thread**: The `join()` method of a thread ensures that the program waits for threads to complete their tasks before moving on.
- **Daemon Threads**: These are background threads that are automatically killed when the main program exits. They are set by marking a thread as a daemon thread before starting it.
- **Thread Safety**: When multiple threads access a shared resource, it can lead to race conditions. Thread safety can be achieved through synchronization mechanisms such as locks.

### Example:

Here is a simple example demonstrating how to create and start a thread:

```python
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
```

This program creates and starts a thread that prints numbers 0 to 4, each followed by a 1-second delay.

### GIL (Global Interpreter Lock):

It's important to note that Python has a Global Interpreter Lock (GIL) which is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This means that in CPU-bound programs, threading may not provide the expected performance improvement due to the serialization of bytecode execution. For CPU-bound tasks, using the `multiprocessing` module to achieve parallelism might be more effective.

### Conclusion:

Threading is a powerful feature in Python for I/O-bound and network-bound applications. It allows for the concurrent execution of code, making efficient use of waiting time. However, due to the GIL, threading in Python may not be the best choice for CPU-bound tasks.
Learn more [here](https://docs.python.org/3/library/threading.html#threading.Thread)

Example : **run_thread.py**
