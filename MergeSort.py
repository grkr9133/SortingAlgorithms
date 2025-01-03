def MergeSort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        #recursion
        MergeSort(left_arr)
        MergeSort(right_arr)
        #merge
        i,j,k=0,0,0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
    return arr

print(MergeSort([2,5,49,52,1,64,92,2,94,7,1,62,1,94]))