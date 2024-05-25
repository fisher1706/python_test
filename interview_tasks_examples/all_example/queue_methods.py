from queue import Queue

# Initializing a queue
q = Queue(maxsize=3)


if __name__ == "__main__":
    # qsize() give the maxsize of the Queue
    print(f"size = {q.qsize()}")

    # Adding of element to queue
    q.put("a")
    print(f"queue = {q}")

    # Return Boolean for Full Queue
    print(f"full = {q.full()}")

    # Removing element from queue
    print(f"get = {q.get()}")

    # Return Boolean for Empty Queue
    print(f"empty = {q.empty()}")
