def detectPalindrome(S):
    if len(S) > 1: 
        left = 0
        right = len(S)-1
        palindrome  = False

        for i in range((len(S)//2)):
            if (S[left].isalnum() == False):
                left += 1
            if (S[right].isalnum() == False):
                right -= 1
            if(S[left].lower() == S[right].lower()):
                palindrome = True
                left += 1
                right -= 1
            else:
                palindrome = False

        return palindrome
    return True



STRING = " Hello "
print("String is Palindrome =" , detectPalindrome(STRING))
