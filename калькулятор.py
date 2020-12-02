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
    result = x/y
else:
    print("unsupported operation")
    if result is not None:
        print("result:",result)
