# first import thread
import threading

# create a function for the thread to target
def hi():
    print("Hi")

t1 = threading.Thread(target=hi)

t1.start()