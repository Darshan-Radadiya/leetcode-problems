
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

def printNumberCrownPattern(N):
    space = 2 * (N-1)

    for i in range(1,N+1):
    #Number
        for j in range(1,i+1):
            print(j, end=' ')
    
    #Space
        for j in range(1,space+1):
            print(" " ,end=' ') 
    
    #Space
        for j in range(i,0,-1):
            print(j ,end=' ')

        print(" ")
        space -= 2

def printSymmetricVoidPattern(N):

    space = 0
    for i in range(0,N):

        for j in range(1, N-i+1):
            print(j, end=" ")

        for j in range(space):
             print(" ", end=' ')

        for j in range(1, N-i+1):
             print(j, end = ' ')

        print()
        space += 2

    space = 2*(N-1)
    for i in range(1,N+1):

        for j in range(1, i+1):
            print(j, end=" ")

        for j in range(1, space+1):
             print(" ", end=' ')

        for j in range(i,0,-1):
             print(j, end = ' ')

        print(" ")
        space -= 2
        
        
NUMBER = 4

print("printReactangularPattern = ")
printReactangularPattern(NUMBER)
print("-------------------------")

print("printRightAngledTrianglePattern = ")
printRightAngledTrianglePattern(NUMBER)
print("-------------------------")

print("printRightAngledNumberPyramid = ")
printRightAngledNumberPyramid(NUMBER)
print("-------------------------")

print("printInvertedRightPyramid = ")
printInvertedRightPyramid(NUMBER)
print("-------------------------")

print("printTrianglePyramid = ")
printTrianglePyramid(NUMBER)
print("-------------------------")

print("printDiamondStarPattern = ")
printDiamondStarPattern(NUMBER)
print("-------------------------")

print("printDiamondStarPattern = ")
printHalfDiamondStarPattern(NUMBER)
print("-------------------------")


print("printDiamondStarPattern = ")
printNumberCrownPattern(NUMBER)
print("-------------------------")

print("printDiamondStarPattern = ")
printSymmetricVoidPattern(NUMBER)
print("-------------------------")