# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title,published_on ):
        self.title = title
        # TODO: add properties
        self.published_on = published_on 

    # TODO: create instance methods


# TODO: create some book instances
b1 = Book("War and Peace",12/3/24)
b2 = Book("The Catcher in the Rye",12/3/24)

# TODO: print the price of book1


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
