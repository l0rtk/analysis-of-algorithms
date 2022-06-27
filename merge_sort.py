def merge(arr1,arr2):
    res = []
    m = len(arr1)+len(arr2) 
    i = 0
    j = 0
    for k in range(m):
        if i > len(arr1)-1:
            res.append(arr2[j])
            j+=1
        elif j > len(arr2)-1:
            res.append(arr1[i])
            i+=1
        
        elif arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    return res



def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    m = len(arr)//2

    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])
    return merge(l,r)


