for itr in range(10):
    print(itr)

print()

sum = 0
for itr in range(1, 11):
    sum += itr
print(sum)

print()

for itr in range(1, 100, 10):
    if (itr == 51):
        continue
    else:
        print(itr)

print()

# else: when for-loop is finished without a break
for itr in range(5):
    print(itr)
else:
    print(':')
print('done')

print()

# break will be exited for-else statement
for itr in range(5):
    if itr == 3:
        break
    print(itr)
else:
    print('finished')
print('done')