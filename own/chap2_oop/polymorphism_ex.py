class Building:
    strAddress = 'Daejeon'
    def openDoor(self):
        print("Door Opened")
    def checkIn(self):
        print("Someone checks in for 1 day.")

    def __init__(self, paramAddress):
        self.strAddress = paramAddress
    def __del__(self):
        pass


class Hotel(Building):
    hotelAddress = "Seoul"
    def openDoor(self):
        print("Bellboy opens a door")
    
    # Method Overloading
    # 여기서 days = 1 은 들어오면 들어온 값으로 바꾸고, 아니라면
    # default 값을 1 이라고 지정한다.
    def checkIn(self, days = 1):
        print("Someone checks in for", days, "days")
    
    def __init__(self, paramAddress):
        self.hotelAddress = paramAddress
        print("Hotel at", self.hotelAddress)
    def __del__(self):
        pass

print(Building.strAddress)
print(Hotel.hotelAddress)
lotteHotel = Hotel("Changwon")
lotteHotel.openDoor()
lotteHotel.checkIn()
lotteHotel.checkIn(2)