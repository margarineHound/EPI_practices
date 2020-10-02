def count_bits(x):
  # print(x)
  num_bits=0
  while(x):
    num_bits += x & 1
    x >>=1

  return(num_bits)

def count_parity(x):
  print('number received: ' + str(x))
  num_bits = count_bits(x)
  if(num_bits % 2) == 1:
    print('parityBit = 1')
    return(1)
  else:
    print("parityBit is 0")
    return(0)


def count_lookupParity(x):
  BIT_MASK = 0xF
  MASK_SIZE = 4
   
  COMPUTEDPARITY={ \
    0b0000: 0, \
    0b0001: 1, \
    0b0010: 1, \
    0b0011: 0, \
    0b0100: 1, \
    0b0101: 0, \
    0b0110: 0, \
    0b0111: 1, \
    0b1000: 1, \
    0b1001: 0, \
    0b1010: 0, \
    0b1011: 1, \
    0b1100: 0, \
    0b1101: 1, \
    0b1110: 1, \
    0b1111: 0, \
  }

  result0 = COMPUTEDPARITY[x & BIT_MASK]
  result1 = COMPUTEDPARITY[(x >> MASK_SIZE) & BIT_MASK]
  result2 = COMPUTEDPARITY[(x >> MASK_SIZE*2) & BIT_MASK]
  result3 = COMPUTEDPARITY[(x >> MASK_SIZE*3) & BIT_MASK]

  result = result0 ^ result1^result2^result3
  return(result)
  

if __name__ == "__main__":
  count_bits()