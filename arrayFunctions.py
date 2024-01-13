"""
Author: Jon Angle
"""

# reverse an array
def reverseArray(inputArray):
    print(inputArray)
    lenArray = len(inputArray)
    outputArray = []
    for i in range(lenArray):
        countBack = lenArray-i-1
        outputArray.append(inputArray[countBack])
        print(inputArray[countBack],end=" ")
    # print(outputArray)
    return outputArray

def hourglassSum(array6x6):
    arrayWidth = len(array6x6[0])
    arrayHeight = len(array6x6)
    if arrayWidth != 6 or arrayHeight != 6:
        print("Error: The array must be a 6x6 array.")
        return
    print("You entered an array that is",str(arrayWidth)+"x"+str(arrayHeight)+". We can proceed.")
    subArray = []
    iSums = []
    for i in range(4):
        for j in range(4):
            print(i,j)
            iSum = array6x6[i][j]+array6x6[i][j+1]+array6x6[i][j+2]+array6x6[i+1][j+1]+\
                   array6x6[i+2][j]+array6x6[i+2][j+1]+array6x6[i+2][j+2]
            subArray = [array6x6[i][j:j+3],[0,array6x6[i+1][j+1],0],array6x6[i+2][j:j+3]]
            iSums.append(iSum)
            print(subArray[0])
            print(subArray[1])
            print(subArray[2])
            arraySum = 0
            for x in range(3):
                for y in range(3):
                    arraySum = arraySum + subArray[x][y]
            print(arraySum)
            print(iSum)
            print(iSums)
    print(max(iSums))
    maxiSums = max(iSums)
    return maxiSums

# Run the functions
def main():
    # Tests for reverseArray
    # inputArray = [1,4,3,2]
    # reverseArray(inputArray)
    # print()
    # inputArray = [1,2,3,4,5,6,7,8,9]
    # reverseArray(inputArray)
    # print()
    # inputArray = [5,9,1,3,7]
    # reverseArray(inputArray)
    # print()

    # Tests for hourglass
    array6x6 = [[1,1,1,0,0,0],
                [0,1,0,0,0,0],
                [1,1,1,0,0,0],
                [0,0,2,4,4,0],
                [0,0,0,2,0,0],
                [0,0,1,2,4,0]]
    hourglassSum(array6x6)

main()