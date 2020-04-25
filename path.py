import os
from os import path
import datetime
from datetime import date, time, timedelta
import  time
def main():
    print(os.name)
    print("is the path exits  " + str(path.exists("text.txt")))
    print("is the file is directory" + str(path.isdir("text.txt")))
    print("the realpath of item is " + str(path.realpath("text.txt")))
    print("the real path and item is " + str(path.split(path.realpath("text.txt"))))

# if modification is done to a file , if yes, at what time?

    t = time.ctime(path.getmtime("text.txt"))
    print(t)
if __name__ == '__main__':
    main()
