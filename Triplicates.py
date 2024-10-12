def mergeSort(arr): 
    #Time complexity O(log N)
    #When combined with merge
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 #middle of array
    left = arr[:mid] #Left half of array
    right = arr[mid:] #Right half of array
    
    return merge(mergeSort(left), mergeSort(right))

def merge(l , r): #Time complexity O(N)
    mergedArr = []
    i = j = 0
    
    #append least element(s) first
    while i < len(l) and j < len(r):
        #if left is lower, append it
        if l[i] < r[j]:
            mergedArr.append(l[i]) 
            i += 1
        #else append right element
        else:
            mergedArr.append(r[j])
            j += 1
    
    # append remaining elements if any
    mergedArr.extend(l[i:])
    mergedArr.extend(r[j:])
    
    #return merged array with sorted elements
    return mergedArr


def binarySearchBool(arr, name):
    ################################
    #Binary Search has Time Complexity
    # O(log N)
    ################################
    #if len == 0 that means 
    #search was exhausted 
    #thus no common name was found
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    
    #searched name found
    if arr[mid] == name:
        return True
    
    #searched name has value greater than mid
    #search larger half of sorted name list
    if arr[mid] < name:
        return binarySearchBool(arr[mid+1:], name)
    
    #searched name has value greater than mid
    #search smaller half of sorted name list
    elif arr[mid] > name:
        return binarySearchBool(arr[:mid], name)


def main():
    list1 = ["Alice", "John", "Michael", "Sara"]
    list2 = ["John", "David", "Emma", "Sophia"]
    list3 = ["Sophia", "Liam", "John", "Olivia"]

    #Time complexity of O(NlogN): mergeSort complexity
    sortList1 = mergeSort(list1)
    sortList2 = mergeSort(list2)
    sortList3 = mergeSort(list3)
    
    triplicate = False
    
    #Time complexity of O(NLogN): for each name do binary searh
    for name in sortList1:
        triplicate = binarySearchBool(sortList2, name) and binarySearchBool(sortList3, name)
        if triplicate == True:
            print("Triplicate: " + name)
            return name
    print("Triplicate: None Found")
    return

main()

###################################################
"""
This program uses merge sort and binary search to find a common name in 3 lists of equal size
After sorting all 3 lists (3 * NlogN = O(NlogN))
We condunct a binary search for each name in the first list (3 * NlogN = O(NlogN))

Adding up these time complexities we get: 3NlogN + 3NlogN = 6NlogN 
6NlogN = O(NlogN)
This matches the required time complexity: linearithmic
"""
