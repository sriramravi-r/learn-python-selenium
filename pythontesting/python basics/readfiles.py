file=open("test.txt") #open file
#print(file.read()) #read file
#print(file.read(3)) #print char less than given num
#read one single line at a time
print(file.readline())
print(file.readline())

#print line by line using readline method
# line=file.readline()
# while line != "":
#     print(line)
#     line=file.readline()

# values=file.readlines();
for val in file.readlines(): #return list

    print(val)

file.close() #close file
