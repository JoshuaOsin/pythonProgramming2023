# stop while loop BREAK
i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break
print('----------------')

# first  unique char
word = 'aaabssssdkkkk'
print(word)
for each in word:
    count = word.count(each)
    if count == 1:
        print(each)
        break

# Skip Iteration CONTINUE
print('----------------')

z = 'ABCDE'
for each in z:
    if each == 'C':
        continue
    print(each)

# PASS is used for placeholder
print('----------------')

if True:
    pass

print('Test completed')
