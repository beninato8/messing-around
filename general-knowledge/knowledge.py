#questions from this article https://link.springer.com/article/10.3758/s13428-012-0307-9
#as mentioned in this podcast http://www.hellointernet.fm/podcast/123
#data scraped from here: https://www.reddit.com/r/HelloInternet/comments/bkczlx/complete_list_of_general_knowledge_questions/

import pandas as pd

data = pd.read_csv('knowledge.csv')['Question and Correct Response'].values.tolist()[1:]

class Question:
    def __init__(self, q, a):
        self.q = q
        self.a = a

# print(data)
l = []
for x in data:
    s = x.split(' (')
    a = s[-1][:-1]
    q = ' '.join(s[:-1])
    l.append(Question(q, a))

score = 0
for i, x in enumerate(l):
    q = x.q
    a = x.a.lower()
    q = q.lower().split(' ')
    q[0] = q[0].title()
    q = ' '.join(q)
    print(f'Question {i+1}: {q}')
    s = input()
    if s == a:
        print("Correct.", end=' ')
        score += 1
    else:
        print(f"Incorrect. The correct answer was {a}.", end=' ')
    print(f'You are {score} for {1+i}, {score*100/(i+1):.0f}% accurate')
    print()

