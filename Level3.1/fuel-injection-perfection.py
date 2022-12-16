import math

def isEven(num):
    return num % 2 == 0

def isPowerOfTwo (x):
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not(x & (x - 1))) )

def Log2(x):
    return (math.log10(x) /
            math.log10(2))

def solution(inputPellets):
    inputPellets = long(inputPellets)
    
    counter = 0
    #If pellets is 3 or less those are my final cases
    #So, divide by 2 when i can until pellets are 3 or less
    while inputPellets > 3:
        #Check in inputPellets is even
        if inputPellets & 1:
            if inputPellets & 2:
                #Add one and divide by 2 two time, so increment counter by 3
                inputPellets = (inputPellets + 1) >> 2
                counter += 3
            else:
                #Decress one and divide by 2, so i made 2 operations, incremente counter by 2
                inputPellets = (inputPellets - 1) >> 1
                counter += 2
        else:
            #is even, so divide by 2
            inputPellets = inputPellets >> 1
            counter += 1
    
    #I left while loop, so its 3 or less
    if inputPellets == 3:
        inputPellets = inputPellets - 1
        counter += 1

    if inputPellets == 2:
        inputPellets = inputPellets - 1
        counter += 1

    #Didn't check if pellets is 1 because is my last value
    return counter


if __name__ == "__main__": 

    if solution("15") == 5:
        print("1 PASSED")
    else:
        print("1 FAIL")

    if solution("4") == 2:
        print("2 PASSED")
    else:
        print("2 FAIL")
    