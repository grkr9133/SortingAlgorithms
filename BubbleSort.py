# Bubble Sort Algorithm
# Author: Radhakrishna Rakesh Grandi
# Updated on December 26, 2024

def bubblesort(list_a):
    print(list_a)
    length = len(list_a)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if list_a[i] > list_a[i+1]:
                list_a[i],list_a[i+1]=list_a[i+1],list_a[i]
                sorted = False
    return list_a

print(bubblesort([5,6,7,2,47,31,84,95,15,21,46])) 