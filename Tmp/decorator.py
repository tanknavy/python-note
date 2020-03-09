from datetime import datetime
import time

def decorator(func):
    def wrapper(*args,**kwargs):
        start = datetime.now().timestamp()
        func(*args,**kwargs)
        runtime = datetime.now().timestamp() - start
        print("the runtime is %d" % runtime)
    return wrapper

@decorator
def myfunc(a,b):
    time.sleep(1)
    return a+b

myfunc(1,9)