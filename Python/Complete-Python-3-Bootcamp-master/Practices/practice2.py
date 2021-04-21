#Two.py

import practice1

print("Top level in two.py")

practice1.func()

if __name__ == '__main__':
	print("Two.py isbeing run directly")
else:
	print("Two.py has been imprted")