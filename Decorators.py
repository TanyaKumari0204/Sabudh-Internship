import time

# 1. Define uppercase_decorator
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# 2. Define say_hello function
def say_hello(name):
    return f"Hello, {name}!"

# 3. Apply uppercase_decorator to say_hello
greet = uppercase_decorator(say_hello)

# 4. Test greet function
print("Test greet function:")
print(greet("Alice"))  # Output: HELLO, ALICE!

# 5. Define timing_decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# 6. Apply timing_decorator to greet
timed_greet = timing_decorator(greet)

# 7. Test timed_greet function
print("\nTest timed_greet function:")
print(timed_greet("Bob"))  # Output includes timing and greeting

# 8. Define Math class with add and subtract methods
class Math:
    # 9. Define logging_decorator
    def logging_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with arguments: {args}")
            result = func(*args, **kwargs)
            print(f"Result: {result}")
            return result
        return wrapper

    @logging_decorator
    def add(self, a, b):
        return a + b

    @logging_decorator
    def subtract(self, a, b):
        return a - b

# 10. Test Math class methods
print("\nTest Math class methods:")
math_instance = Math()
math_instance.add(10, 5)       # Logs: Calling add with arguments: (10, 5)
math_instance.subtract(10, 3)  # Logs: Calling subtract with arguments: (10, 3)
