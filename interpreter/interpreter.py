input_string = input("maths\n").strip()

# finds the operator used
operation = ''
if input_string.find('+') != -1:
    operation = '+'
elif input_string.find('-') != -1:
    operation = '-'
elif input_string.find('*') != -1:
    operation = '*'
elif input_string.find('/') != -1:
    operation = '/'

# splits the equasion into its componant numbers
numbers = input_string.split(operation)

# does the operation to the numbers
if operation == '+':
    print(float(int(numbers[0]) + int(numbers[1])))
elif operation == '-':
    print(float(int(numbers[0]) - int(numbers[1])))
elif operation == '*':
    print(float(int(numbers[0]) * int(numbers[1])))
elif operation == '/':
    print(float(int(numbers[0]) / int(numbers[1])))