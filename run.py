import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("library_books")

"""Add new Book Details"""
def add_new_book():

    Title = input("Enter book Title: ")
    Author = input("Enter Author,s name:")
    EntryDate = input("Enter EntryDate:")

    return f"Title, Author, EntryDate"
    

new_book = add_new_book()
print(new_book)


"""Updating googlesheet"""

def update_list_worksheet(data):
    print("updating list worksheet...\n")
    list_worksheet = sheet.worksheet("list")
    
    print("list worksheet  updated succesfully.\n")

data = add_new_book()   
new_book = add_new_book()
update_list_worksheet(new_book)




"""search book from google sheet."""

list = sheet.worksheet("list")
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
