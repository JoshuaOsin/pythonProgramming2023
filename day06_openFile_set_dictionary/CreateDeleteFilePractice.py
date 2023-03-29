from os import mkdir, rmdir
from shutil import rmtree

directoryName = 'MyFolder2'
mkdir(directoryName)
print(directoryName)
rmdir(directoryName) #delete empty directory or folder

directoryName = 'MyFolder3'
mkdir(directoryName)

i = 1

while i <= 5:
    open(f'{directoryName}/Test{i}.txt', 'x')
    i += 1
print(directoryName)
rmtree(directoryName) #delete folder which is not empty


