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
que = {'0','0'}

with open(resource_path('resource\\words.txt'),'r', encoding='UTF-8') as a:
    word = a.read().splitlines()
    for i in word:
        words.append(i)
with open(resource_path('resource\\wordsmean.txt'),'r', encoding='UTF-8') as b:
    mean = b.read().splitlines()
    for j in mean:
        answer.append(i)
question = dict(zip(words,answer))
for i in range(1,len(words)+1):
    uanswer = input()
    if uanswer is question[words[i]]:
        print('O')
    else:
        print('X')