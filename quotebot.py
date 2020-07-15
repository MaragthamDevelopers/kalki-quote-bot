# Kalki Quote bot v1.3 Created By MaragthamDevelopers
# Licensed under MIT license.

import random
rnd=random.randint(1,28)
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()
