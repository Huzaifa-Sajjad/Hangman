def filter(index,letter):
    for x in possible_words.copy():
      if x[index] == letter:
        possible_words.remove(x)

data_set = open("data.txt","r")
words = []
possible_words = []
word = []
RESULT = False
for data in data_set:
  if data[-1] == "\n":
    words.append(data[0:-1])
  else:
    words.append(data)

word_length = int(input("How many letters are in the word > "))

for w in words:
  if len(w) == word_length:
    possible_words.append(w)

counter = word_length

while counter:
  word.append("__")
  counter -= 1

TOTAL_TRIES = 5
tries = 0

counter = int(input("How many letters would you tell me? > "))
while counter:
  print(word)
  letter = input("Give me a letter > ".lower())
  index = int(input("Where to place it in the word? > ")) - 1
  for x in possible_words.copy():
    if x[index] != letter:
      possible_words.remove(x)
  word[index] = letter
  counter-= 1

print(possible_words)

while TOTAL_TRIES:
  print("{} tries left".format(TOTAL_TRIES))
  print(word)
  for x,l in enumerate(word):
    if l == "__":
      index = x
      break
  guess = possible_words[0]
  q = input("Is the letter {} ? Y/N > ".format(guess[index]))
  if q.lower() == "n":
    filter(index,guess[index])
    TOTAL_TRIES -= 1
  else:
    word[index] = guess[index]
    if guess == "".join(word):
      print("".join(word))
      RESULT = True
      break

if RESULT:
  print("I WON")
else:
  print("YOU LOST")

  