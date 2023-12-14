import json
import random
import os
import sys

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)

# with open(resource_path('resource\\words.txt'),'r', encoding='UTF-8') as a:
#     word = a.read().splitlines()
#     for i in word:
#         words.append(i)
# with open(resource_path('resource\\wordsmean.txt'),'r', encoding='UTF-8') as b:
#     mean = b.read().splitlines()
#     for j in mean:
# #         answer.append(j)
# question = dict(zip(words,answer))
# with open(resource_path(f'unit\\{unitnum}.json'),'w',encoding='UTF-8') as jsonfile:
#     json.dump(question,jsonfile,indent=2,ensure_ascii=False)

words=[]
answer = []
num=0
unitnum = input("단원을 선택해주세요\n")

def jsontodict(unitnumber):
    with open(resource_path(f'unit\\{unitnumber}.json'),'r',encoding='UTF-8') as jsondict:
        answersheet = json.load(jsondict)
    return answersheet

def dicttojson(unitnumber,answerdict):
    with open(resource_path(f'unit\\{unitnumber}.json'),'w',encoding='UTF-8') as dictjson:
        json.dump(answerdict,dictjson)

try:
    question = jsontodict(unitnum)
except:
    print("단원이 존재하지 않습니다")

words = list(question.keys())
random.shuffle(words)
for l in range(1,len(words)+1):
    uanswer = input(words[l]+'\n')
    ranswer = str(question[words[l]])
    if uanswer == ranswer:
        print('O')
    else:
        print('X')
        print(ranswer)
