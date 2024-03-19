# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class book:
    def __init__(self,title):
        self.title= title 

# TODO: create instances of the class
b1=book("self made millionaire ")
b2=book("atomic habits")

# TODO: print the class and property
print(b1)
print(b2.title)