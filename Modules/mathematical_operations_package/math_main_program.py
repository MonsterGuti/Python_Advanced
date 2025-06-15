from Modules.mathematical_operations_package.math_operations_module import operations_mapper

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator: ")

print(f'{operations_mapper[operator](num1, num2):.2f}')