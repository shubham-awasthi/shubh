#one.py

def func():
	print("Func() In One.py")

print("Top level in one.py")

if __name__ == '__main__':
	print("one.py is run directly")
else:
	print("One.py has been inported")