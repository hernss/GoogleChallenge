def solution(inputList):
    #Type check
    if not type(inputList) is list:
        raise TypeError("Invalid argument, only string list allowed.")

    #Size check
    if len(inputList) > 100:
        raise Exception("Too many items in input list.")
    
    if len(inputList) == 0:
        raise Exception("Input list can't be empty.")

    sortedList = []
    for version in inputList:
        #Item type check
        if not type(version) is str:
            raise TypeError("Invalid argument, only string list allowed.")

        versionSplitted = version.split('.')
        if len(versionSplitted) == 1:
            sortedList.append({"major": int(versionSplitted[0]), "minor" : -1, "rev" : -1})
        elif len(versionSplitted) == 2:
            sortedList.append({"major": int(versionSplitted[0]), "minor" : int(versionSplitted[1]), "rev" : -1})
        elif len(versionSplitted) == 3:
            sortedList.append({"major": int(versionSplitted[0]), "minor" : int(versionSplitted[1]), "rev" : int(versionSplitted[2])})  
        else:
            raise Exception("Invalid version format.")

    #sort list by major, minor and rev criteria.
    sortedList.sort(key=lambda x: (x["major"], x["minor"], x["rev"]))
    
    outputList = []
    #make output string from sorted list
    for item in sortedList:
        outputString = ""
        outputString += str(item["major"])
        if item["minor"] != -1:
            outputString += "." + str(item["minor"])
        if item["rev"] != -1:
            outputString += "." + str(item["rev"])

        outputList.append(outputString)

    return outputList

if __name__ == "__main__": 
    if solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]:
        print("1 PASSED")
    else:
        print("1 FAIL")

    if solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]:
        print("2 PASSED")
    else:
        print("2 FAIL")
    