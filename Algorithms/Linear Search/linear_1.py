array = input().strip().split(' ')
N = int(array[0])
M = int(array[1])
index = -1
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
res = max(idx for idx, val in enumerate(arr) if val == M)
for j, data in enumerate(arr):
    if arr[res] == data:
        index = j + 1
print(index)
