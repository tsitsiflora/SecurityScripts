def log_on_exception(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if Exception == True:
            print("An Exception has been raised")

    return wrapper
      
@log_on_exception      
def say_okay():
  print("OKAY")

@log_on_exception
def greet(name):
  print(f"Hello {name}")

@log_on_exception
def divide_by_0():
  return 10//0

say_okay()
greet("Bob")
divide_by_0()