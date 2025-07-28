import threading
import time


def delay_process(link, delay_time=10):
    print(f"Starting the process {link}")
    time.sleep(delay_time)
    print(f"Process completed {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

threads = []
for link in links:
    t = threading.Thread(target=delay_process, args=(link,), kwargs={"delay_time":5})
    threads.append(t)
threads2 = []
for link in links:
    t = threading.Thread(target=delay_process, args=(link,), kwargs={"delay_time":5})
    threads2.append(t)
print(threading.active_count()) # Return the active threads
for t in threads:
    t.start()

for t in threads:
    t.join()
print(delay_process("First Link", 20))
print(delay_process("Second Link", 10))