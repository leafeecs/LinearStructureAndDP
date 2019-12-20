class Father(object):
    strHometown = 'Jeju'
    
    def __init__(self, paramHome):
        self.strHometown = paramHome
        print("Father is created.")
    
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created.")
    
    def doMotherThing(self):
        print("Mother's action")

# Multiple Inheritance 의 경우 상속받을 때 첫 번째 superclass
# 의 attributes, methods 를 상속받는다.
class Child(Father, Mother):
    strName = "Moon"
    def __init__(self, paramName, paramHome):
        # super 라고 하는 것은 상속받고 있는 Base class 를 의미한다.
        # 즉 거꾸로 읽으면 내 자신이, Child 라고 하는 것의 super 에서
        # constructor 를 찾고 있고, paramHome 을 건내주고 있다.
        super(Child, self).__init__(paramHome)

        # self 라고 하는 것은 인스턴스 자신을 말한다.
        # 즉 아래에서 me 라는 instance 가 Child 클래스를 이용해
        # 집을 만들었는데, 그 member variable 을 자신이 원하는
        # Kim 으로 바꾸는 것이다.
        self.strName = paramName
        print("Child is created.")

    def doRunning(self):
        print("Fast")

me = Child("Kim", "Changwon")
me.doFatherThing()
me.doMotherThing()
me.doRunning()

print(Father.strHometown)
# strHometown 을 Father class 로 부터 상속 받았지만, 내가 태어난
# 곳으로 바꾸고 싶을 때 Child class 의 Constructor 를 수정한다.
print(me.strHometown)
print(me.strName)