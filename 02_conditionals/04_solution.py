fruit= input("Enter fruit: ")

if fruit != 'Banana':
    print("I don't have information about this fruit")
    exit()
color= input("Color of the fruit: ")

if fruit == 'Banana':
    if color == 'Green':
        print('Unripe')
    elif color == 'Yellow':
        print('Ripe')
    elif color == 'Brown':
        print('Overripe')
    else:
        print("Don't know about this color")