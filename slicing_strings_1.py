# Variable is called data, which is made up of 'product', price & condition.
data = 'Playstation 4 Pro | £350 | New'

#data.index is saying from the variable data, index the | from the string.
data.index('|')

#variable 'product' is equal to variable 'data', [: is saying anything before the colon you want up to data.index('|')] so this will go "'Playstation 4 Pro' |"
product = data[:data.index('|')]
price = data[18:26]
condition = data[27:]

#print (product,price,condition)

print(data[data.find('|'):data.find('|', 18)])
