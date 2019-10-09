#even better way to get an array, find missing numbers, using some Google-Fu

def FindMissingEvenBetter(InputArr):

    return [i for i in range(InputArr[0], InputArr[-1]+1) if i not in InputArr]
    #interates through InputArr and finds missing number in one line!


InputArr = [1,2,3,5,7,8,10]
print(FindMissingEvenBetter(InputArr))
