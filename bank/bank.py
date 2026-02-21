input_string = input("greeting please\n").lower().replace(' ', '')[:5]
# removes all spaces, makes the string lowercase and saves the first 5 letters to input_string

if input_string == "hello":
    print("$0")
elif input_string[0] == 'h':
    print("$20")
else:
    print("$100")