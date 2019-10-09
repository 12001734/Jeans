#better way to get an array, find missing numbers

def FindMissingBetter(InputArr):

    OutputArr=[]

    for i in range(InputArr[0], InputArr[-1]+1): #iterate through a just once
        if i not in InputArr:                           #if inequal put in OutputArr
            OutputArr.append(i)
    print(OutputArr)


InputArr = [1,2,3,5,7,8,10]
FindMissingBetter(InputArr)
