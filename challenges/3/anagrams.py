# Anagrams

# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(first_word, second_word):
  anagram = True
  for letter in first_word:
    if anagram == False:
      return False
    amount_in_first = first_word.count(letter)
    for letters in second_word:
      amount_in_second = second_word.count(letter)
    if amount_in_first == amount_in_second:
      next
    else:
      anagram = False
      
  return anagram

print(is_anagram("test", "less"))