
with open('storeSales.txt') as arquive:
    text = arquive.read()
text_list = text.split('\n')

invoicing = 0

#Delete file first line
text_list = text_list[1:]

#For each line in the file
for i in text_list:
    position_sc = i.find(';')
    value = float(i[position_sc + 1:])
    invoicing += value

print(invoicing)
#Add the value that comes after the ;    





   

