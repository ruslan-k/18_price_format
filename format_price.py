import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='Convert price to readable format.')
    parser.add_argument('price', help='Price to format')
    args = parser.parse_args()

    return args


def convert_string_to_float_or_int(string):
    try:
        str_as_num = int(string)
        return str_as_num
    except ValueError:
        try:
            str_as_num = float(string)
        except ValueError:
            raise ValueError('Given value cannot be converted into a number')
    return str_as_num


def format_price(price):
    if isinstance(price, str):
        price = convert_string_to_float_or_int(price)

    if isinstance(price, int):
        return '{:,.0f}'.format(price).replace(',', ' ')
    elif isinstance(price, float):
        return '{:,.2f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    args = get_arguments()
    print(format_price(args.price))
