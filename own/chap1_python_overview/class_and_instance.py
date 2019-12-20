# class 는 설계도와 같다.
class MyHome:
    colorRoof = 'red'
    stateDoor = 'closed'

    # 여기서 self 가 가리키는 것은 instance 그 자체이다.
    # 즉, 설계도 마다 변수가 있는데, self 를 이용하면 그 집의
    # 변수가 바뀐다.
    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDoor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Door color is", self.colorRoof, \
            ", and door is", self.stateDoor)

# 설계도를 이용해 instantiation 을 하여 집들(instances) 를 만듦
# 설계도를 호출한다는 것은 사실 설계도 안에 있는 Constructor 를 호출.
homeAtDaejeon = MyHome()
homeAtSeoul = MyHome()

# 기본 설계도는 default 로 설정하되, 각각의 집에 맞는 설정을 바꾼다.
homeAtSeoul.openDoor()
homeAtSeoul.paintRoof('blue')

homeAtDaejeon.printStatus()
homeAtSeoul.printStatus()

