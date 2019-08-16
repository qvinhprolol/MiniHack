num = input('Type the numbers, seperated by comma: ')
numlist = num.split(",")
output = []
for number in numlist:
    if int(number)%2==0:
        output.append(number)
print('All even numbers are: ', end='')
for i in range(len(output)):
    print(output[i],end=' ')