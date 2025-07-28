# Threading in Python
The threading module provides a way to run multiple threads (smaller units of a process) concurrently within a single process. It allows for the creation and management of threads, making it possible to execute tasks in parallel, sharing memory space. Threads are particularly useful when tasks are I/O bound, such as file operations or making network requests, where much of the time is spent waiting for external resources.

## Procedure
- Add them on thread using **threading.Thread**
- Start each of the thread using **start**
- Join them using **join**