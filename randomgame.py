import os
import random
import string
import time
text_file = open("games.txt", "r")
games = text_file.read().split('\n')
print ("Loading games")
for items in games:
    print(items)
print ("Selected game:")
selectedgame = random.choice(games)
print(selectedgame)
os.startfile("%s" % selectedgame)
time.sleep(3000)
