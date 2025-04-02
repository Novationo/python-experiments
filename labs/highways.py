interstate = int(input())

# if interstate == 0 or 00 or 50 or 60 or 200 or 300 or 400:
#     print(f"{interstate} is not a valid interstate highway number.")
# else:
invalid = [00, 100, 200, 300, 400, 500, 600, 700, 800, 900]
if interstate in invalid:
    print(f"{interstate} is not a valid intersate highway number.")
else:
    if interstate > 0 and interstate < 1000:
        maininter = interstate % 100
        if interstate > 100:
            news = ((interstate % 100) % 2)
            if news == 1:
                dirstring = "north/south"
            else:
                dirstring = "east/west"
            print(f"I-{interstate} is auxiliary, serving I-{maininter}, going {dirstring}.")
        else:
            news = interstate % 2 # north east west south
            if news == 1:
                print(f"I-{interstate} is primary, going north/south.")
            else:
                print(f"I-{interstate} is primary, going east/west.")
    else:
        print(f"{interstate} is not a valid interstate highway number.")