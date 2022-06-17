
# O(logn)
def binary_search(lst,target):

    L = 0
    R = len(lst)-1

    while (L <= R):
        M = (R+L)//2
        if lst[M] == target:
            return M
        elif lst[M] > target:
            R = M - 1
        else: #lst[M] < target
            L = M + 1

    return -1


test_list = [1,2,3,4,5,21414,12121,422,2]
target = 5

assert binary_search([1,2,3,4,5,6],1) == 0
assert binary_search([1,2,3,4,5,6],2) == 1
assert binary_search([1,2,3,4,5,6],3) == 2
assert binary_search([1,2,3,4,5,6],4) == 3
assert binary_search([1,2,3,4,5,6],5) == 4
assert binary_search([1,2,3,4,5,6],6) == 5
assert binary_search([1,2,3,4,5,6],7) == -1
