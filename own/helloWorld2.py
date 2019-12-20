# Hello World in Python

# Your second Python program in this class

# class declaration
class HelloWorld():
    # self 는 함수 자신을 의미함.
    # init 은 class 가 initiate 을 통해 instance 으로 바뀌고 생성될 때 init
    # 이 실행된다.
    # constructor
    def __init__(self):
        print("Hello World! Just one more time")

    # del 은 instance 가 없어질 때 실행뙨다.
    def __del__(self):
        print("Good bye")

    # 여기서 self 는 instance 를 접근하고자 할 때 자신이 이용하기 위해 받아들
    def performAverage(self, val1, val2):
        average = (val1, val2) / 2.0
        print("The average of the scores is: ", average)

# class 이용을 함수화
# function declaration
def main():
    # HelloWorld 라는 클래스를 한 번 만들어봐라 하는 명령어
    # world 라는 것은 instance 를 storage 하는 variable
    # HelloWorld 는 instance 를 template 하는 마치 붕어빵 기계
    world = HelloWorld()

    score1, score2 = input("Enter two score separated by a comma: ").split(',')

    # . 은 world, 즉 HelloWorld class 속에 담긴 함수를 실행해봐라는 것
    world.performAverage(float(score1), float(score2))

# function 을 trigger 하기 위함
main()



