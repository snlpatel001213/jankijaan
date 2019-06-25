import random
def mergesort(array:list, p, r):
    if r-p > 1:
        q = (p+r)//2
        mergesort(array, p, q)
        mergesort(array,q,r)
        merge(array,p,q,r)

def merge(array:list,p,q,r):

    lowHalf = array[p:q]
    highHalf = array[q:r]
    i = 0
    j = 0
    k = p

    while(p+i < q and q+j < r):
        if lowHalf[i] <= highHalf[j]:
           array[k] =  lowHalf[i]
           i = i + 1
        else:
            array[k] = highHalf[j]
            j = j + 1
        k = k + 1

    while (p+i<q):
        array[k] = lowHalf[i]
        i = i + 1
        k = k + 1
    while (q+j<r):
        array[k] = highHalf[j]
        j = j + 1
        k = k + 1
    print(array)

array = [random.randint(1,10000) for i in range(0,1000000)]
print(array)
print(mergesort(array,0, len(array)))
print(array)