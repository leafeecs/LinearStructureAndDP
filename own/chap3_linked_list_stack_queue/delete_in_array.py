# Goal: remove 'd' in the list 
# a := delete position index)

x = ['a', 'b', 'c', 'd', 'e', 'f']
print("Before delete 'd':", x)

idxDelete = 3

# 1. Make new list, or y, with 5 cells
y = list(range(5))

# 2. Copy the reference links of x[0:a-1] to y[0:a-1]
# retrieval count: a
for itr in range(0, idxDelete):
    y[itr] = x[itr]

# 3. Copy the referencee links of x[a+1:] to y[a:]
for itr in range(idxDelete+1, len(x)):
    y[itr-1] = x[itr]

# 4. change y's reference to x's reference
x = y

# Total count of retrievals = a + n - a - 1 = n - 1 ~= n
print("After delete 'd':", x)
