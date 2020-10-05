import primitives_4p1
import sys
import time

global  = dict()
for i in range(0xffff):
  temp[i]=primitives_4p1.count_parity(i)

cases = {
  0x43: 0x01,
  0x0A: 0x00,
  0x0B: 0x01,
  0xFF: 0x00,
  0xFC: 0x00,
}

t = time.time()
for key, value in cases.items():
  if(primitives_4p1.count_parity(key) != value):
    print("uh oh",key, value)
print(time.time()-t)

t = time.time()
for key, value in cases.items():
  if(primitives_4p1.count_lookupParity(key) != value):
    print("shit",key, value)
print(time.time()-t)
