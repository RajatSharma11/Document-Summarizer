from tkinter import *
import nltk.data
import sys
import os
import random

def rank(str1,str2):
    words1 = str1.split()
    words2 = str2.split()
    count=0
    for i in words1:
        for j in words2:
            if(i.lower() == j.lower()):
                count = count + len(i)
    return count
    
def DescendingSort(r,mode):
    if(len(r) <= 1):
        return r
    else:
        left=DescendingSort(r[:len(r)//2],mode)
        right=DescendingSort(r[len(r)//2:],mode)
    leftPointer = 0
    rightPointer = 0
    temp = []
    while(leftPointer < len(left) and rightPointer < len(right)):
        if(left[leftPointer][mode] > right[rightPointer][mode]):
            temp.append(left[leftPointer])
            leftPointer = leftPointer + 1
        else:
            temp.append(right[rightPointer])
            rightPointer = rightPointer + 1
    if(leftPointer < len(left)):
        while(leftPointer < len(left)):
            temp.append(left[leftPointer])
            leftPointer = leftPointer + 1
    else:
        while(rightPointer < len(right)):
            temp.append(right[rightPointer])
            rightPointer = rightPointer + 1
    return temp
master = Tk()
def quit():
    master.destroy()

def show_entry_fields():
    input_path = e1.get()
    output_path = e2.get()
    files = next(os.walk(input_path))[2]
    for i in range(len(files)):
        output_filename = output_path + "/" + files[i]
        fpOutput = open(output_filename ,"w")
        fp = open(input_path+"/"+files[i],"r")
        text = fp.read()
        fp.close()
        detector = nltk.data.load("tokenizers/punkt/english.pickle")
        text = detector.tokenize(text.strip())
        textCopy = text[:]
        for j in range(len(text)):
            #for endings
            text[j]=text[j].replace("."," ")
            text[j]=text[j].replace("?"," ")
            text[j]=text[j].replace("!"," ")
            #for non-terminal punctuation marks
            text[j]=text[j].replace(","," " )
            text[j]=text[j].replace(";"," ")
            text[j]=text[j].replace(":"," " )
            text[j]=text[j].replace("-"," " )
            text[j]=text[j].replace("("," " )
            text[j]=text[j].replace(")"," " )
            text[j]=text[j].replace("{"," " )
            text[j]=text[j].replace("}"," " )
            text[j]=text[j].replace("\""," ")
            text[j]=text[j].replace("\'"," " )
            text[j]=text[j].replace("/"," ")
            text[j]=text[j].replace("\n"," " )
            text[j]=text[j].strip()
        graph = []
        rankCount = []
        for j in range(len(text)):
            temp = []
            for k in range(len(text)):
                temp.append(0) #initially zero score is assigned to each edge
            graph.append(temp)
            rankCount.append([0,j])
        j = 0
        while(j < len(text)):
            k = j+1
            while(k < len(text)):
                r = rank(text[j],text[k])
                graph[j][k] = r
                graph[k][j] = r
                k = k+1
            j = j + 1
        for j in range(len(text)):
            rankCount[j][0]=sum(graph[j])
        rankCount = DescendingSort(rankCount,0)
        regulator = 4
        output=DescendingSort(rankCount[:len(text)//regulator],1)
        
        for j in range(len(text)//regulator):
            fpOutput.write(textCopy[output[len(text)//regulator - j - 1][1]])  
        fpOutput.close()
        # for formatting the Summary
        file = open(output_filename,"r+")
        f = file.read().split(".")
        p = []
        for i in f:
                n = i.replace("\n", " ")
                p.append(n+".\n")
        file = open(output_filename,"w")
        file.write("\n".join(p))
        file.close()
    quit()


master.geometry("400x250")
master.title('Document Summarizer')
master.resizable(width=False, height=False)
master.configure(bg="#a1dbcd")
Label(master, text="Input File Path",bg="#a1dbcd",height = 3,width = 30).grid(row=0)
Label(master, text="Output File Path",bg="#a1dbcd",height = 3,width = 30).grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Summarize', command=show_entry_fields,fg="#a1dbcd",bg="#383a39", height=2, width=15).grid(row=4, column=1, sticky=W, pady=4)

mainloop( )
