''' 선택정렬

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]


array1 = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array1)):
    min_index = i
    for j in range(i+1, len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
        # 여기 스와프 코드 잘 인식하기. 
        array1[i], array1[min_index] = array1[min_index], array1[i]
print(array)
print(array1)
'''
'''
삽입정렬

array = [7,5,9,0,3,1,6,2,4,8]
array1 = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in range(1, len(array1)):
    for j in range(i, 0, -1):
        if array1[j]< array1[j-1]:
            array1[j-1], array1[j] = array1[j], array1[j-1]
        else:
            break

print(array)
print(array1)
'''
array = [5,7,9,0,3,1,6,2,4,8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while left <= right: # 종료조건
        while left <= end and array[left] <= array[pivot]:
            left +=1
        while right>start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0 , len(array)-1)

print(array)

        




    




