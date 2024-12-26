# SortingAlgorithms
## Bubble Sort
* Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity are quite high.
* We sort the array using multiple passes. After the first pass, the maximum element goes to end (its correct position). Same way, after second pass, the second largest element goes to second last position and so on.
* In every pass, we process only those elements that have already not moved to correct position. After k passes, the largest k elements must have been moved to the last k positions.
* In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at its correct position.
#### Advantages of Bubble Sort:
* Bubble sort is easy to understand and implement.
* It does not require any additional memory space.
* It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
#### Disadvantages of Bubble Sort:
* Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.
* Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set. It can limit the efficiency of the algorithm in certain cases.


## Selection Sort
* Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.

* First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
* Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
* We keep doing this until we get all elements moved to correct position.

### Complexity Analysis of Selection Sort
* Time Complexity: O(n2) ,as there are two nested loops:
 * One loop to select an element of Array one by one = O(n)
 * Another loop to compare that element with every  other Array element = O(n)
 * Therefore overall complexity = O(n) * O(n) = O(n*n) = O(n2)
### Advantages of Selection Sort
* Easy to understand and implement, making it ideal for teaching basic sorting concepts.
* Requires only a constant O(1) extra memory space.
* It requires less number of swaps (or memory writes) compared to many other standard algorithms. Only cycle sort beats it in terms of memory writes. Therefore it can be simple algorithm choice when memory writes are costly.
### Disadvantages of the Selection Sort
* Selection sort has a time complexity of O(n^2) makes it slower compared to algorithms like Quick Sort or Merge Sort.
* Does not maintain the relative order of equal elements which means it is not stable.
### Applications of Selection Sort
* Perfect for teaching fundamental sorting mechanisms and algorithm design.
* Suitable for small lists where the overhead of more complex algorithms isn’t justified and memory writing is costly as it requires less memory writes compared to other standard sorting algorithms.
* Heap Sort algorithm is based on Selection Sort.