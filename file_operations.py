# file operations
def main():
#    #f = open("text.txt", "w+")
#if i want to append the data that already existing file
#    f = open("text.txt", "a")
#    for i in range(10):
#        f.write("this is line" + str(i) +"\r\n")
#    f.close()

# read the content with out opening the file
    f = open("text.txt", "r")
    if f.mode == 'r':
    #    a = f.read()
    #    print(a)
## reading the contents in another way
        a = f.readlines()
    for i in a:
        print(i)
if __name__ == "__main__":
    main()