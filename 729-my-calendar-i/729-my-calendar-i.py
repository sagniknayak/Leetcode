class MyCalendar:

    def __init__(self):
        self.table = {0:1e+9}
        

    def book(self, start: int, end: int) -> bool:
        flag = False
        start_after = None
        endtime = list(self.table.keys())
        endtime.sort()
        for key in endtime:
            if key <= start:
                start_after = key
            else:
                break
        if end <= self.table[start_after]:
            flag = True
            self.table[end] = self.table[start_after]
            self.table[start_after] = start
        return flag
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)