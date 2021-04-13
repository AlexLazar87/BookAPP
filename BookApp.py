def add_book():
    print("Add a book option")
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