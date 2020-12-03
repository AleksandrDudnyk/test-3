x = float(input("first namber"))
y = float(input("second namber"))
operation = input("operation")

result = None

if  operation == "+":
    result = x+y    
elif operation == "-":
    result = x-y
elif operation == "*":
    result = x*y
elif operation == "/":
    if y is not y == 0:
        result = x/y
    else:
        print('do not divide on zero')
else:
    print("unsupported operation")

if result is not None:
    print(result)
