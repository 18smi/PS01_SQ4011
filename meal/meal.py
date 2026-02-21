def main():
    time_f = convert(input("time\n"))

    if time_f >= 7 and time_f <= 8:
        print("breakfast time")
    if time_f >= 12 and time_f  <= 13:
        print("lunch time")
    if time_f >= 18 and time_f <= 19:
        print("dinner time")
    


def convert(time):
    # the position of the ':' indicates wether its xx:xx or x:xx
    if time[1] == ':':
        return int(time[0]) + int(time[2])/6 + int(time[3])/60
    return int(time[0])*10 + int(time[1]) + int(time[3])/6 + int(time[4])/60



if __name__ == "__main__":
    main()