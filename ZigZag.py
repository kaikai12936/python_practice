'''
P   A   H   N
A P L S I I G
Y   I   R

PAHNAPLSIIGYIR
'''
s = "PAYPALISHIRING"
numRows = 3

L = [''] * numRows
index, step = 0, 1

for x in s:
    L[index] += x
    if index == 0:
        step = 1
    elif index == numRows -1:
        step = -1
    index += step

print( ''.join(L))