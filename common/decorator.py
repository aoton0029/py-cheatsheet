import time

def timer_decorator(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"{func.__name__} ran in {end - start} seconds")
		return result
	return wrapper


def logging_decorator(func):
	def wrapper(*args, **kwargs):
		print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
		result = func(*args, **kwargs)
		print(f"{func.__name__} returned {result}")
		return result
	return wrapper


def check_arguments(*argtypes):
	def decorator(func):
		def wrapper(*args):
			if len(args) != len(argtypes):
				raise TypeError("Argument count does not match")
			for arg, argtype in zip(args, argtypes):
				if not isinstance(arg, argtype):
					raise TypeError(f"Argument {arg} is not of type {argtype}")
			return func(*args)
		return wrapper
	return decorator

