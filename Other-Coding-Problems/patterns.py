
def printReactangularPattern (N):
    for i in range(0, N):
        for j in range(0, N):
            print("* ", end=' ')
        print(" ")

def printRightAngledTrianglePattern(N): 
    for i in range(0,N):
        for j in range(0,i):
            print("* ",end=' ')
        print(" ")

def printRightAngledNumberPyramid(N):
    for i in range(0,N):
        for j in range(0,i):
            print(" ", i ,end=' ')
        print(" ")

def printInvertedRightPyramid(N):
    for i in range(0,N):
        for j in range(0,N-i):
            print("* " ,end=' ')
        print(" ")

def printTrianglePyramid(N):
    for i in range(0,N):
        for j in range(0,N-i-1):
                print("  " ,end=' ')
        for j in range(0,2*i+1):
                print("* ",end=' ')
        for j in range(0,N-i-1):
                print("  " ,end=' ')
        print(" ")

def printDiamondStarPattern(N):
    for i in range(0,N):
        for j in range(0,i):
                print("  " ,end=' ')
        for j in range(0,2*N -(2*i +1)):
                print("* ",end=' ')
        for j in range(0,i):
                print("  " ,end=' ')
        print(" ")

def printHalfDiamondStarPattern(N):
    for i in range(0,N):
        for j in range(0,i):
            print("* ",end=' ')
        print(" ")
    for i in range(0,N):
        for j in range(0,N-i):
            print("* " ,end=' ')
        print(" ")
    

number = 10

print("printReactangularPattern = ")
printReactangularPattern(number)
print("-------------------------")

print("printRightAngledTrianglePattern = ")
printRightAngledTrianglePattern(number)
print("-------------------------")

print("printRightAngledNumberPyramid = ")
printRightAngledNumberPyramid(number)
print("-------------------------")

print("printInvertedRightPyramid = ")
printInvertedRightPyramid(number)
print("-------------------------")

print("printTrianglePyramid = ")
printTrianglePyramid(number)
print("-------------------------")

print("printDiamondStarPattern = ")
printDiamondStarPattern(number)
print("-------------------------")

print("printDiamondStarPattern = ")
printHalfDiamondStarPattern(number)
print("-------------------------")