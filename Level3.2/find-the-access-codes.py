def solutionSlow(codeList):

    #First check if argument is list
    if type(codeList) != list:
        return -1
    
    #Then check if list is not empty
    if len(codeList) < 3:
        return -1

    #Check if list above max value
    if len(codeList) > 2000:
        return -1
    
    #order list in descending order
    codeList.sort(reverse=True)

    triplesCounter = 0
    for outerIndex in range(0,len(codeList)):
        #make a sublist from actual index until end
        midSublist = codeList[outerIndex+1:]
        #if len of sublist is less than 2 its time to break main for
        if len(midSublist) < 2:
            break
        
        actualNumber = codeList[outerIndex]
               
        #look for dividers from actual number
        for midIndex in range(0,len(midSublist)):
            #check if mid item is divider of actual item
            if actualNumber % midSublist[midIndex] == 0:

                #save mid number at local varible
                midNumber = midSublist[midIndex]
                #make a sublist with lasts numbers
                innerSublist = midSublist[midIndex+1:]

                #if len of sublist is less than 1 its time to break mid for
                if len(innerSublist) < 1:
                    break
                
                
                for innerIndex in range(0,len(innerSublist)):
                    #check if inner item is divider of actual item
                    if midNumber % innerSublist[innerIndex] == 0:
                        triplesCounter += 1
                        #print((actualNumber, midNumber, innerSublist[innerIndex]))
                        
    return triplesCounter


def solution(codeList):

    #First check if argument is list
    if type(codeList) != list:
        return -1
    
    #Then check if list is not empty
    if len(codeList) < 3:
        return -1

    #Check if list above max value
    if len(codeList) > 2000:
        return -1

    #define a counter with size equals codeList
    counters = [0] * len(codeList)
    triplesCounter = 0

    #two nested for, outer travel thru codeList, inner goes from 0 to actual value
    #inner for colects dividers quantity from previous values, if found a number with previous divider increase triple counter
    for outerIndex in range(0,len(codeList)):
        for innerIndex in range(0, outerIndex):
            if codeList[outerIndex] % codeList[innerIndex] == 0:
                counters[outerIndex] += 1
                triplesCounter += counters[innerIndex]
      
    return triplesCounter





def test():
    if(solution([1, 2, 3, 4, 5, 6]) == 3):
        print("TEST 1 PASSED")
    else:
        print("TEST 1 FAILED")

    if(solution([1, 1, 1]) == 1):
        print("TEST 2 PASSED")
    else:
        print("TEST 2 FAILED")

    if(solution([]) == -1):
        print("TEST 3 PASSED")
    else:
        print("TEST 3 FAILED")
    
    # (12 6 3) (12 6 2) (12 6 1) (12 4 2) (12 4 1) (12 3 1) (12 2 1) (6 3 1) (6 2 1) (4 2 1)
    if(solution([1, 2, 3, 4, 5, 6, 12]) == 10):
        print("TEST 4 PASSED")
    else:
        print("TEST 4 FAILED")

    if(solution([1, 2, 3, 5, 7, 11]) == 0):
        print("TEST 5 PASSED")
    else:
        print("TEST 5 FAILED")
    
    if(solution([1,2,3,4,5,6,7,8]) == 6):
        print("TEST 6 PASSED")
    else:
        print("TEST 6 FAILED")


if __name__ == "__main__": 
    test()