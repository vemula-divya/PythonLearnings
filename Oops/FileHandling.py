f = open('Mydata', 'r')  # filename,Mode(write,read,overwrite...)
# print(f.__next__())
# print(f.read())  # to fetch data
# print(f.readline())  # it  reads only first line
# print(f.readline())  # 2nd time it will print 2nd line
# print(f.readline(4))  # it gives 4 char

# f1 = open('NewFile', 'w')  # if file is not present it will create a file
# f1.write("new write file")  # check the file for content

# f1.write('overrides') if the file contains something and if you open with write mode it will override.
# to append
f1=open('NewFile','a')
#f1.write("append")

f2=open('NewFile','r')
#print(f2.read())

# to get the data from mydata to new file

# file1=open('MyData','r')
# file2=open('NewFile','w')
#
# for data in file1:
#     file2.write(data)

#file has char and binary format (image)

image1=open('Img_01','rb')
image2=open('Img_copy_01','wb')
for i in image1:
    image2.write(i)
