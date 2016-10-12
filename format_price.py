import re
import locale


def format_price(price):
    price = str(price).replace(',', '.')
    price = re.sub(r'\s', '', price)
    price = float(price)

    loc = locale.getlocale()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    price = locale.currency(price, grouping=True)
    price = re.sub(r'\.00$', '', price)
    price = price.replace('$', '')
    price = price.replace(',', ' ')

    locale.setlocale(locale.LC_ALL, loc)
    return price


if __name__ == '__main__':
    while True:
        price = input('Enter the price: ')
        if not price:
            break
        try:
            print(format_price(price))
        except ValueError:
            print('Incorrect number.')
