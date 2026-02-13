input_string = input("input please\n")
output_string = ""
for i in input_string:
    if i.isupper:
        output_string += i.lower()
    else:
        output_string += i


if output_string == "42" or output_string == "forty-two" or output_string == "forty two":
    print("yes")
else:
    print("no")
