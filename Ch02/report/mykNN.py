#-*- coding:utf-8 -*-
from numpy import *

def getData(filename):
    f=open("./"+filename,'r')
    lines=f.readlines()
    f.close()
    vector=zeros((1,3))
    dataV=zeros((len(lines),3))
    label=zeros((len(lines),1))

    index=0
    for line in lines:
        vector=(line.split("\t")[:3])

        for i in range(3):
            vector[i]=float(vector[i])
        dataV[index,:]=vector
        label[index]=line.split("\t")[3]
        index+=1
    
    return dataV,label

def normalData(dataV):
    minAttri=dataV.min(0)
    maxAttri=dataV.max(0)

    r=maxAttri-minAttri

    dataV=dataV-minAttri*ones((dataV.shape[0],1))

    dataV=dataV/r*ones((dataV.shape[0],1))

    return dataV



def predict(vect,dataV,label,k):
    newV=vect*ones((dataV.shape[0],1))

    disV=dataV-newV
    
    disV=disV**2
    disM=zeros((dataV.shape[0]))
    

    for i in range (dataV.shape[0]):
        disM[i]=sum(disV[i,:])
    disM=disM**0.5

    queryIndex=disM.argsort()

    
    numberOfEach=zeros((3))



    for i in range(k):
        numberOfEach[(int(label[queryIndex[k]])-1)]+=1

        
    
    
    result=numberOfEach.argsort()

    

   

    
    return result[2]+1


if __name__ == '__main__':

    dataV,label= getData("datingTestSet2.txt")
    #print dataV
    dataV=normalData(dataV)

    vect=dataV[0]

    testV=dataV[700:999]

    dataV=dataV[0:699]

    testLabel=label[700:999]

    label=label[0:699]

    index=0
    error=0
    for vect in testV:
        if(predict(vect,dataV,label,k=7)!=testLabel[index]):
            error+=1
        index+=1
        
    errorrate=(float(error)/300)

    print "error number: ",error
    print  "error rate: %.6f"%errorrate



