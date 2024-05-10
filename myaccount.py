import pandas as pd
from gmail import send_gmail

def find_book(bname,name,password,phone):
    csv_file = 'books.csv'
    df = pd.read_csv(csv_file)
    result = df[df['books'] == bname]
    if not result.empty:
        book_is = result['books'].values[0]
        price = result['price'].values[0]
        return book_is,price
    else:
        return f"No record found for {bname}."


def proceed(name,password,phone):
    choice = input(f"welcome {name}\nNOTE : remember not to put ',' while writing book name\nWe can deliver books to your home with cash on delivery as well as come to take it\nPlease select if you want to\nissue a book\nreturn a book\nBuy a book\nSell a book\nBack\n").lower()

    if choice == 'issue a book':
        bname = input('Please enter the book name you want to issue: ').lower()

        book_is,price = find_book(bname,name,password,phone)

        if bname == book_is:
            print(f'{bname} is available for Rs {price}')
            pass2 = input('Please enter your password to proceed: ')
            if pass2 == password:
                print('Thanks for your order the book will be delivered with the help of phone number\n')
                send_gmail(bname,name,phone)
        else:
            print(f'Sorry {name} the book is not available')

    elif choice == 'return a book':
        bname = input('Please enter the book name you want to return: ').lower()

    elif choice == 'buy a book':
        bname = input('Please enter the book name you want to buy: ').lower()

    elif choice == 'sell a book':
        bname = input('Please enter the book name you want to sell: ').lower()

    else:
        print('ERROR: unable to understand the operation, please try again')