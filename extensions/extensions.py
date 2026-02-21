input_string = input("input please\n").lower()
start_index = input_string.find('.')


if start_index == -1:
    print("application/octet-stream")
else:
    if input_string[start_index:] == ".jpg" or input_string[start_index:] == ".jpeg":
        print("image/jpeg")
    elif input_string[start_index:] == ".png":
        print("image/png")
    elif input_string[start_index:] == ".gif":
        print("image/gif")
    elif input_string[start_index:] == ".zip":
        print("application/zip")
    elif input_string[start_index:] == ".pdf":
        print("application/pdf")
    elif input_string[start_index:] == ".txt":
        print("text/plain")