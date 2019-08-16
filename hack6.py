dist = ['ST','BĐ','BTL','CG','ĐĐ','HBT']
pop = [150300,247100,333300,266800,420900,318000]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
pop_density=[]
average_density = 0
for i in range(6):
    density = pop[i] / area[i] / 1000000
    pop_density.append(density)
    average_density = average_density + density/6
print(pop_density)
print('The average population density is: ',average_density, 'people per square metre')

