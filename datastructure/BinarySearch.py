
pos = -1
def binarySearch(list,n):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = (low+high) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < n:
                low = mid
            else:
                high = mid

list = [1,2,5,2,4,7,8,9,22,4,2]

if binarySearch(list,9):
    print("found in position",pos+1)
else:
    print("not found")

