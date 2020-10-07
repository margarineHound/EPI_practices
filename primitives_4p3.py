def reverse_bits_naive(n, m):
    mask = (2 ** m) - 1
    for i in range(m//2):

        mask1 = mask ^ (1<< i)
        mask2 = mask ^ (1 << ((m-1)-i))

        # lowBit = (n & (n << i)) >> i
        # highBit = (n & (1 << ((m-1) -i ))) >> (m-1-i)

        lowBit = (n & (1 << i)) != 0
        highBit = (n & (1 << ((m-1)-i))) !=0

        n &= mask1 & mask2

        n += (lowBit << ((m-1)-i))
        n += highBit << i

    return n




def reverse_bits_lookUp(n, lookupTable):

    BITMASK = (2**4) -1
    MASKSIZE = 4
    BITMASK_ZERO = (2**64) -1
    SIZE = 64 // MASKSIZE

    for i in range(SIZE//2):
        tempLow = (n & (BITMASK << MASKSIZE * i))
        print(f'Op1: n: {bin(n)}, tempLow: {bin(tempLow)}')
        n -= tempLow
        print(f'Op2: n: {bin(n)},tempLow: {bin(tempLow)}')
        tempLow = tempLow >> (MASKSIZE * i)
        print(f'Op3: n: {bin(n)}, tempLow: {bin(tempLow)}')
        tempHigh = n & (BITMASK << (MASKSIZE * ((SIZE//2 -1)-i) ))

        print(f'Op4: n: {bin(n)}, tempLow: {bin(tempLow)}, NEW tempHigh: {bin(tempHigh)}')
        n -= tempHigh
        print(f'Op5: {bin(n)}, {bin(tempLow)}, {bin(tempHigh)}')
        tempHigh = tempHigh >> (MASKSIZE * ((SIZE//2 - 1) -i))
        print(f'Op6: {bin(n)}, {bin(tempLow)}, {bin(tempHigh)}')

        flippedLow = lookupTable[tempLow]
        print(f'Op7: flippedLow {bin(flippedLow)}')
        flippedHigh = lookupTable[tempHigh]
        print(f'Op8: flippedHigh: {bin(flippedHigh)}')

        toSwitchHigh = flippedLow << (MASKSIZE * ((SIZE//2 - 1) -i))
        print(f'Op9: toSwitchHigh: {bin(toSwitchHigh)}')
        toSwitchLow = flippedHigh << (MASKSIZE * i)
        print(f'Op10: toSwitchLow: {bin(toSwitchLow)}')

        print(f'Op11: N: {bin(n)}, toSwitchHigh: {bin(toSwitchHigh)}')
        n = n | toSwitchHigh

        print(f'Op12: N: {bin(n)}, toSwitchLow: {bin(toSwitchLow)}')
        n = n | toSwitchLow

        print(f'Op13: FINAL n: {bin(n)}')
        print("\n\n*********")


    return n
