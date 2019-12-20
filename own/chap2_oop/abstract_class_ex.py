from abc import ABC, abstractmethod

class Room(ABC):
    # abstract class 의 경우 @ 를 붙여서 어디서 abstrct 했는지
    # 명시한다. 그리고 method 안에는 pass 를 써서 완료해야함을
    # 보여준다. 즉, 여러명이 작업할 때, manager 는 이런 것들을 만들
    # 어야 한다고만 명시하고, 다른 사람들이 이 것들을 완료하는 것이다.
    @abstractmethod
    def openDoor(self):
        pass
    @abstractmethod
    def openWindow(self):
        pass

class BedRoom(Room):
    # Room class 를 상속 받아 완료되지 못한 것들을 완료한다.
    def openDoor(self):
        print("Open bedroom door")
    def openWindow(self):
        print("Open bedroom window")

class Lobby(Room):
    def openDoor(self):
        print("Open lobby door")

room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))

# Lobby class 에서 Room 에서 상속받은 method 를 전부 완성하지
# 않았으므로 error 가 발생한다.
lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))