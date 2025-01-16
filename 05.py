def sort(a):
    i=0
    while(i<len(a)):
        j=0
        while(j<len(a)-i-1):
            if(a[j]>a[j+1]):
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            j+=1
        i+=1
    return a
print(sort([6,3,4,1,9,7]))