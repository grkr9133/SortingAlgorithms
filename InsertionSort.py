# Insertion Sort Algorithm
# Author: Radhakrishna Rakesh Grandi
# Updated on January 02, 2025.

def insertion_sort(list_a):
    for i in range(1,len(list_a)):
        val=list_a[i]
        while list_a[i-1] > val and i>0:
            list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
            i=i-1
    return list_a

print(insertion_sort([5,84,4,7,65,4,7,52,6,4,78,16,35]))