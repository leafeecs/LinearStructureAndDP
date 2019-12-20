numA = 1
numB = 2

def add(numParam1, numParam2):
    return numParam1 + numParam2

# You can return multiple variables
# However, you have to keep them in order
def multiply(numParam1, numParam2):
    return numParam1*2, numParam2*3

def increase(numParam1, step = 1):
    return numParam1 + step

numC = add(numA, numB)
print(numC)

numD, numE = multiply(numA, numB)
print(numD, numE)

numF = increase(numA, 2)
print(numF)

numG= increase(numA)
print(numG)

lambdaAdd = lambda numParam1, numParam2 : numParam1 + numParam2
numH = lambdaAdd(numA, numB)
print(numH)