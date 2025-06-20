import requests
import re

SEARCH_URL = "https://api.itbook.store/1.0/search/"
BOOK_URL = "https://api.itbook.store/1.0/books/"

''' This script searches for a book by title, retrieves its details, and validates the price format. '''
def search_books(query):
    try:
        response = requests.get(f"{SEARCH_URL}{query}")
        response.raise_for_status()
        data = response.json()
        books = data.get("books", [])
        if not books:
            print("❌ No books found.")
            return None
        return books[0]  # Return the first book
    except Exception as e:
        print(f"❌ Error during book search: {e}")
        return None

''' Fetches book details by ISBN13 from the API. '''
def get_book_details(isbn13):
    try:
        response = requests.get(f"{BOOK_URL}{isbn13}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error fetching book details: {e}")
        return None
'''
Validates the price format to ensure it matches the pattern "$X.XX" where X is a digit. '''
def validate_price_format(price):
    """
Regex Breakdown: ^\$\d+\.\d{2}$
| Part     | Meaning
|----------|-------------------------------------------------------------|
| ^        | Start of the string                                         |
| \$       | Matches a literal dollar sign "$"                           |
| \d+      | One or more digits (matches whole dollar amount)            |
| \.       | Matches the decimal point "."                               |
| \d{2}    | Exactly two digits (matches the cents)                      |
| $        | End of the string                                           |
"""
    return bool(re.match(r"^\$\d+\.\d{2}$", price))

'''
Main function to execute the book search and details retrieval. '''
def main():
    query = input("🔍 Enter a search term: ").strip()
    first_book = search_books(query)
    if not first_book:
        return

    isbn13 = first_book.get("isbn13")
    if not isbn13:
        print("❌ ISBN13 not found in the first book result.")
        return

    details = get_book_details(isbn13)
    if not details:
        return

    print("\n📚 Book Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

    price = details.get("price", "")
    print("\n💵 Price Validation:")
    if validate_price_format(price):
        print(f"✅ Price '{price}' is in the correct format.")
    else:
        print(f"❌ Price '{price}' is NOT in the correct format.")

if __name__ == "__main__":
    main()
