# script.py

from time import sleep
import sys
def yielder(li):
    for i in li:
        yield i

def streaming_avg(yielder):
    average = 0
    n = 0
    for newval in yielder:
        if n==0:
            n += 1
            average = newval
        else:
            n += 1
            average = average*(1-1/n) + newval/n
        print("Seen {}\tCurrent average is {}".format(newval, average))
        sleep(.5)

if __name__=="__main__":
    userlist = [int(i) for i in sys.argv[1:]]
    streaming_avg(yielder(userlist))

