input_string = input("maths\n") + '\0'
a = 0
operation = ''
b = 0

i = 0
while input_string[i] != ' ':
    a = a * 10 + int(input_string[i])
    i += 1
i += 1
operation = input_string[i]
i += 2
while input_string[i] != '\0':
    b = b * 10 + int(input_string[i])
    i += 1


if operation == '+':
    print(float(a + b))
if operation == '-':
    print(float(a - b))
if operation == '*':
    print(float(a * b))
if operation == '/':
    print(float(a / b))