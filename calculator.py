# Basic Calculator Program 

print("=== Simple Calculator ===")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operation from user
print("Enter operation:")
print("+ for addition")
print("- for subtraction") 
print("* for multiplication")
print("/ for division")

operation = input("Enter operation (+, -, *, /): ")

# Show what user chose
print("You entered:", num1, operation, num2)

# Calculate result 
result = num1 + num2
print("Result:", num1, "+", num2, "=", result)

print("Calculator finished!")
