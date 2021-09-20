# Documentation for "adder" function:
#
# models an n-bit ripple-carry adder in python
# takes positive integer n >=1, and two collections of bits of length >= n
# forms the n-bit sum of adding the lowest n bits of the two bit strings together,
# each interpreted as unsigned integers
# if the sum cannot be represented in n bits, it will overflow modulo 2^n
#
# returns a three-tuple of hexadecimal values:
# carryOut -- the carry out from the addition
# sumOut -- the n-bit sum modulo 2^n
# allCarries -- the value of every carry in the ripple carry adder, as
#    a set of bits, including the final carry out.
#
# example: for n=2, bitStringA=0x101 and bitString_B = 0xFF
#    the lowest two bits of each string would be 01 and 11
#    adding these together would produce 00 with a carry out of 1,
#    having formed carries of 11 in a ripple carry adder

def adder(n, bitString_A, bitString_B):
    a = f'{bitString_A:0>{int(2*n+1)}b}'  # converting hex to binary
    b = f'{bitString_B:0>{int(2*n+1)}b}'

    cOut = []
    sumO = []
    allC = []

    bit = 1
    cin = 0
    while bit <= n:
        sumO.append((int(a[-bit]) ^ int(b[-bit])) ^ cin)    # (A bit XOR B bit) XOR carryIn
        cOut.append(int(a[-bit]) & int(b[-bit]) | (cin & (int(a[-bit]) ^ int(b[-bit]))))    # (A bit AND B bit) OR (carryIn AND A bit) XOR B bit
        cin = int(a[-bit]) & int(b[-bit]) | (cin & (int(a[-bit]) ^ int(b[-bit]))) # Same as carryOut
        bit += 1

    cOut.reverse(), sumO.reverse(), allC.reverse()      # Sort bits by Most significant to least

    carryOut = hex(int(cOut[0]))    # Parse integer values into hexadecimal
    sumOut = hex(int(''.join([str(i) for i in sumO]), 2))
    allCarries = hex(int(''.join([str(i) for i in cOut]), 2))
    return (carryOut, sumOut, allCarries)
