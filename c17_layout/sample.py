from os import path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def main():

    # Opening and reading the file
    file_in = open(r"C:\Harini\Verification\python\Design_Files\SEMT_SMT_Benchmarks/c17/c17_synth.def")
    file_out = open(r"C:\Harini\Verification\python\layout/c17_layout/component.def", "r+")

    # Copying the lines present between "COMPONENTS and ENDCOMPONENTS"
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

    # now Taking Two lists to store x-coordinates and y-coordinates

    file_out.seek(0, 0)   # cursor again starts first
    my_list_x = []
    my_list_y = []
    for line in file_out:
        if not line.startswith(' ;'):
            #spl_word = "gate"   # grabbing lines with "gate"
            test = line.split()
            my_list_x.append(test[6])      # x-coordinate
            my_list_y.append(test[7])      # y-coordinate
    #  converting list of strings to integers
    for i in range(0, len(my_list_x)):
        my_list_x[i] = (int(my_list_x[i])/2000) # 2000 is unit micro distance
    for i in range(0, len(my_list_y)):
        my_list_y[i] = (int(my_list_y[i])/2000)
    x = my_list_x
    y = my_list_y

    # scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y, color='red', s=10)

    # add rectangles
    width = 0.76
    height = 2.47
    for i in range(len(x)):
        ax.add_patch(
            Rectangle(xy=(x[i],y[i]), width=width, height=height, linewidth=1, color='blue',
                      fill=False,hatch='///'))
    plt.show()


if __name__ == "__main__":
    main()