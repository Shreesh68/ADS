#Q1

import sys
with open(sys.argv[1], 'r') as f:
    contents = f.read()
print(contents)





  #  Q2
fname = "Q2.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
    print(num_lines)
    print(num_words)
    print(num_chars)

#Q3

def openfile_sumofallnums:

        filename = input("Please enter your file name: ")
        sum_number = 0
        openthefile = open(filename, "r")

        for i in openthefile:
            Split = i.split(',')
            Join = "".join(Split)
            print(Join)

        for i in Join:
            sum_number = sum_number + float(i)

        print("The sum of your numbers is",sum_number)

#Q15
def group_intosmalllist(x,l):
        gl=[]
        g=[]
        i=0
        while i<len(x):
                if(len(gl)<l):
                        gl.append(x[i])
                        i=i+1
                else:
                        g.append(gl)
                        gl=[]
        g.append(gl)
        return g

#Q14

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

#q7
import os
import sys

def getfilenames(path):
    ftype = path.split(".")[-1]
    folder = path.split("*")[0]
    return [i for i in os.listdir(folder) if ftype in i.split(".")[-1]]

print(getfilenames(sys.argv[1]))



#q10
import os 

list_files = []    
for root, dirs, files in os.walk(input_folder):
        for filename in files:
            joined = os.path.join(input_folder, filename)
            list_files.append(joined)

#q8
import sys
import os

max_size = 0
size = 0
max_file = ''

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

print(os.walk(path))

for folders, subfolder, files in os.walk(path):
    for f in files:
        size = os.stat(os.path.join(folders, f)).st_size
        if size > max_size:
            max_size = size
            max_file = os.path.join(folders, f)
print("Largest File: ", max_file)
print("File size: ", max_size)


#q6
import sys
import shutil

shutil.copy(sys.argv[1], sys.argv[2])


