order_size = input('Tell the order size: ')
espresso= input('Want Extra shot of espresso?: ')

if espresso == 'yes':
    coffee= order_size + ' coffee with extra shot of espresso'
else:
    coffee = order_size +' coffee without extra shot of espresso'

print(coffee)