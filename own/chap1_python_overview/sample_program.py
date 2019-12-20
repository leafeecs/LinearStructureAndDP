# class declaration
class CashierLine:
    # Member Variable
    lstLine = []
    lineNumber = ''
    
    # Member Function(Method)
    def addCustomer(self, strName):
        self.lstLine.append(strName)
    def processCustomer(self):
        strReturnName = self.lstLine[0]
        self.lstLine.remove(strReturnName)
        return strReturnName
    def printStatus(self):
        strReturn = ''
        for itr in range(len(self.lstLine)):
            strReturn += self.lstLine[itr] + ' '
        return strReturn

    def __init__(self, lineNumber):
        self.lineNumber = lineNumber
    def __del__(self):
        pass

binLoop = True

# 설계도를 이용해 하나의 instance 를 create 하고 constructor 에 넣음
line = CashierLine('1')

while binLoop:
    print("If you want to quit, press 'q'.")
    print("After check one person out(enter 'check'):")
    strName = input("Add to line(enter a name): ")

    if strName == 'q':
        break
    elif strName == 'check':
        print("Processed:", line.processCustomer())
        print("Line:", line.printStatus())
    else:
        line.addCustomer(strName)
        print("Line:", line.printStatus())
print("Number of remaining customer:", len(line.lstLine))

x = [1,2,3]
y = [100,x,120]
print(y)

z = 1.23
print(type(z))