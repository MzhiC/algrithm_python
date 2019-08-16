# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:47:56 2019

@author: 37709
"""
import time
import random
import numpy as np

#第一种方法比第二种快，但是while里面每次都要重置sort,而且有可能是【1，2，3，4，0】这样的排序需要移动很多次，第二种并不快，除非是
#后面的全部排好，例如[3,1,2,4,5,6,7,8]

#重点：list a赋值给b，即b = a，当我们用b[1]=3这种方法操作b的时候，a也会联动变化#####
#np.array转list后，操作list就不会改变原来的array了
#range转list是用  list(range ())


A= list(range(1999))
#for i in range(1):
#    A.append(random.randint(0,1))
A=np.array(A)
A[0] = 9999#将range的第一个变为3，这样对于第二种是很快的，只需要进行一次while循环
b=A.tolist()   

def bubbleSort1(ran):
    time1 = time.time()
    n = len(b)
    for i in range(n):
        for j in range(n-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]   #这一步赋值会和A联动，为什么呢？
    time2 = time.time()
    deltime = time2-time1
    return deltime


def bubbleSort2(ran):
    time1 = time.time()
    n = len(ran)
    sort = False                      
    while sort==False:
        sort = True#假设它已经排好了，假如下面的if不成立，那就真的是排好了，就会跳出while循环
        for j in range(n-1):
            if ran[j] > ran[j+1]:
                ran[j], ran[j+1] = ran[j+1], ran[j]
                sort = False#发现有没排好的，尽管调换了一次，但依然认为它还没有排好
    time2 = time.time()
    deltime = time2-time1
    return deltime


time1 = bubbleSort1(b)
c = A.tolist()
time2 = bubbleSort2(c)