import nltk.data
import sys
import random
def rank(str1,str2):
    words1=str1.split()
    words2=str2.split()
    count=0
    for i in words1:
        for j in words2:
            if(i.lower()==j.lower()):
                count=count+len(i)
    return count
    
def DescendingSort(r,mode):
    if(len(r)<=1):
        return r
    else:
        left=DescendingSort(r[:len(r)//2],mode)
        right=DescendingSort(r[len(r)//2:],mode)
    leftPointer=0
    rightPointer=0
    temp=[]
    while(leftPointer<len(left) and rightPointer<len(right)):
        if(left[leftPointer][mode]>right[rightPointer][mode]):
            temp.append(left[leftPointer])
            leftPointer=leftPointer+1
        else:
            temp.append(right[rightPointer])
            rightPointer=rightPointer+1
    if(leftPointer<len(left)):
        while(leftPointer<len(left)):
            temp.append(left[leftPointer])
            leftPointer=leftPointer+1
    else:
        while(rightPointer<len(right)):
            temp.append(right[rightPointer])
            rightPointer=rightPointer+1
    return temp
            

print("Enter the file names:\n (Press e to exit):")
files=[]
while(1):
    fileName=input()
    if(fileName=="e"):
        break;
    fileName=fileName.strip()
    files.append(fileName)
if(len(files)==0):
    print("No files for processing. Process aborting...")
    sys.exit()
fpOutput=open("Summary.txt","w")
for i in range(len(files)):
    fp=open(files[i],"r")
    text=fp.read()
    fp.close() 
    detector=nltk.data.load("tokenizers/punkt/english.pickle")
    text=detector.tokenize(text.strip())
    textCopy=text[:]
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
    graph=[]
    rankCount=[]
    for j in range(len(text)):
        temp=[]
        for k in range(len(text)):
            temp.append(0) #initially zero score is assigned to each edge
        graph.append(temp)
        rankCount.append([0,j])
    j=0
    while(j<len(text)):
        k=j+1
        while(k<len(text)):
            r=rank(text[j],text[k])
            graph[j][k]=r
            graph[k][j]=r
            k=k+1
        j=j+1
    for j in range(len(text)):
        rankCount[j][0]=sum(graph[j])
    print(textCopy)
    rankCount=DescendingSort(rankCount,0)
    output=DescendingSort(rankCount[:len(text)//5],1)
    fpOutput.write("SUMMARY : %s \n"%str(i+1))
    
    for j in range(len(text)//5):
        fpOutput.write(textCopy[output[len(text)//5-j-1][1]])
    fpOutput.write("\n-----------------------------------------------------------")   
        
fpOutput.close()

# for formatting the Summary
file = open("Summary.txt","r+")
f = file.read().split(".")
print(len(f))
p = []
for i in f:
    n = i.replace("\n", " ")
    p.append(n+".\n")
file = open("Summary.txt","w")
file.write("\n".join(p))
file.close()

        
    
    
        
        
    
    
    
    
    

