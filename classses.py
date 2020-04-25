# classes and inherited classes
# defining base class
class base_clas():
    def method1(self):
        print("this is base class")
    def method2(self, somestring):
        print("base class" + somestring)

class child_class():
    def method1(self):
        base_clas.method1(self)
        print("this is child class")
    def method2(self):
        print("this is child method 2")

def main():
    c1 = base_clas()
    c1.method1()
    c1.method2("  arguement")

    c2= child_class()
    c2.method1()
    c2.method2()


if __name__ == "__main__":
    main()