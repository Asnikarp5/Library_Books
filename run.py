import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("library_books")

"""
children= sheet.worksheet("children")

data = children.get_all_values()

print(data)
"""



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










