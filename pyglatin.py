pyg = 'ay' # 'ay' added to the end of the word.

original = input('Enter a word: ') # input to create a user required action, in this case to enter a word.

if len(original) > 0 and original.isalpha(): # if the character length of the variable 'original' (which is for the user input) is greater than 0 AND the variable 'original' doesn't contain any non-letter character.
  
  word = original.lower() # then new variable 'word' is equal to variable orignal (user input) in lower case letters.
  
  first = word[0] # new variable 'first' to index the first letter of the word created.
  
  new_word = word + first + pyg # new variable 'new_word' to concatenate other variables together, so new_word is equal to word + first + pyg so this will take the word, add the first letter to the end and then add yg to the end to create the word in 'pig latin'.
  
  new_word = new_word[1:len(new_word)] # new variable 'new_word' is equal to new_word from letter position 1 (which is the 2nd letter as letter positions start at 0) so the word starts from the 2nd letter up to the rest of the length of the new word, can also do new_word = new_word[1:4] and this would do from the second letter to the 5th letter but in this case we only want to get rid of the first letter and keep the remaining letters.
  
  print (new_word) # as the variable 'new_word' is a combonation of variables, word + first + pyg this will print the word you type but move the first letter to the end so 'hello' will be 'elloh' and then it'll add ay on the end so will  be 'ellohay' which is then translated to pig latin.
  
else: #otherwise
  
    print ('You didn\'t enter a word!') # this outcome is if the user just presses enter without typing a word, or types a word that contains non-letter characters due to the .isalpha above.
