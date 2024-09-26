import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk


def waiting(timeout):
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print("Ok")


def thread_wait(timeout):
    thread = Thread(target=waiting, args=(timeout,), daemon=True)
    thread.start()
    return thread


counter = [0]
lock = threading.Lock()


if __name__ == "__main__":
    tk = Tk()
    button_1 = ttk.Button(tk, text="WAIT", command=lambda: waiting(3))
    button_1.pack(side=LEFT)
    button_2 = ttk.Button(tk, text="THREAD", command=lambda: thread_wait(3))
    button_2.pack(side=LEFT)
    tk.mainloop()
