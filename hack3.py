numlist = [5, 1, 8, 92, -1, 30]
search_num = int(input('Enter a number: '))
for i in range(0,6):
    if search_num == numlist[i]:
        print('Found, position', i+1)
        break
    if i == 5:
        print('Not found in the list')
        break
    else:
        continue
    
    
print(sum(numlist))
tong = 0
for i in range(6):
    tong = tong + numlist[i]
print(tong)

numbers = input("Enter numbers, seperated by a space: ")
split = numbers.split(" ")
tongxd = 0
for n in split:
    tongxd = tongxd + int(n)
print(tongxd)
