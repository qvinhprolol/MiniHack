import re
colorlist = ['blue', 'red', 'teal', 'green']
locu = input('Nhập vị trí muốn xem màu: ')
vitri = int(locu)
print(colorlist[vitri-1])
for count,ele in enumerate(colorlist):
    print (count,'.',ele)
deleted_item = input('Item to delete: ')
if re.search("[0-9]", deleted_item):
    colorlist.pop(int(deleted_item))
else:
    colorlist.remove(deleted_item)
print(colorlist)

from turtle import *
colorlist2 = ['blue', 'red', 'teal', 'green']
for i in range(0,4):
    color(colorlist2[i])
    forward(100)

mainloop()
