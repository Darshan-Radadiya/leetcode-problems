class Node():
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage,None,None)

    def visit(self, url: str) -> None:
        newNode = Node(url,self.head,None)
        self.head.next = newNode
        self.head = newNode

    def back(self, steps: int) -> str:
        curr = self.head
        while self.head.prev and steps > 0:
                self.head = self.head.prev
                steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while self.head.next and steps > 0:
                self.head = self.head.next
                steps -= 1
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)