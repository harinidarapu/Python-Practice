# Opening and reading the file
def main():
    file_in = open("c17_synth.def")
    file_out = open("componet.def", "w")
    copy = False
    for line in file_in:
        if line.strip() == "COMPONENTS 6 ;":
            copy = True
            continue
        elif line.strip() == "END COMPONENTS":
            copy = False
            continue
        elif copy:
            file_out.write(line)
            #print(copy)


if __name__ == "__main__":
    main()

#
#with open('c17_synth.def') as infile, open('componet.def', 'w') as outfile:
#    copy = False
#    for line in infile:
#        if line.strip() == "COMPONENTS 6 ;":
#            copy = True
#            continue
#        elif line.strip() == "END COMPONENTS":
#            copy = False
#            continue
#        elif copy:
#            outfile.write(line)