#Dictonaries
#DICT[key] --> value
# using { type of bracket we make a DICT - {key1: value1, key2: value 2} Ben is the KEY, the number is the VALUE.


#(Variable = DICT bracket { 'Ben' is the KEY, list bracket ['phone number', 'email'] DICT bracket }
phone_book = {
    'Ben': ['07803545678', 'ben@ben.com'],
    'Joe': ['07805432167', 'joe@joe.com'],
    'Mac': ['07803543468', 'mac@mac.com']
    }

#print 'name of variable' ['Ben'] [0], this will display the phone number, [1] will show the email.
print(phone_book['Ben'][0])
print(phone_book['Joe'][1])
print(phone_book['Mac'])
