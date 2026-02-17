from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
      print("before excecution")
      func()
      print("after excecution")
    return wrapper



@my_decorator
def greet():
    print("from inside greet")

greet()
print(greet.__name__)