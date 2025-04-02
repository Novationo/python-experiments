
import time

t = int(input())

while t:
    mins, secs = divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mins,secs)

    # not finihed obv