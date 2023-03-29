filePath = "/Users/gulsahcostur/PycharmProjects/pythonProgramming2023/day06_openFile_set_dictionary/MyNotes1.txt"

file= open(filePath, "r")

fullText = file.read()

print(fullText)

print('-------------------')

file= open(filePath, "r")

firstLine = file.readline()
print(firstLine)
print('----**----')
secondLine = file.readline()
print(secondLine)

file.close()

print('-------------------')
file= open(filePath, "r")

for line in file.readlines():
    print(line)
    print('----**----')

file.close()
