in_f = open("componet.def", "r")
out_f = open("gate.def", "w")


def split_line_gate(file_in, file_out):
    for line in file_in:
        if not line.startswith(' ;'):
            spl_word = "gate"
            test = line.split()
            some_var = f'{test[1]} {test[2]} ({test[6]},{test[7]})\n'
            print(some_var)
            file_out.write(some_var)


split_line_gate(in_f, out_f)
