class FreqStack:

    def __init__(self):
        self.freq = {}
        self.maxFreq = 0
        self.stackOfStack = {}

    def push(self, val: int) -> None:
        self.freq[val] = 1 + self.freq.get(val, 0)
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
            self.stackOfStack[self.maxFreq] = []
        self.stackOfStack[self.freq[val]].append(val)
        return None
    def pop(self) -> int:
        res = self.stackOfStack[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.stackOfStack[self.maxFreq]:
            self.maxFreq -= 1
        return res

# [null,null,null,null,null,null,null,5,7,5,4]
# Initialize FreqStack object
obj = FreqStack()

# Operations to perform
operations = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
operands = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

# Iterate over operations and operands
for i in range(len(operations)):
    operation = operations[i]
    operand = operands[i]
    
    if operation == "FreqStack":
        obj = FreqStack()  # Construct a new FreqStack object
    elif operation == "push":
        print(obj.push(operand[0]))  # Call push operation with operand
    elif operation == "pop":
        print(obj.pop())  # Call pop operation and print the result
