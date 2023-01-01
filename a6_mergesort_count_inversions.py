from collections import deque
_ = input()
arr = [int(x) for x in input().split()]
result = 0

def merge_sort(data):
    size = len(data)
    if size <= 1:
        return deque(data)
    return merge(merge_sort(data[:size//2]), merge_sort(data[size//2:]))

def merge(left, right):
    global result
    data = deque()
    while left and right:
        if left[0] <= right[0]:
            data.append(left.popleft())
        else:
            data.append(right.popleft())
            result += len(left)
    data.extend(left or right)
    return data

merge_sort(arr)
print(result)