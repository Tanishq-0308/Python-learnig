name= 'python'
reversed_=''

# for i in range(len(name)-1,-1, -1):
#     reversed_= reversed_ + name[i]
#     # print(name[i])
# print(reversed_)

for char in name:
    reversed_ = char + reversed_
print(reversed_)