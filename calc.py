def calculate (a , b):
    return int
a = int(input("Enter the first number: ")) 
operator = input("Enter an operator (+, -, *, /, **): ")
b = int(input("Enter the second number: "))

if operator == '+':
        result = a + b
elif operator == '-':
        result = a - b
elif operator == '*':
        result = a * b
elif operator == '/':
        if b != 0:
            result = a / b
        else:
            result = "Error: Division by zero"
elif operator == "**":
       result = a**b
else:
        result = "Error: Invalid operator"

print("The result is:", result) 
