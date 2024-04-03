import heapq
class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetsMap = {}
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsMap: 
            self.tweetsMap[userId] = []
        self.tweetsMap[userId].append([self.timeStamp, tweetId])
        self.timeStamp -= 1 # bcs we are using min Heap

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)

        # Add one most recent tweet from the followee.
        for followee in self.followMap[userId]:
            if followee in self.tweetsMap:
                index = len(self.tweetsMap[followee]) - 1
                timeStamp, tweet = self.tweetsMap[followee][index]
                minHeap.append([timeStamp, tweet, followee, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            timeStamp, tweet, followee, idx = heapq.heappop(minHeap)
            res.append(tweet)
            if idx >= 0:
                timeStamp, tweet = self.tweetsMap[followee][idx]
                heapq.heappush(minHeap, [timeStamp, tweet, followee, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            return
        if followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)