def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert an author name -> ")
    # importing csv library
    import csv
    with open('booksDB.csv','w') as file:
        writer = csv.DictWriter(file, fieldnames=["BookName","AuthorName","SharedWith","IsRead"])
        writer.writerow({"BookName": book_name,
                         "AuthorName": author_name})
    print("Book was added succesfully")

def list_books():
    print("List Books option")
def update_book():
    print("Update Book option")
def share_book():
    print("Share book option")

# Main menu for user
print("Menu: ")
print("1: Add a book")
print("2: List books")
print("3: Update book")
print("4: Share book")
option = int(input("Choose an option -> "))

if option == 1:
    add_book()
elif option == 2:
    list_books()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("Not a valid option")