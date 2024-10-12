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


def longestIntervals(jobs):
    lastFinish = 0
    currentRunningStart = 0
    maxIdleTime = 0
    maxIdleInterval = [0, 0]
    maxRunningTime = 0
    maxRunningInterval = [0, 0]   
    
    #Iterate over jobs
    for i in range(len(jobs)):
        
        #current job starts after the last one finised - represents idle time
        if jobs[i][0] > lastFinish:
            
            #if this idle time is greather than last recorded max idle time
            #update max idle time
            #update the new max idle interval
            if jobs[i][0] - lastFinish > maxIdleTime:
                maxIdleTime = jobs[i][0] - lastFinish
                maxIdleInterval[0], maxIdleInterval[1] = lastFinish, jobs[i][0]
            
            #new current start time for the job if there is idle time
            currentRunningStart = jobs[i][0]

        #create new current run time when theres no idle time
        currentRunningTime = jobs[i][1] - currentRunningStart
        
        #when current running time greater than last recorded max running time
        #new max run time = current running time
        #update running interval
        if currentRunningTime > maxRunningTime:
            maxRunningTime = currentRunningTime
            maxRunningInterval[0], maxRunningInterval[1] = currentRunningStart, jobs[i][1]
        
        #finally check if last recorded finish time is greater or current jobs finish
        #update last finish accordingly for next loop
        lastFinish = max(lastFinish, jobs[i][1])
        
    return(f"""Max Idle Time is: {maxIdleTime}
Max Idle Interval is: {maxIdleInterval}
Max Running Time is: {maxRunningTime}
Max Running Interval is: {maxRunningInterval}
    """)


def main():
    jobs = [(1, 4)]#, (2, 5), (7, 9), (10, 16), (11, 13), (14, 17)]
    print(longestIntervals(mergeSort(jobs)))


main()