# Kalki Quote bot v1.1 Created By MaragthamDevelopers
# Licensed under MIT license.

import random
rnd=random.randint(1,20)
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()
