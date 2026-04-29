class Twitter:

    def __init__(self):
    # for each use, keep most recent 10 posts
    # graph: user A follow (->) user B
        self.user_post = defaultdict( deque )
        self.user_to_user = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_post[userId].append( (self.count, tweetId) )
        self.count += 1
#        print(self.user_post)
        while len(self.user_post[userId]) > 10:
            self.user_post[userId].popleft()


    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.user_to_user[userId] | {userId}

        minHeap = []

        for u in users:
#            for idx in range( min(10, len(self.user_post[u])) ):
            for count, tweetId in self.user_post[u]:
                heapq.heappush(minHeap, (count, tweetId) )
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        minHeap.sort(reverse = True)
        return [tweetId for count, tweetId in minHeap]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_to_user[followerId]:
            self.user_to_user[followerId].remove(followeeId)
