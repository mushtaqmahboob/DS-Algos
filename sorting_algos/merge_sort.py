def merge_sort(arr):
    size = len(arr)
    if size>1:
        mid = size//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(arr, left, right)
    return arr


def merge(arr,left,right):
    i=0
    j=0
    k=0

    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1



b = [54,26,93,17,77,31]
print(merge_sort(b))



