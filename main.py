import primitives_4p1
import primitives_4p3, primitives_4p11
import sys
import time
# from dataclass import dataclass

####primitives_4p1.py related codes
# global  = dict()
# for i in range(0xffff):
#   temp[i]=primitives_4p1.count_parity(i)

# cases = {
#   0x43: 0x01,
#   0x0A: 0x00,
#   0x0B: 0x01,
#   0xFF: 0x00,
#   0xFC: 0x00,
# }

# t = time.time()
# for key, value in cases.items():
#   if(primitives_4p1.count_parity(key) != value):
#     print("uh oh",key, value)
# print(time.time()-t)

# t = time.time()
# for key, value in cases.items():
#   if(primitives_4p1.count_lookupParity(key) != value):
#     print("shit",key, value)
# print(time.time()-t)

####primitives_4p3.py related code
#value = 4
#lookUpTable = dict()
#numbits = 2**value
#for i in range(1 << numbits):
#  lookUpTable[i] = primitives_4p3.reverse_bits_naive(i, numbits)
#
#
#
#val = 21
#result = primitives_4p3.reverse_bits_naive(val, 5)
#print(f'the result of your operation for {bin(val)}: {result}: {bin(result)}')

###primtivies_4p11.py relating
rect1 = primitives_4p11.Rectangle(3,3,4,1)
rect2 = primitives_4p11.Rectangle(1,1,2,2)
primitives_4p11.intersectionFinder(rect1, rect2)