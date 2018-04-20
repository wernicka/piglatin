# piglatin

print "Welcome to Amanda\'s Pig Latin Translator"

pyg = 'ay'
way = 'way'

original = raw_input('Enter a word: ')

word = original.lower()
if len(word) > 0 and word.isalpha():
    
  if word[0] in ("a","e","i","o","u"):
    new_word = word + way
    print new_word
  
  else:
    word = word[1:] + word[0]
    while word[0] not in ("a","e","i","o","u","y"):
      word = word[1:] + word[0]
    new_word = word + pyg
    print new_word
     
else:
  print "Type a real word! Just one word, no spaces. Try again"
