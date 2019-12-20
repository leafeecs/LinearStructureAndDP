class Room:
    numWidth  = 100
    numHeight = 100
    numDepth = 100

    # 기본적으로 __init__, __del__, __eq__, __cmp__, __add__
    # 는 object 에 있는 method 이다. 즉 Room class 는 deefault로
    # Object 의 method 를 overriding 항여 수정하는 것이다.
    def __init__(self, parWidth, parHeight, parDepth):
        self.numWidth = parWidth
        self.numHeight = parHeight
        self.numDepth = parDepth
    
    def getVolume(self):
        return self.numWidth * self.numHeight * self.numDepth
    
    def __eq__(self, other):
        if isinstance(other, Room):
            # Duc Typing
            if self.getVolume() == other.getVolume():
                return True
        return False

room1 = Room(100, 20, 30)
room2 = Room(100, 10, 60)
print(room1 == room2)

    