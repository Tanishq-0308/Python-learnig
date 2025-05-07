weather= input("Enter weather: ")

if weather == 'Sunny':
    activity= 'Go for a walk'
elif weather == 'Rainy' or weather == 'rainy':
    activity = 'Read a book'
elif weather == 'Snowy':
    activity = 'Build a snowman'
else:
    activity = 'Tell correct Weather'

print(activity)