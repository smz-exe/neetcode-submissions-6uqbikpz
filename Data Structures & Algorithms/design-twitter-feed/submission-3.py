class Twitter:

    def __init__(self):
        self.count = 0
        self.posts_of = defaultdict(list)
        self.followed_by = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_of[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.followed_by[userId].add(userId)

        for followeeId in self.followed_by[userId]:
            if followeeId in self.posts_of:
                index = len(self.posts_of[followeeId]) - 1
                count, tweetId = self.posts_of[followeeId][index]
                heapq.heappush(min_heap, (count, tweetId, followeeId, index))
        
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.posts_of[followeeId][index - 1]
                heapq.heappush(min_heap, (count, tweetId, followeeId, index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed_by[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed_by[followerId]:
            self.followed_by[followerId].remove(followeeId)
