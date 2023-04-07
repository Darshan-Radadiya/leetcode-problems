def detectpalindrom(S):
    left = 0
    right = len(S)-1
    palindrom  = False

    for i in range((len(S)//2)):
        if (S[left].isalnum() == False):
            left += 1
        if (S[right].isalnum() == False):
            right -= 1
        if(S[left].lower() == S[right].lower()):
            palindrom = True
            left += 1
            right -= 1
        else:
            palindrom = False

    return palindrom



STRING = "Nayan is nayan "
print("String is Palindrom =" , detectpalindrom(STRING))
