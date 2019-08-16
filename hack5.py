dist = ['ST','BĐ','BTL','CG','ĐĐ','HBT']
pop = [150300,247100,333300,266800,420900,318000]
max = 0
min = 0
for i in range(6):
    if max < pop[i]:
        max = pop[i]
        pos = i
    else:
        continue
print('The district with the largest population is: ', dist[pos], 'with', max, 'people')

for i in range(6):
    if min > pop[i]:
        min = pop[i]
        pos = i
    else:
        continue
print('The district with the smallest population is: ', dist[pos], 'with', min, 'people')
