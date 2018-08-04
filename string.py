# Variable is called data, which is made up of 'product', price & condition.
data = 'Playstation 4 Pro | £350 | New'

#data.index is saying from the variable data, index the | from the string.
data.index('|')

#variable 'product' is equal to variable 'data', [: is saying anything before the colon you want up to data.index('|')] so this will go "'Playstation 4 Pro' |"
product = data[:data.index('|')]
price = data[0:26]
condition = data[27:]

print (product, price, condition)


# Variable is called data, which is made up of 'product', price & condition.
data = 'Playstation 4 Pro | £350 | New'

#data.index is saying from the variable data, index the | from the string.
data.index('|')

#variable 'product' is equal to variable 'data', [: is saying anything before the colon you want up to data.index('|')] so this will go "'Playstation 4 Pro' |"
product = data[0:26]

print (product)



greeting = "Hello, How the fuck are you doing bruh?"

## [START:STOP:STEP] the brackets 0 is saying the first letter, : is up to, -1 is up to the end of the string, 2 is the step so this gets every 2nd word from the string.
greeting[0:-1:2]

print(greeting[0:-1:2])


hello = "Hello"

## This will reverse the sting by doing [::-1]
print(hello[::-1])



##.split can be used to split strings, this takes the string 'what-is-going-on' and splits it by the '-'.
greeting = "what-is-going-on".split('-')



##
data = "Playstation 4 | 350 | New"
data.split('|')
#['Playstation 4 ', '150', 'New'] would appear.

details = data.split('|')
#details will now reveal the same as above.

#by setting the variables = to details and adding [0],[1] or [2] breaks the list down.
product = details[0]
price = details[1]
condition = details[2]

#Now typing product, price or condition will match the correct item from the the variable 'data'
# product
# price
# condition

# the more efficant way to do it however is
product, price, condition = data.split('|')

#Now typing product, price or condition will match the correct item from the the variable 'data'
# product
# price
# condition


##.append can be used to add something to an existing string.
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7)
#now, when callings the numbers variable it'll display [1, 2, 3, 4, 5, 6, 7]

#you can also loop numbers by
for i in range(10):
    print(i)
#this will start printing numbers up to 10, so you can use this to append numbers also

# after for you can put whateve name you want as this is a variable.
for number in range(7, 20):

# this will now add numbers 7 through 20 to the 'Numbers' variable so if we type numbers) it'll display them all
    numbers.append(number)
    
