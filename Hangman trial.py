import random

r=open("words.txt","rt")
content=r.readlines()
word=random.choice(content)

turns=25
fail=0
while turns>=0:
    split=list(word)
    g=str(input("guess a character: "))
    for char in split:
        if g==char:
            print(g)
            split=split.replace('__',g)
        else:
            print('__')
            fail+=1
    turns-=1





















"""guess=str(input("guess a character: "))
for char in word:
    if guess==char:
        print(char)
    else:
        print('__')
    turns-=1"""
        
