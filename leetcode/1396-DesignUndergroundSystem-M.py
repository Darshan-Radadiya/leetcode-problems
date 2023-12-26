class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id : startStation, time
        self.totalTimeMap = {} # startStation, endStation : totalTime, Count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.checkInMap[id]
        route = (startStation, stationName)
        if route not in self.totalTimeMap:
            self.totalTimeMap[route] = [0,0]
        self.totalTimeMap[route][0] += t - time
        self.totalTimeMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.totalTimeMap[(startStation, endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()

obj.checkIn(45,"Leyton",3)
obj.checkIn(32,"Paradise",8)
obj.checkIn(27,"Leyton",10) 
obj.checkOut(45,"Waterloo",15 )
obj.checkOut(27,"Waterloo",20 )
obj.checkOut(32,"Cambridge",22) 
param_3 = obj.getAverageTime("Paradise","Cambridge")
ExpectedOutput = 14.0
print("\nOutput is:      ", param_3,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == param_3, "\n" )
print("Time Complexity is: O(1) and Space Complexity is O(n)\n" )