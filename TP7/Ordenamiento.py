import random
import math

def fill_array_1D(A,array_dimesions):
    for i in range(array_dimesions):
        A[i]=random.randint(1,51)
    return A 

#Tambien funciona con listas de strings
def bubble_sort(A):
    for p in A:
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp  
    return A  
#Tambien funciona con listas de strings
def selection_sort(A):
    lesser_value=1000
    for p in range(len(A)-1):
        lesser_value=A[p]
        lesser_value_pos=p
        for i in range(p+1,len(A),+1):
            if A[i]<lesser_value:
                lesser_value=A[i]
                lesser_value_pos=i
        if lesser_value_pos!=p:
            temp=A[p]
            A[p]=A[lesser_value_pos]
            A[lesser_value_pos]=temp
    return A
#Tambien funciona con listas de strings
def insert_sort(A):
    for p in range(1,len(A)):
        temp=A[p]
        i=p-1
        while i>=0 and temp<A[i]:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=temp
    return A
#Tambien funciona con listas de strings
def merge_sort(A):
    if len(A)>1:

        u=math.trunc(len(A)/2)
        A_left=A[0:u]
        A_right=A[u:len(A)]

        merge_sort(A_left)
        merge_sort(A_right)
        i=0
        p=0
        j=0
        while i<len(A_left) and p<len(A_right): 
            if A_left[i]<A_right[p]:
                A[j]=A_left[i]
                i=i+1
            else:
                A[j]=A_right[p]
                p=p+1
            j=j+1
        while i<len(A_left):
            A[j]=A_left[i]
            i=i+1
            j=j+1
        while p<len(A_right):
            A[j]=A_right[p]
            j=j+1
            p=p+1
    return A
#Solo funciona con numeros
def countSort(A):
    A_range=-1
    for i in A:
        if i>A_range:
            A_range=i

    final_A=list (range(len(A)))
    count=list(0 for i in range(A_range+1))
    for i in A:
        count[i]+=1
    
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(len(A)):
        final_A[count[A[i]]-1]=A[i]
        count[A[i]]-=1
    return final_A
#Solo funciona con numeros
def countSortNegative(A):
    A_posi=[]
    A_neg=[]
    new_A_neg=[]
    for i in A:
        if i>=0:
            A_posi.append(i)
        else:
            A_neg.append(i)
    for i in range(len (A_neg)):
        A_neg[i]*=-1
    A_posi=countSort(A_posi)
    A_neg=countSort(A_neg)
    for i in range((len(A_neg)-1),-1,-1):
        new_A_neg.append(A_neg[i])
    for i in range(len (new_A_neg)):
        new_A_neg[i]*=-1
    for i in A_posi:
        new_A_neg.append(i)
    return new_A_neg






