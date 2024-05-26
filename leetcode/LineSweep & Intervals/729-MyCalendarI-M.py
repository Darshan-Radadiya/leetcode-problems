from collections import defaultdict
class MyCalendar:

    def __init__(self):
        self.timing = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        # O(n * nlogn)
        self.timing[start] += 1
        self.timing[end] -= 1
        curr_event_count = 0
        for key in sorted(self.timing):
            curr_event_count += self.timing[key]
            if curr_event_count == 2:
                self.timing[start] -= 1
                self.timing[end] += 1
                return False
        return True

class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        # O(nlogn)
        l = 0
        r = len(self.calender)
        while l < r:
            mid = (l + ((r-l)//2))
            if end == self.calender[mid][0]:
                l = mid
                break
            if end > self.calender[mid][0]:
                l = mid + 1
            else:
                r = mid
        if (l > 0 and start < self.calender[l-1][1]) or (l < len(self.calender) and end > self.calender[l][0]):
            return False
        self.calender.insert(l,(start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)