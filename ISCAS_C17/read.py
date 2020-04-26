def main():
 f = open("c17_synth.def", "r")
 if f.mode == 'r':
     a = f.read()
     print(a)
if __name__ == "__main__":
    main()