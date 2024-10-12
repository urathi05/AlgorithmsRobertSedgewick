def partition(arr, low, high, pivot):
    i = low  # Index for the smaller element
    j = high
    
    while(True):
        
        #while i less than pivot and high then increment
        while arr[i] < pivot and i < high:
            i += 1
        
        #while j greater than pivot and low then decrement
        while arr[j] > pivot and j > low:
            j -= 1
        
        #When i >= j target partition reached
        if i >= j:
            break
        
        #Swap values at i and j
        arr[j], arr[i] = arr[i], arr[j]
    
    return j
        


def nutsBoltsMatch(nuts, bolts, low, high):
    #Run while not base case (both lists not empty)
    if low < high:
        #Choose pivot nut based on a bolt at the low position
        #Partition accordingly
        pivotNut = partition(nuts, low, high, bolts[low])
        partition(bolts, low, high, nuts[pivotNut])
        
        #Recursively sort nuts and bolts using the pivot
        nutsBoltsMatch(nuts, bolts, low, pivotNut - 1)
        nutsBoltsMatch(nuts, bolts, pivotNut + 1, high)


def main():
    nuts = [1, 1, 1, 2, 4, 5, 3 ,6]
    bolts = [1, 5, 4, 6, 3, 1, 1, 2]
    
    # Match the nuts and bolts
    nutsBoltsMatch(nuts, bolts, 0, len(nuts) - 1)
    
    # Print the matched nuts and bolts
    print(f"Nuts: {nuts}")
    print(f"Bolts: {bolts}")

# Run the main function
main()
