# file handling
import os

file=open("python.txt",'r')
# data=file.read()  #i can pass a number as argument whcih tells teh number of charcters to read
# print(data)
# print(type(data))

line1=file.readline()  #reads one line at a time
print("line 1 data",line1)
line2=file.readline() 
print("line  2dtaa",line2)


file.close()  # for cosing theh fie tat u have opened

# different file modes :
# r-reading teh data of the file
# w-writing the data (it will overwrite the data of the file after deleting teh  whole content)
# x-create a new file and open it for writing
# a-open for writing and appending the data  to the existing data
# b- if we are opening a binary file we will write b
# t- if openieng a text file we will write t 
# +- opens a text file for updation  ie. reading and writing


file1=open("python.txt",'a')

file1.write("I have to learn django")
file1.close()

with open('python.txt','r') as f:
    data=f.read()
    print(data)

    # when we are opening any file using the with keyword there is no need to close it

# for deleting any file we need to use the os module  for deletig any file
os.remove("python.txt")