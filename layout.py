from os import path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def main():

    # Opening and reading the file
    file_in = open(r"C:\Harini\Verification\python\Design_Files\SEMT_SMT_Benchmarks/c432/c432_synth.def")
    file_out = open(r"C:\Harini\Verification\python\layout/c432_layout/componet.def", "r+")

    # Copying the lines present between "COMPONENTS and ENDCOMPONENTS"
    copy = False
    for line in file_in:
        if line.strip() == "COMPONENTS 215 ;":
            copy = True
            continue
        elif line.strip() == "END COMPONENTS":
            copy = False
            continue
        elif copy:
            file_out.write(line)

    # now Taking lists to store x-coordinates and y-coordinates

    file_out.seek(0, 0)   # cursor again starts first
    # Declaration of lists
    INV_X = []
    INV_Y = []
    NAND_X = []
    NAND_Y = []
    NOR_X = []
    NOR_Y = []
    AND_X = []
    AND_Y = []
    XOR_X = []
    XOR_Y = []
    x1 = []
    yi = []

    for line in file_out:
        if not line.startswith(' ;'):
            test = line.split()
            if test[2] == "INVX1":
                INV_X.append(test[6])
                INV_Y.append(test[7])
            if test[2] == "NAND2X1":
                NAND_X.append(test[6])
                NAND_Y.append(test[7])
            if test[2] == "NOR2X1":
                NOR_X.append(test[6])
                NOR_Y.append(test[7])
            if test[2] == "AND2X1":
                AND_X.append(test[6])
                AND_Y.append(test[7])
            if test[2] == "XOR2X1":
                XOR_X.append(test[6])
                XOR_Y.append(test[7])
    #Converting list of stings to integer
    for i in range(0, len(INV_X)):
            INV_X[i] = (int(INV_X[i]) / 2000)  # 2000 is unit micro distance
    for i in range(0, len(INV_Y)):
            INV_Y[i] = (int(INV_Y[i]) / 2000)

    for i in range(0, len(NAND_X)):
            NAND_X[i] = (int(NAND_X[i]) / 2000)  # 2000 is unit micro distance
    for i in range(0, len(NAND_Y)):
            NAND_Y[i] = (int(NAND_Y[i]) / 2000)

    for i in range(0, len(NOR_X)):
            NOR_X[i] = (int(NOR_X[i]) / 2000)  # 2000 is unit micro distance
    for i in range(0, len(NOR_Y)):
            NOR_Y[i] = (int(NOR_Y[i]) / 2000)

    for i in range(0, len(AND_X)):
            AND_X[i] = (int(AND_X[i]) / 2000)  # 2000 is unit micro distance
    for i in range(0, len(AND_Y)):
            AND_Y[i] = (int(AND_Y[i]) / 2000)

    for i in range(0, len(XOR_X)):
            XOR_X[i] = (int(XOR_X[i]) / 2000)  # 2000 is unit micro distance
    for i in range(0, len(XOR_Y)):
            XOR_Y[i] = (int(XOR_Y[i]) / 2000)

    # to plot scaterplot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(INV_X, INV_Y, color='red', s=0)
    ax.scatter(NAND_X, NAND_Y, color='blue', s=0)
    ax.scatter(AND_X, AND_Y, color='green', s=0)
    ax.scatter(XOR_X, XOR_Y, color='yellow', s=0)
    ax.scatter(NOR_X, NOR_Y, color='pink', s=0)


    # draw rectangles
    # inverter :  SIZE 0.57 BY 2.47 ;
    for i in range(len(INV_X)):
        ax.add_patch(Rectangle(xy=(INV_X[i], INV_Y[i]), width=0.57, height=2.47, linewidth=1, color='red',
                      fill=False, hatch='---'))
    # NAND : SIZE 0.76 BY 2.47 ;
    for i in range(len(NAND_X)):
        ax.add_patch(Rectangle(xy=(NAND_X[i], NAND_Y[i]), width=0.76, height=2.47, linewidth=1, color='blue',
                      fill=False, hatch='/'))
    # AND :  SIZE 1.14 BY 2.47 ;
    for i in range(len(AND_X)):
        ax.add_patch(Rectangle(xy=(AND_X[i], AND_Y[i]), width=1.14, height=2.47, linewidth=1, color='green',
                      fill=False, hatch='////'))
    # XOR_X : SIZE 1.71 BY 2.47 ;
    for i in range(len(XOR_X)):
        ax.add_patch(Rectangle(xy=(XOR_X[i], XOR_Y[i]), width=1.71, height=2.47, linewidth=1, color='black',
                      fill=False, hatch='/'))
    # NOR :  SIZE 0.76 BY 2.47 ;
    for i in range(len(NOR_X)):
        ax.add_patch(Rectangle(xy=(NOR_X[i], NOR_Y[i]), width=0.76, height=2.47, linewidth=1, color='violet',
                      fill=False, hatch='||||'))


    plt.title('layout of C432')
    plt.show()

if __name__ == "__main__":
    main()