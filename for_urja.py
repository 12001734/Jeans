#take an array, output the missing numbers

#import random      #just using this for testing

def FindMissing(a):

    ArrayToCompare=[]
    OutputArr=[]

    for i in range(1,(sorted(a)[-1]+1)):     #make a list using the
        ArrayToCompare.append(i)             #highest number in InputArr

    for i in ArrayToCompare:    #iterate through arrays, finding inequal
        if i not in a:          #values then putting it in OutputArr
            OutputArr.append(i)

    print(OutputArr)


#InputArr = random.sample(range(20),10)     #just using this for testing
InputArr = [1,2,3,5,7,8,10]
FindMissing(InputArr)
