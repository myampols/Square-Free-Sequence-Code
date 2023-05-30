import random

T = 4
fullAlphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = fullAlphabet[:T]

def squareAtLastChar(s):
  for suffixLength in range(2, len(s)+1, 2):
    suffix = s[len(s)-suffixLength:]
    if suffix[0:suffixLength//2] == suffix[suffixLength//2:]:
      return True
  return False

def allSquarefreeWords(currentString, constraints):
  if len(currentString) == len(constraints):
    return 1
  characterPossibilities = constraints[len(currentString)]
  sum = 0
  for c in characterPossibilities:
    if not squareAtLastChar(currentString+c):
      sum += allSquarefreeWords(currentString+c, constraints)
  return sum

def generateNormalConstraints(N):
  return [alphabet[:3]]*N

def generateRandomConstraints(N):
  C = []
  for i in range(N):
    C.append("".join(sorted(random.sample(alphabet, 3))))
  return C

def generateShiftingConstraints(N):
  repeated = alphabet*(N + 1)
  C = []
  for i in range(N):
    C += [repeated[i : i + 3]]
  return C
  
def hasDec():
  hasDecreases = []
  for run in range(1000):
    print(run, hasDecreases)
    currRand_C = generateRandomConstraints(N)
    currOutput = allSquarefreeWords("", [currRand_C[0]])
    for i in range(2, N+1):
      newOutput = allSquarefreeWords("", currRand_C[:i])
      if newOutput <= currOutput:
        hasDecreases += [currRand_C]
        break
  return hasDecreases
