# first import thread
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