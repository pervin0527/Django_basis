class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"{self.title} written by {self.author}"
    

mybook = Book(title="그대들 어떻게 살 것인가?", author="Minjun Kim", pages=100) 
print(mybook)
print(len(mybook))