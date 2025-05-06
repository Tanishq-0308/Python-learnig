age = int(input("Enter age: "))
day = input("Enter day:")

price = 12 if age >= 18 else 8

if day == 'wednesday':
    price -= 2

print("Ticket price for you is $",price)