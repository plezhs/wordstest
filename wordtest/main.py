import random
import os
import sys

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)

condition = True
words=[]
answer = []
num=0

with open(resource_path('resource\\words.txt'),'r', encoding='UTF-8') as a:
    word = a.read().splitlines()
    for i in word:
        words.append(i)
with open(resource_path('resource\\wordsmean.txt'),'r', encoding='UTF-8') as b:
    mean = b.read().splitlines()
    for j in mean:
        answer.append(j)
question = dict(zip(words,answer))
random.shuffle(words)
for l in range(1,len(words)+1):
    uanswer = input(words[num]+'\n')
    ranswer = str(question[words[num]])
    if uanswer == ranswer:
        print('O')
    else:
        print('X')
    num+=1