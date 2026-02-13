input_string = input("greeting please\n")
reward = 100
is_hello = 5

for i in input_string:
    if i == ' ':
        continue
    elif ((i == 'h' or i == 'H') and reward == 100) or ((i == 'e' or i == 'e') and is_hello == 4) or ((i == 'l' or i == 'l') and is_hello == 3) or ((i == 'l' or i == 'l') and is_hello == 2):
        reward = 20
        is_hello -= 1
    elif (i == 'o' or i == 'o') and is_hello == 1:
        reward = 0
    else:
        break

print(reward)