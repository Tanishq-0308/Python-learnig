password= input("Enter password: ")

if len(password) < 6:
    strength= 'Weak'
elif len(password) <=10:
    strength= 'Medium'
else:
    strength= 'Strong'

print(strength)