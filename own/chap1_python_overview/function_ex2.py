def isPrimeNumber(numParam1):
    for itr in range(2, numParam1):
        if numParam1 % itr == 0:
            break
    else:
        return True
    return False

def findPrimes(numParam1, numParam2):
    numCount = 1
    for itr in range(numParam1, numParam2):
        if isPrimeNumber(itr) == True:
            print(f"{numCount}th prime: {itr}")
            numCount += 1
        
findPrimes(1, 10)