input_string = input("input please\n")
media_type_string = ""
media_type_found = False

for i in input_string:
    if i == '.':
        media_type_found = True
    if media_type_found:
        media_type_string += i.lower()

if media_type_found == False:
    print("application/octet-stream")
else:
    print(media_type_string)