import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('library_books')

"""Add new Book Details"""

def add_new_book():
    title = input("Enter book Title: ")
    author = input("Enter Author's name: ")
    category = input("Enter category: ")
    entry_date = input("Enter EntryDate: ")

    # Construct a dictionary to hold the book information
    book_data = {
        'Title': title,
        'Author': author,
        'Category': category,
        'EntryDate': entry_date
    }

    return book_data

def update_list_worksheet(data):
    print("Updating list worksheet...\n")

    headers = ['Title', 'Author', 'Category', 'EntryDate']

    list_worksheet = SHEET.worksheet("list")
    list_worksheet.append_row([data[header] for header in headers])
    

    

   

    print("List worksheet updated successfully.\n")


new_book = add_new_book()
update_list_worksheet(new_book)



"""search book from google sheet."""

list = SHEET.worksheet("list")
all_values = list.get_all_values()

book_name = input(f"Enter book name:")

found_books = []

for row in all_values:
    if book_name.lower() in row[0].lower():
        found_books.append(row[0])

if found_books:
    print(f"Books containing '{book_name}':")
    for book in found_books:
        print(book)
else:
    print(f"No books containing '{book_name}' found.")
