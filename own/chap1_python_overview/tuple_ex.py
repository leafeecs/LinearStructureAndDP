tplTest = (1, 2, 3) 

print('-----------------------------------------')
print(tplTest)
print(tplTest[0], tplTest[1], tplTest[2])
print(tplTest[-1]), tplTest[-2]
print(tplTest[1:3])
print(tplTest + tplTest)
print(tplTest * 3)

# Tuple 은 immutable, 즉 변경할 수 없다. 왜냐하면 여러사람이 쓰는
# 프로그램에서 바꿀 수 없는 값도 필요하기 때문이다.
tplTest[0] = 100