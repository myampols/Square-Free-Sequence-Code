import random

def createListConstraints(Sets):
  n = len(Sets)
  numClauses = 0
  constraints = ""
  for coordinate in range(n):
    currentSet = Sets[coordinate]
    clause1 = ""
    for possibility in currentSet:
      clause1 += str(possibility + 4 * coordinate) + " "
    clause1 += "0\n"
    clause2 = "k 3 "
    for possibility in {1, 2, 3, 4}:
      clause2 += "-" + str(possibility + 4 * coordinate) + " "
    clause2 += "0\n"

    constraints += clause1 + clause2
    numClauses += 2

  return (constraints, numClauses)


def createAdjacencyConstraints(Sets):
  n = len(Sets)
  numClauses = 0
  constraints = ""
  for wordLen in range(1, n // 2 + 1):
    print("wordLen = " + str(wordLen))
    for startingIndex in range(n - 2 * wordLen + 1):
      combinations = allCombinations(wordLen)
      for combination in combinations:
        clause = ""
        for x in range(len(combination)):
          c = combination[x]
          clause += "-" + str((startingIndex + x) * 4 + c) + " "
          clause += "-" + str((startingIndex + wordLen + x) * 4 + c) + " "
        clause += "0\n"
        constraints += clause
        numClauses += 1
  return (constraints, numClauses)


def createFormula(Sets):
  print("creating list constraints")
  (listConstraints, numClauses1) = createListConstraints(Sets)
  print("creating adjacency constraints")
  (adjacencyConstraints, numClauses2) = createAdjacencyConstraints(Sets)
  numVariables = 4*len(Sets)
  numClauses = numClauses1 + numClauses2
  return "p knf " + str(numVariables) + " " + str(numClauses) +"\n" + listConstraints + adjacencyConstraints


def allCombinations(wordLen):
  if wordLen == 1:
    return [[1], [2], [3], [4]]
  combinations = []
  for lastCoordinateValue in range(1, 5):
    for combination in allCombinations(wordLen - 1):
      combination.append(lastCoordinateValue)
      combinations.append(combination)
  return combinations


# for i in range(1, 4):
#   print(allCombinations(i))


def writeToFile(fileName, text):
  o = open(fileName, 'w')
  o.write(text)
  o.close()

# for n in range(1,100):
#   print("n = " + str(n))
#   Sets = [{1, 2}]*n
#   output = createFormula(Sets)
#   writeToFile("test_" + str(n) + ".knf", output)

def generateRandomSetsTest(n):
  Sets = []
  for i in range(n):
    Sets.append(set(random.sample({1, 2, 3, 4}, 3)))
  output = createFormula(Sets)
  writeToFile("test_random" + str(n) + ".knf", output)
