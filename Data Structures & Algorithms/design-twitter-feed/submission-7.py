class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.following[userId] | {userId}

        if len(followees) >= 10:
            followee_heap = []

            for followeeId in followees:
                if followeeId in self.tweets:
                    idx = len(self.tweets[followeeId]) - 1
                    neg_time, tweetId = self.tweets[followeeId][idx]
                    heapq.heappush(followee_heap, (-neg_time, followeeId, tweetId, idx))

                    if len(followee_heap) > 10:
                        heapq.heappop(followee_heap)
            
            while followee_heap:
                time, followeeId, tweetId, idx = heapq.heappop(followee_heap)
                heapq.heappush(heap, (-time, followeeId, tweetId, idx))

        else:
            for followeeId in followees:
                if followeeId in self.tweets:
                    idx = len(self.tweets[followeeId]) - 1
                    time, tweetId = self.tweets[followeeId][idx]
                    heapq.heappush(heap, (time, followeeId, tweetId, idx))
        
        res = []
        while heap and len(res) < 10:
            time, followeeId, tweetId, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx > 0:
                time, tweetId = self.tweets[followeeId][idx - 1]
                heapq.heappush(heap, (time, followeeId, tweetId, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        self.following[followerId].discard(followeeId)
