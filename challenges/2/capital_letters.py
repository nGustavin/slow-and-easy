##Capital indexes

##Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
##For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

super_string = "I dont Know what to WRite but thats ok!"

def capital_letters(string: str)-> list:
  """
   This function get's a string and return the index of all capital letters on it
  """
  capital_letters_list = []
  for idx, letter in enumerate(string):
    if(letter.isupper()):
      capital_letters_list.append(idx)
    else:
      pass
  return capital_letters_list
