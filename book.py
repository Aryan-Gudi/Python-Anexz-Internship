class Book:
    def __init__(self, book_id, book_title, author_name, price, availability_status):
        self.__book_id = book_id
        self.__book_title = book_title
        self.__author_name = author_name
        # Set price using the setter to include validation
        self.set_price(price) 
        self.__availability_status = availability_status

    # Getters
    def get_book_id(self):
        return self.__book_id

    def get_book_title(self):
        return self.__book_title

    def get_author_name(self):
        return self.__author_name

    def get_price(self):
        return self.__price

    def get_availability_status(self):
        return self.__availability_status

    # Setters
    def set_book_id(self, book_id):
        self.__book_id = book_id

    def set_book_title(self, book_title):
        self.__book_title = book_title

    def set_author_name(self, author_name):
        self.__author_name = author_name

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Error: Price must be a positive value.")
            # Depending on requirements, raising an exception might be better, 
            # but for introductory examples printing an error is common.
            # I will default to printing but setting the value to 0 or keeping previous if it existed
            # In __init__, we need a valid initial state. Let's assume user provides valid input or handle it gracefully.
            # If called from __init__ with invalid price, this might leave __price undefined if we don't handle it.
            # I'll initialize it to 0.0 if invalid in setter, or raise ValueError for better robustness.
            # "Include validation... ensure price is positive" - implies we should reject non-positive.
            if not hasattr(self, '_Book__price'):
                 self.__price = 0.0

    def set_availability_status(self, availability_status):
        self.__availability_status = availability_status

# Example Usage
if __name__ == "__main__":
    my_book = Book(101, "Python Programming", "John Doe", 29.99, True)
    
    # Accessing data via getters
    print(f"Book Title: {my_book.get_book_title()}")
    print(f"Price: ${my_book.get_price()}")

    # Updating data via setters
    my_book.set_price(35.50)
    print(f"New Price: ${my_book.get_price()}")

    # Testing validation
    my_book.set_price(-10)  # Should print error
    print(f"Price after invalid set: ${my_book.get_price()}")
