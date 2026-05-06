class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followeeIds = self.following[userId] | {userId}
        
        heap = []
        for followeeId in followeeIds:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(heap, (time, tweetId, followeeId, idx))
        
        res = []
        while heap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                time ,tweetId = self.tweets[followeeId][idx - 1]
                heapq.heappush(heap, (time, tweetId, followeeId, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self.following[followerId].discard(followeeId)
        
