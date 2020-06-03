'''
class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"{self.author} has written the book {self.title} which is very interesting book for coders in Python"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A Book object has been deleted")
b=Book("Core Python Programming","Nageshwarrao",2000)
print(str(b))
print(b)
print(len(b))
#del b  #After writting this statement you will not be able to further access the object b
#print(b)    #that is this line of code will nto execute
del b
'''



