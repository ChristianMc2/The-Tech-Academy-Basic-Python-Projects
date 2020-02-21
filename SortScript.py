
import os
import time





fPath = 'C:\\S\\'





os.listdir(fPath)



for i in os.listdir(fPath):
    abPath = os.path.join(fPath, i)
    if i.endswith('.txt'):
        print(os.path.join(fPath, i))
        print(os.path.getmtime(abPath))







