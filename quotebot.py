# Kalki Quote bot V 1.0 Created By MaragthamDevelopers
# Licensed under MIT license.

import random
rnd=random.randint(1,15)
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()
