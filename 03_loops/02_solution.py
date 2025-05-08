number = int(input('enter number'))
sum_count =0

for i in range(1, number + 1):
    if (i%2 == 0):
        sum_count= sum_count + i
print(sum_count)
