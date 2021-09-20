from rippleAdder import adder

def checker(output,expected):
    print("got",output, "; expected", expected, "; Equivalent?", output==expected)


def main():
    out1 = adder(1,1,1)
    out2 = adder(2,4,3)
    out3 = adder(9,0xFEEDEEC5,0xBADF00D)
    expected1 = (hex(1),hex(0),hex(1))
    expected2 = (hex(0),hex(3),hex(0))
    expected3 = (hex(0),hex(0xD2),hex(0xD))
    checker(out1, expected1)
    checker(out2, expected2)
    checker(out3, expected3)

if __name__ == "__main__":
    main()
