x = float(input("first number"))
y = float(input("second number"))
operation = input("operation")

result = None

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
elif operation == "/":
    if y is not y == 0:
        result = x / y
    else:
        print('do not divide on zero')
else:
    print("unsupported operation")

if result is not None:
    print(result)
