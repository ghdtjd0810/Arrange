# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:23:36 2022

@author: LG
"""



array = [5,7,9,0,3,1,6,2,4,8]


def quick_sort(array):
    if len(array) <=1: #왼쪽 오른쪽 정렬된 각각의 함수들을 
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] #만약에 tail 보다 작으면 왼쪽에 리스트 반환
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))




tail1 = array[1:]
pivot1 = array[0]


abc = [x for  x in tail1 if x <= pivot1]

print(abc)
