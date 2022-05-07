# first import thread
from concurrent.futures import thread
import threading

# create a function for the thread to target
def hi():
    print("Hi")

# create a thread obj
    #target: controls a specified function
t1 = threading.Thread(target=hi)

# must use the start() function on thread obj to run code in function
    # YOU DO NOT make a function call on itself 
t1.start()

# without comments

def zipcode():
    print("12345")

t2 = threading.Thread(target=zipcode)
t2.start()


