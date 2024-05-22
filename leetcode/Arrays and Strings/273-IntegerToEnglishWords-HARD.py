class Solution:
    def numberToWords(self, num: int) -> str:
        one_digit = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }

        two_digit = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        def getTwoDigitNum(num):
            if num == 0:
                return ""
            elif num < 10:
                return one_digit[num]
            elif num < 20:
                return two_digit[num]
            else:
                tenner = num // 10
                rest = num % 10
                if rest:
                    return tens[tenner] + " " + one_digit[rest]
                else:
                    return tens[tenner]

        def getThreeDigitNum(num):
            if num == 0:
                return ""
            hundreds = num // 100
            rest = num % 100
            if rest and hundreds:
                return one_digit[hundreds] + " Hundred " + getTwoDigitNum(rest)
            elif rest and not hundreds:
                return getTwoDigitNum(rest)
            elif not rest and hundreds:
                return one_digit[hundreds] + " Hundred"

        if num == 0:
            return "Zero"

        res = ""
        billion = num // 1000000000
        million = (num % 1000000000) // 1000000
        thousand = ((num % 1000000000) % 1000000) // 1000
        rest = ((num % 1000000000) % 1000000) % 1000

        if billion:
            res = getThreeDigitNum(billion) + " Billion"
        if million:
            res += " " if res else ""  # we need space if res is not empty
            res += getThreeDigitNum(million) + " Million"
        if thousand:
            res += " " if res else ""
            res += getThreeDigitNum(thousand) + " Thousand"
        if rest:
            res += " " if res else ""
            res += getThreeDigitNum(rest)
        return res

sol = Solution()
num = 123456726546
ExpectedOutput = "One Hundred Twenty Three Billion Four Hundred Fifty Six Million Seven Hundred Twenty Six Thousand Five Hundred Forty Six"
Output = sol.numberToWords(num) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )