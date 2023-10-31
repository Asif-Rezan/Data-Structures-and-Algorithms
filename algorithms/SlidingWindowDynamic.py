from typing import List
def dynamic_sliding_window(arr: List[int],x: int) -> int:
    min_length = float('inf')

    start = 0
    end = 0
    current_sum = 0

    while end < len(arr):
        current_sum = current_sum + arr[end]
        end = end +1

        while start < end  and current_sum >= x:
            current_sum = current_sum - arr[start]
            start = start + 1


            min_length = min(min_length, end - start+1)


    return min_length

list = [1,2,3,4,5,6,7,8]
x = 3
print(dynamic_sliding_window(list,x))