filePath = "TestFile2.txt"

open(filePath, 'x')

file = open(filePath, 'a')
file.write('Cydeo School\n')
file.write('Python Programming\n')
file.close()