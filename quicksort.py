import random
def partittion(array, start, end):
    pivot = array[start]
    i = start + 1
    j = end - 1
    while True:
        while(i<=j and array[i] <= pivot):
            i= i +1
        while (i <= j and array[j] >= pivot):
            j = j - 1

        if(i<=j):
            array[i], array[j]  = array[j], array[i]
        else:
            array[start], array[j] = array[j], array[start]
            return j

def quicksort(array,start, end):
    if  end - start > 1:
        p = partittion(array, start, end)
        quicksort(array,start,p)
        quicksort(array, p + 1, end)

alist = [random.randint(1,10000) for i in range(0,1000000)]
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)