lstTest = [1, 2, 3, 4]

print('-----------------------------------------')
print(lstTest)
print(lstTest[0], lstTest[1], lstTest[2])
print(lstTest[-1], lstTest[-2])
print(lstTest[1:3])
print(lstTest + lstTest)
print(lstTest * 3)

print('-----------------------------------------')
# In Python2, range returns a list
# However, in Python3, range returns a range object.
# The range object does not have an append method.
# To fix, convert the range object to a list
lstTest = list(range(1, 20, 3))
print(lstTest)
print(4 in lstTest, 100 in lstTest)
lstTest.append('hey')
print(lstTest)

print('-----------------------------------------')
del lstTest[0]
print(lstTest)
lstTest.reverse()
print(lstTest)

print('-----------------------------------------')
# remove the value in the list
lstTest.remove(4)
print(lstTest)

