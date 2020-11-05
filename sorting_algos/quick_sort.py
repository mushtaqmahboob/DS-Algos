def quick_sort(arr,p,r):

    if p<r:
        q = partition(arr, p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)


def partition(arr,p,r):
    pivot = arr[p]
    i=p
    for j in range(p+1, r+1):

        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[p] = arr[p], arr[i]
    return i

b= [2,6,8,11,0,7]
quick_sort(b, 0, len(b)-1)
print(b)