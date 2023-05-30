BASE = 265
MODULUS = 101

def hashExtend(c, prevHash):
  return (prevHash * BASE + ord(c) * 1) % MODULUS


def hashShift(cAdd, cRem, prevHash, power):
  return (BASE * (prevHash - (ord(cRem) * power)) + ord(cAdd)) % MODULUS

def squareAtLastCharWithHash(s):
  hashLeft = 0
  posRight = 0
  hashRight = 0
  power = 1
  len_s = len(s)
  for suffixLength in range(2, len(s) + 1, 2):
    c = s[len_s - suffixLength // 2]
    hashRight = hashExtend(c, hashRight)
    posRight += 1
    cAdd = s[len_s - suffixLength + 1]
    cExt = s[len_s - suffixLength]
    if (suffixLength == 2):
      hashLeft = hashExtend (cExt, hashLeft)
    else:
      hashShifted = hashShift(cAdd, c, hashLeft, power)
      hashLeft = hashExtend(cExt, hashShifted)
      power = power * BASE
    if hashLeft == hashRight:
      return True
  return False
