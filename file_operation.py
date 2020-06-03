#with the help of python you can read as well as write data to a file and even create a file
#Here I have created a sample text file as "file.txt" in the same project
f=open("file1.txt","r")
'''read() will return all the contents of the file as a single giant string'''
print(f.read())
print(f.read())
'''If you already read the file once and you try to read it again it will display nothing because
once for the first time you have read the file then after reading this file for the first time the cursor will be there at the 
end of the file'''
'''In order to bring the cursor back to the starting/begining of the text file you will have to use the seek() function
  and assign it the value of '0' so as to bring the cursor at the starting of the file.'''
f.seek(0)
print(f.read())
f.close()



'''readlines() method will return the seperate lines in a file as a list.These seperate lines will be the individual 
components of the list.'''
'''readline() method will return a single line from the file.'''
f=open("file1.txt","r")
print(f.readlines())
print(f.readline())
'''Here it will display nothing because you are already at the end of the file i.e the file cursor is at the 
end of the file just the poroblem which had been earlier mentioned in the case of read() function'''
f.seek(0)
print(f.readline())
f.close()



'''While using the 'with-as' block there is no need to externally close the file as shown in the below example'''
with open("myfile.txt","w") as f1:
    f1.write("Hello\n This is another new File created by me\nThis is the file created internaly. ")
print("The file 'myfile.txt' is closed is ",f1.closed)
with open ("myfile.txt","r")as file:
    print(file.read())
