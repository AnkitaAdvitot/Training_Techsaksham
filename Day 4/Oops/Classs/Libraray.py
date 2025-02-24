class Library:
    def __init__(self):
        self.books=[]
    def add(self,title):
        self.books.append(title)
    def remove(self,title):
        self.books.remove(title)
    
    def displayBooks(self):
        print("||||||||||||List of Books||||||||||||||||\n",self.books)

obj=Library()
obj.add("Ikigai")
obj.add("Harry Potter")
obj.displayBooks()
obj.remove("Ikigai")
obj.displayBooks()