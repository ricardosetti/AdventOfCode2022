

file1 = [char for char in open("day6.txt").read()]
# print(file1)
length = len(file1)
print(length)
code = 0
codeFound = False
for i in range(3, length):
    tempSequence = str(file1[i]+file1[i-1]+file1[i-2]+file1[i-3])
    print(tempSequence)
    if (tempSequence.count(tempSequence[0])==1)&(tempSequence.count(tempSequence[1])==1)&(tempSequence.count(tempSequence[2]) == 1) & (tempSequence.count(tempSequence[3])==1):
        codeFound = True
        code = i+1
        break


print(code)


