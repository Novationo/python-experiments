
string = str(input())
stop = 1

while stop != 0:
    if string == "done" or string == "Done" or string == "d":
        stop = 0
        break
    else:
        string = list(string)
        string.reverse()
        print(("".join(string)))
        string = str(input())
        break

