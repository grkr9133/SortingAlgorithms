# Selection Sort Algorithm
# Author: Radhakrishna Rakesh Grandi
# Updated on December 26, 2024.

def selectionSort(list_a):
    print(list_a)
    length=len(list_a)
    for i in range(length):
        min_idx=i
        for j in range(i+1,length):
            if list_a[j]<list_a[min_idx]:
                min_idx=j
        list_a[min_idx],list_a[i]=list_a[i],list_a[min_idx]

    return list_a

print(selectionSort([5, 6, 7, 2, 47, 31, 84, 95, 15, 21, 46]))


