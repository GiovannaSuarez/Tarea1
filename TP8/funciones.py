
#1--------------------
def num_len(num):
    if num-int(num)==0:
        num=str(int(num))
        num_list=list(num)
        if len(num_list)==1:
            return 1
        else:
            
            return len(num_list)
    else:
        num=str(num)
        num_list=list(num) 
        return len(num_list)-1
#2--------------------------------------
def power_of(a,b,n=0):
    if a==pow(b,n):

        return True
    elif n>b:

        return False
    else:

        return power_of(a,b,n+1)
#3---------------------------------------
def frequency(a,b,c=0):
    if b==a[0:len(b)]:
        return [c]+frequency(a[1:],b,c+1)
    elif len(b)>=len(a):
        return []
    else:
        return frequency(a[1:],b,c+1) 
#4------------------------------------ 
def even(num,i=0):
    if num==i:
        return " es par"
    else:
        i+=1
        return odd(num,i)


def odd(num,i):
    if  num==i:
        return " es impar"
    else:
        i+=1
        return even(num,i)
#5----------------------------
def max_number(numbers,i=0):
    if i==(len(numbers)-1):
        return numbers[i]
    elif numbers[i]>numbers[i+1]:
        temp=numbers[i]
        numbers[i]=numbers[i+1]
        numbers[i+1]=temp
        i+=1
        return max_number(numbers,i)
    else:
        i+=1
        return max_number(numbers,i)
#6--------------------
def replicate(repli_list,repli_list_og,repli_times):
    repli_list=list(repli_list)
    if repli_times<2:
        return repli_list
    else:
        for i in repli_list_og:
            repli_list.append(i)
        repli_times-=1
        repli_list=replicate(repli_list,repli_list_og,repli_times)
    return repli_list

#7-----------------------------
#K(n, p) = 1*p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
def K(n,p,i):
    i+=1
    if i==n:
        return n*p
    else:
        return i*p+K(n,p,i)
#8-------------------------------------
#1
#11
#121
#1331
#14641

def pascal(f,c):
    if c==0 or c==f: #Si esto se cumple significa que estanos en las equinas y por tanto los valores son iguales a 1
        return 1
    else:
        value=pascal(f-1,c-1)+pascal(f-1,c) #Esto permina sumar los elementos contiguos volviendo una fila hacia arria en ambos y volviendo una comlumna en solo uno
        return value
#9.	-------------------------------------

def combinations(chars,k,final):
    if k==0:
        print(final)
        return
    else:
        for i in chars:
            combinations(chars,k-1,final+i)    

#10-----------------
def paper_size(A,i,width,length):
    
    if i==A:
        return[width,length]
    elif i%2==0:
        i+=1
        length=int(length/2)
        return paper_size(A,i,width,length)
    else:
        i+=1
        width=int(width/2)
        return paper_size(A,i,width,length)
    