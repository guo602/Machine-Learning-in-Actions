#coding:utf-8

#__author__ = 'burger'

from math import log
import operator
import treePlotter as dtPlot


LL={'age':1,'prescript':1,'astigmatic':1,'tearRate':1}
def loadData():
    filename="lenses.txt"
    label=['age', 'prescript', 'astigmatic', 'tearRate']
    f=open("./"+filename,'r')
    lines=f.readlines()
    f.close()

    data=[]
    for line in lines:
        vector=line.strip('\n').split("\t")
        data.append(vector)
    return data,label





def calcuEntropy(data):
    result=[re[-1] for re in data]
    result=set(result)
    c=[]
    for i in range(len(result)):
        c.append(0)

    rdict=dict(zip(result,c))
    
    amount=len(data)

    for d in data:
        for r in result:
            if r==d[-1]:rdict[r]+=1
    
    entropy=0



    for r in (rdict):
        entropy-=float(rdict[r])/amount*log(float(rdict[r])/amount,2)
    return entropy

def diviData(data,fearture,label):
    fearturei=label.index(fearture)
    diData=[]

    dls=[re[fearturei] for re in data]
    dls.sort()
    dls=set(dls)

   

    data.sort(key=lambda x:x[fearturei])
 
    di=[]

    index=0

    lie=[x[fearturei] for x in data]  
    lie.sort()
    for dl in dls:
        di.append(lie.index(dl))
    di.sort()

    dls=list(dls)
    dls.sort()
    
    index=0
    print "index: \n",di
    print "datas \n",data
    for dl in dls:
        if index==len(dls)-1:
            diData.append(data[int(di[index]):len(data)])
        else:

            diData.append(data[int(di[index]):int(di[index+1])])

        print "didata i :\n",diData[index]
        index+=1

    return diData,dls
    
        


def findbestfeature(data,label):
    
    feature=''
    minE=float("inf")

    totalLength=len(data)
    
    for f in label:
        # if L[f]==0:continue
        dvidata,dls=diviData(data,f,label)
        E=0
        for d in dvidata:
            tempLength=len(d)
            E+=float(tempLength)*calcuEntropy(d)/totalLength
        print "E ",E
        print "Feature ",f
        if E<=minE:
            minE=E
            feature=f
    # L[feature]=0
    return feature
        

def createTree(data,label):
   
    re=[re[-1] for re in data]
    re.sort()
    if re[0]==re[len(re)-1]:return  re[0]
    
    else:
        bestfeature=findbestfeature(data,label)

        print "data : ",data
        print "bestfeature : ",bestfeature
        
        dData,dls=diviData(data,bestfeature,label)

       
        tree={bestfeature:{}}


        for i in range(len(dls)):
            if dData[i]==None:continue
            elif len(dData[i])==0:continue
            tree[bestfeature][dls[i]]=createTree(dData[i],label)

    return tree



def test():
    data,label=loadData()
   

   

    tree=createTree(data,label)
    print tree

    #api
    dtPlot.createPlot(tree)

