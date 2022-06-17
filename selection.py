#find Kth largest element in array


def swap(array,index1,index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp

    return array

# O(i=0 to K ΣN-i)   N - size of the list
def selection(array,k):
    for i in range(1,k+1):
        largestEl = array[0]
        largestInd = 0

        for j in range(len(array[:-i])+1):
            if array[j] > largestEl:
                largestEl = array[j]
                largestInd = j

        array = swap(array,largestInd,len(array)-i)


    print(array)
    return array[-k]


arr = [217,3291,239829378237,9,-21,0]

assert selection(arr,1) == 239829378237
assert selection(arr,2) == 3291
assert selection(arr,3) == 217
assert selection(arr,4) == 9
assert selection(arr,5) == 0
assert selection(arr,6) == -21

