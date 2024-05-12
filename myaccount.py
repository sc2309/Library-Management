import pandas as pd
from gmail import send_msg

def find_book(bname,name,password,phone):
    csv_file = 'books.csv'
    df = pd.read_csv(csv_file)
    result = df[df['books'] == bname]
    if not result.empty:
        book_is = result['books'].values[0]
        i_price = result['i_price'].values[0]
        price = result['price'].values[0]
        return book_is,price,i_price
    else:
        return f"No record found for {bname}."


def proceed(name,password,phone):
    choice = input(f"welcome {name}\nNOTE : remember not to put ',' while writing book name\nWe can deliver books to your home with cash on delivery as well as come to take it\nPlease select if you want to\nissue a book\nreturn a book\nBuy a book\nSell a book\n").lower()

    if choice == 'issue a book':
        bname = input('Please enter the book name you want to issue: ').lower()

        book_is,price,i_price = find_book(bname,name,password,phone)

        if bname == book_is:
            print(f'{bname} is available for issue for Rs {i_price}')
            pass2 = input('Please enter your password to proceed: ')
            if pass2 == password:
                print('Thanks for your order the book will be delivered with the help of phone number\n')
                send_msg(f'book {bname} was ordered by {name}, phone no. {phone}, operation : {choice}')
        else:
            print(f'Sorry {name} the book is not available')

    elif choice == 'return a book':
        bname = input('Please enter the book name you want to return: ').lower()
        send_msg(f'{name} wants to return the book {bname}, phone no. {phone}, operation : {choice}')

    elif choice == 'buy a book':
        bname = input('Please enter the book name you want to buy: ').lower()
        book_is,price,i_price = find_book(bname,name,password,phone)

        if bname == book_is:
            print(f'{bname} is available for buying for Rs {price}')
            pass2 = input('Please enter your password to proceed: ')
            if pass2 == password:
                print('Thanks for your order the book will be delivered with the help of phone number\n')
                send_msg(f'book {bname} was ordered by {name}, phone no. {phone}, operation : {choice}')
        else:
            print(f'Sorry {name} the book is not available')

    elif choice == 'sell a book':
        bname = input('Please enter the book name you want to sell: ').lower()
        price2 = int(input('Please enter the price you want others to buy your book: '))
        i_price2 = int(input('Please enter the price you want others to issue your book: '))
        money = int(input('Please enter the amount you want as income: '))
        send_msg(f'{name} wants to sell the book for Rs {money}, issue price: Rs {i_price2}, buying price: Rs {price2}')

    else:
        print('ERROR: unable to understand the operation, please try again')

