import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("library_books")



"""Add new Book Details"""

def add_new_book(Title, Author,  EntryDate):
    return f"{Title}, {Author}, {EntryDate}"

"""
Get user input for book title and author
"""
Title = input("Enter the book Title: ")
Author = input("Enter the Author's name: ")
EntryDate = input("Enter the book EntryDate: ")

"""
Call the function with user input
"""
new_book = add_new_book(Title, Author,  EntryDate)
print(new_book)


"""To update google sheet"""

def update_nonfiction_worksheet(data):
    """
    update nonfiction worksheet add new row with the list data provided.
    """
    print("updating nonfiction worksheet...\n")
    nonfiction_worksheet = sheet.worksheet("nonfiction")
    
    print("nonfiction worksheet update sucessfully.\n")

data = add_new_book(Title, Author, EntryDate)
new_book = add_new_book(Title, Author, EntryDate)
print(new_book)
update_nonfiction_worksheet(new_book)


"""search book from google sheet."""

nonfiction = sheet.worksheet("nonfiction")
all_values = nonfiction.get_all_values()  # Corrected function call

book_name = input(f"Enter book name:")

found_books = []

# Loop through the rows to search for the book
for row in all_values:
    if book_name.lower() in row[0].lower():
        found_books.append(row[0])

if found_books:
    print(f"Books containing '{book_name}':") 
    for book in found_books:
        print(book)
else:
    print(f"No books containing '{book_name}' found.")
