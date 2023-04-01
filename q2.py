# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:13:11 2023

@author: dor ingber 316080159
"""



def revword(word):
    word=word[len(word)::-1] 
    word = word.lower()
    return word

def countword():
    counter=1
    PATH = "C:\\Users\\user\\Desktop\\dor-university\\3rd_year\\2_simester\\data_maining\\matala1\\text.txt"
    fh = open(PATH)
    for line in fh:
        lineWords = line.split()
        if len(lineWords) == 1:#נתון שהקובץ מכיל רק בשורה הראשונה מילה בודדת
            word = lineWords[0]
            continue
        for i in lineWords:
            if revword(i)==word:
                counter +=1
    return counter

print(countword())