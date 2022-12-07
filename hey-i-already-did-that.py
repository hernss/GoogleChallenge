def solution(minionID, base):
    MAX_ITERATIONS = 40 #Max iteration until it fail
    iterations = 0
    #Array for results
    results = []
    
    #Safe loop
    while(iterations < MAX_ITERATIONS):
        iterations += 1

        k=0
        x = []
        y = []
        
        for c in minionID:
            k+=1
            x.append(int(c))
            y.append(int(c))
        
        #Sort number arrays
        x.sort(reverse=True)
        y.sort()

        #Fill z with 0 
        z = []
        for i in range(0,k):
            z.append(0)
    
        #sustract in base b
        for n in reversed(range(0,k)):
            if x[n] < y[n]:
                x[n] += base
                x[n-1] -= 1     # it wil never fail because x is always greater than y

            z[n] = x[n] - y[n]

        #Make new minion ID
        minionID = ""
        for i in z:
            minionID += str(i)

        #Check if new minion is in results array
        if minionID not in results:
            #If not, just add it and calculate the new one
            results.append(minionID)
        else:
            #If you found it, its because you enter in a loop, look for id of match and then sustract total lenght with this index to calcule the loop lenght
            pos = results.index(minionID)
            return len(results) - pos
    
    #If you did more than MAX ITERATIONS just fail with returning -1
    return -1



if __name__ == "__main__": 
    if solution('1211', 10) == 1:
        print("1 PASSED")
    else:
        print("1 FAIL")

    if solution('210022', 3) == 3:
        print("2 PASSED")
    else:
        print("2 FAIL")
    
