import os

comm = 0

while (comm == 0):
    print("Enter an option: \n1) Wiki Bot \n2) Movie Bot \n3) Exit")
    inp = int(input())
    if(inp == 3):
        comm = 1
        continue
    if(inp == 1):
        os.system('python3 wikibot.py')
    if(inp == 2):
        os.system('python3 moviebot.py')