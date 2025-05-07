pet_species= input('What is the species of Pet: ')
age = int(input('what is the age? :'))

if pet_species == 'Dog':
    if age < 2:
        food= 'Puppy food'
    else:
        food= 'Adult dog food'
elif pet_species == 'Cat':
    if age > 5:
        food= 'Senior cat food'
    else: 
        food= 'Kitten food'
else :
    print("Don't know about this animal")

print(food)