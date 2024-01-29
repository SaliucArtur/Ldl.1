class Book:
    def __init__(self, title, author, isbn):
        self.Title = title
        self.Author = author
        self.ISBN = isbn


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the book's Title: ")
        author = input("Enter the book's Author: ")
        isbn = input("Enter the book's ISBN: ")

        book = Book(title, author, isbn)
        self.books.append(book)

        print(f"Book '{book.Title}' added to the library.")

    def remove_book(self):
        isbn = input("Enter the ISBN of the book to remove: ")

        index_to_remove = next((i for i, book in enumerate(self.books) if book.ISBN == isbn), -1)

        if index_to_remove != -1:
            removed_book = self.books.pop(index_to_remove)
            print(f"Book '{removed_book.Title}' removed from the library.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"{book.Title} ({book.Author})")


library = Library()

while True:
    print("What would you like to execute?")
    print("1) Add a book?")
    print("2) Remove a book?")
    print("3) Display all books in the library?")
    print("4) End")

    choice = input()

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.remove_book()
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        break
    else:
        print("Invalid input. Please enter a valid number.")

    while True:
        response = input("Would you like to continue? (yes/no): ").lower()
        if response == "no":
            exit()
        elif response == "yes":
            break
        else:
            print("Write again")

