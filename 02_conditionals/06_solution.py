distance = int(input("Enter distance in km: "))

if distance < 3:
    print('Walk')
elif distance <= 15:
    print('Bike')
else:
    print('Car')