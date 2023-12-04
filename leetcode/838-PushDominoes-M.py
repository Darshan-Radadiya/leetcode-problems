from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
      
        dominoes = list(dominoes)
        dq = deque()

        for i, d in enumerate(dominoes):
            if d != '.':
                dq.append((i, d))
        
        while dq:
            i, d = dq.popleft()

            if d == 'L' and i > 0 and dominoes[i - 1] == '.':
                dominoes[i-1] = 'L'
                dq.append((i-1, 'L'))
            elif d == 'R' and i + 1 < len(dominoes) and dominoes[i + 1] == '.':
                if i+2 < len(dominoes) and dominoes[i+2] == 'L':
                    dq.popleft()
                else:
                    dominoes[i+1] = 'R'
                    dq.append((i+1, 'R'))
        return ''.join(dominoes)
       
        ## Brilliant solution...
       
        temp = ''
        while dominoes != temp:
            temp = dominoes
            print("Temp....", temp)
            dominoes = dominoes.replace('R.L', 'xxx')     
            print("Dominoes 1st", dominoes)
            dominoes = dominoes.replace('R.', 'RR')         
            print("Dominoes 2nd", dominoes)
            dominoes = dominoes.replace('.L', 'LL')         
            print("Dominoes 3rd", dominoes)
        return  dominoes.replace('xxx', 'R.L')              
        
                    
sol = Solution()
dominoes = ".L.R...LR..L.."
ExpectedOutput = "LL.RR.LLRRLL.."
Output = sol.pushDominoes(dominoes) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
