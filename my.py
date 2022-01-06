import os
path1 = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'

def nop():
    nofip=0
    for i in os.listdir(path1):
        nofip+=1
    return nofip

p = nop()
print(p)