def currency_converter(rate, euros):
    dollars = euros*rate
    return dollars

r = input("Enter a rate: ")
e = input("Enter euros: ")

print(currency_converter(float(r),float(e)))