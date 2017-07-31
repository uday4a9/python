import concurrent.futures
import time

MAX_WORKERS = 5

def delay(arg):
    time.sleep(arg)
    return "Done"

def thread_futures():
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)

    futures = [pool.submit(delay, 2) for _ in range(MAX_WORKERS)]

    for ind, future in enumerate(concurrent.futures.as_completed(futures)):
        result = future.result()
        print(ind, result)

def thread_futures_with_context_manager():
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = [pool.submit(delay, 2) for _ in range(MAX_WORKERS)]

    for ind, future in enumerate(concurrent.futures.as_completed(futures)):
        result = future.result()
        print(ind, result)


if __name__ == '__main__':
    thread_futures()
    print("*" * 12)
    thread_futures_with_context_manager()
