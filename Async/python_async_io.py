# Import necessary libraries
import asyncio
import time
import threading
import multiprocessing

# 1. Simple coroutine that uses asyncio
async def simple_coroutine():
    print("Start of coroutine")
    await asyncio.sleep(1)
    print("End of coroutine")

# Running simple coroutine
asyncio.run(simple_coroutine())

# 2. Simulating I/O-bound tasks using asyncio
async def download_file(file_name):
    print(f"Starting to download {file_name}")
    await asyncio.sleep(2)  # Simulate I/O-bound task
    print(f"Finished downloading {file_name}")

async def main_io():
    # Simulate downloading multiple files concurrently
    await asyncio.gather(
        download_file("file1.txt"),
        download_file("file2.txt"),
        download_file("file3.txt"),
    )

# Running multiple I/O-bound tasks concurrently
asyncio.run(main_io())

# 3. Asyncio vs Threading: Running tasks in parallel using threads
def thread_task(name):
    print(f"Thread {name} starting")
    time.sleep(2)  # Simulate time-consuming task
    print(f"Thread {name} finished")

# Using threads to run parallel tasks
threads = []
for i in range(3):
    thread = threading.Thread(target=thread_task, args=(i,))
    threads.append(thread)
    thread.start()

# Join threads back to the main thread
for thread in threads:
    thread.join()

# 4. Asyncio vs Multiprocessing: Running tasks in parallel using processes
def process_task(name):
    print(f"Process {name} starting")
    time.sleep(2)  # Simulate time-consuming task
    print(f"Process {name} finished")

# Using processes to run parallel tasks
processes = []
for i in range(3):
    process = multiprocessing.Process(target=process_task, args=(i,))
    processes.append(process)
    process.start()

# Join processes back to the main process
for process in processes:
    process.join()

# 5. Running concurrent tasks with asyncio - Real-world use case: Web scraping simulation
async def fetch_website(url):
    print(f"Fetching {url}...")
    await asyncio.sleep(1)  # Simulate fetching data from a website
    print(f"Finished fetching {url}")

async def scrape_websites():
    await asyncio.gather(
        fetch_website("https://example1.com"),
        fetch_website("https://example2.com"),
        fetch_website("https://example3.com"),
    )

# Running a web scraping simulation concurrently
asyncio.run(scrape_websites())

# 6. Demonstrating cancelling asyncio tasks
async def long_running_task():
    try:
        print("Long running task starting")
        for i in range(5):
            await asyncio.sleep(1)
            print(f"Task progress: {i + 1}/5")
    except asyncio.CancelledError:
        print("Long running task was cancelled!")

async def cancel_task_example():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(2)  # Let the task run for 2 seconds
    print("Cancelling the task...")
    task.cancel()  # Cancelling the task

# Running the task cancellation example
asyncio.run(cancel_task_example())

# 7. Demonstrating asyncio’s performance benefit over threading with a simple test
async def async_task():
    print("Async task starting")
    await asyncio.sleep(1)  # Simulate an I/O task
    print("Async task finished")

def thread_task_test():
    print("Thread task starting")
    time.sleep(1)  # Simulate a blocking task
    print("Thread task finished")

# Running asyncio vs threads for 5 tasks
start_time = time.time()
asyncio.run(asyncio.gather(*(async_task() for _ in range(5))))  # 5 Asyncio tasks
asyncio_time = time.time() - start_time

start_time = time.time()
threads = [threading.Thread(target=thread_task_test) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
thread_time = time.time() - start_time

# Comparing the time taken by asyncio vs threads
print(f"Asyncio time: {asyncio_time:.2f} seconds")
print(f"Threading time: {thread_time:.2f} seconds")

# Conclusion: asyncio is faster for I/O-bound tasks compared to threading, period.
