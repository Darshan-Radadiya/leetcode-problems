from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.timing = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        # O(n * nlogn)
        self.timing[start] += 1
        self.timing[end] -= 1
        curr_event_count = 0
        for key in sorted(self.timing):
            curr_event_count += self.timing[key]
            if curr_event_count == 3:
                self.timing[start] -= 1
                self.timing[end] += 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)