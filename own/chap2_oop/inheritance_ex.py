# Super Class(Base Class)
class Father(object):
    # Father 라는 class 의 attribute(member variable)
    strHometown = 'Jeju'
    
    # Constructor(class 를 만들 때 항상 생성되는 것)
    def __init__(self):
        print("Father is created.")
    
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")

# Super Class(Base Class)
# Mother(상속받을 class 의 이름.)
# 여기서 object 라는 것은 Python 에서 가장 상위에 있는 아무것도 들어
# 있지 않은, 가장 Generalized 된 것이라고 볼 수 있다.
# object 는 Default 라 쓰지 않아도 Python 에선 자동으로 상속한다.
class Mother(object):
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created.")
    
    def doMotherThing(self):
        print("Mother's action")

# Multiple Inheritance (Father class 와 Mother class 에서 상속)
class Child(Father, Mother):
    strName = "Moon"
    def __init__(self):
        # 내가 inherit 하고 있는 상위 단계의 superclass 를 call
        super(Child, self).__init__()
        print("Child is created.")
    # Although Father class has doRunning method,
    # Child class want to have new method of his/her own.
    def doRunning(self):
        print("Fast")

# me 라는 변수는 Child 클래스(설계도)를 Intantiate 하여 
# Father 와 Mother class 의 성질을 가진 Child 자체의 집을 만든다.
me = Child()

# inherit 했기 때문에 Child class 에서도 쓸 수 있다.
me.doFatherThing()
me.doMotherThing()

# Child 의 형질을 override 한 것이기 때문에, Father class 의
# doRunning 이 call 되는 것이 아니라, Child 자신의 doRunning called
me.doRunning()

# 가장 먼저 상속 받은 class 의 Member Variable call
print(me.strHometown)

print(me.strName)