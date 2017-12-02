import pandas as pd
import nltk
from nltk.corpus import wordnet
import random #to randomly select few sentence
import json #to get the json format values in the answer

class database:
    def __init__(self):
        self.j={} #this is where we will store all the values
        self.synonyms=["What is the synonyms of ","Tell me word similar to"]
        self.antonyms=["What is the antonyms of","Word opposite to "]
        df= pd.read_csv("val.csv")
        self.word=df['WORD'].tolist()
        self.dict={}
        for i in self.word:
            self.dict[i]=True
    def func(self):
        map={}
        def prep(word):
            synonyms = []
            antonyms = []
            syns=wordnet.synsets(word)
            for syn in syns:
                for l in syn.lemmas():
                    synonyms.append(l.name())
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())
                        if len(syns)!=0 and len(syns[0].examples())!=0:
                            print(set(synonyms))
                            syn=set(synonyms)
                            ant=set(antonyms)
                            if(word in syn):
                                syn.remove(word)
                            #syn=set(synonyms).remove(word)
                            return list(ant),list(syn),"example sentence of:"+word+" "+random.choice(syns[0].examples())
                        else:
                            syn=set(synonyms)
                            ant=set(antonyms)
                            if(word in syn):
                                syn.remove(word)
                            return list(ant),list(syn),""
        for i in self.word:
            map[i]=prep(i)
        return map

    def question(self):
        map=self.func()
        question=[]
        answer=[]
        end=len(self.word)
        follow=[]
        for idx,word in enumerate(self.word):
            l=list(range(1,idx))+list(range(idx+1,end))
            #print(l)
            for i in self.synonyms:
                ans=[]
                if(map.get(word)!=None and len(map.get(word)[1]))!=0:
                    question.append(i+" "+word)#this is to prepare sentence
                    ans.append("|".join(map.get(word)[1])) #this is to put correct answer in the question
                    for j in random.sample(l,2):
                        ans.append(self.word[j])
                    answer.append(ans)
                    follow.append(map.get(word)[2])
            for i in self.antonyms:
                ans=[]
                if(map.get(word)!=None and len(map.get(word)[0]))!=0:
                    question.append(i+" "+word)#this is to prepare sentence
                    ans.append("|".join(map.get(word)[0])) #this is to put correct answer in the question
                    for j in random.sample(l,2):
                        ans.append(self.word[j])
                    answer.append(ans)
                    follow.append(map.get(word)[2])
        return question,answer,follow

    def json_create(self):
        self.j={}
        self.j["answers"]=[]
        self.j["questions"]=[]
        self.j["followUps"]=[]
        self.j["dictionary"]=self.dict
        p=self.question()
        rand=list(range(1,len(p[0])))
        random.shuffle(rand)
        for i in rand:
            self.j["answers"].append(p[1][i])
            self.j["questions"].append(p[0][i])
            self.j["followUps"].append(p[2][i])
        return self.j

if __name__=="__main__":
    dat=database()
    dat.json_create()
    with open('questions.json', 'w') as outfile:
        json.dump(dat.j, outfile)
