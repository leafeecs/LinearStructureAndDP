from time import ctime

# class 는 설계도와 같다.
class MyHome:
    # Member Variable
    colorRoof = 'red'
    stateDoor = 'closed'

    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDoor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Door color is", self.colorRoof, \
            ", and door is", self.stateDoor)
    
    # Consructor: Called when instantiated
    def __init__(self, strAddress):
        print("Built on", strAddress)
        print("Built at", ctime())
    
    # Deconstructor: Called when the instance is removed 
    #                from the value table
    # 현실에서는 많이 쓰지 않지만, 안전한 프로그래밍을 위해서 필요하다.
    def __del__(self):
        print("Destroyed at", ctime())

# class 를 이용해 instantiation 을 하면 Daejeon KAIST 는 
# constructor 의 strAddress 로 들어간다. 즉 Daejeon KAIST 로
# 초기화 하는 것이다.
homeAtDaejeon = MyHome("Daejeon KAIST")
homeAtDaejeon.printStatus()
del homeAtDaejeon

print("-----------------------------------------------")
# 새로운 집을 설계도를 통해 하나 만든다. 그리고, 서울의 서울대에 집을 하나
# 새로 짓는 것이다. 설계도에서 수정하고 싶은 부분을 초기화 하는 것.
homeAtSeoul = MyHome("Seoul SNU")
homeAtSeoul.printStatus()
del homeAtSeoul

