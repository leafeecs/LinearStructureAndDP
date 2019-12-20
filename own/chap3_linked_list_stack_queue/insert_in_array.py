# Goal: insert 'c' between 'b' and 'd' in list x
# Btw, a := instert position index
x = ['a', 'b', 'd', 'e', 'f']
print("Before insert 'c' b/w 'b' and 'd':", x)

idxInsert = 2
valInsert = 'c'

# 1. Make new list, or y, with six cells
y = list(range(6))

# 2. Copy the reference links of x[0:a-1] to y[0:a-1]
# (retrieval count: a)
for itr in range(0, idxInsert):
    y[itr] = x[itr]

# 3. Put a reference link to 'c' in y[a] 
# (retrieval count: 1)
y[idxInsert] = valInsert

# 4. Copy the reference links of x[a:] to y[a+1:]
# (retrieval count: n-a-1)
for itr in range(idxInsert, len(x)):
    y[itr+1] = x[itr]

# 5. Change y's reference to x's reference
x = y

# Total count of retrievals = a + 1 + n - a - 1 = n
print("After insert 'c' b/w 'b' and 'd':", x)
