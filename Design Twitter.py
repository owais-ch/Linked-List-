'''Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the
user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]'''



class Twitter:

    def __init__(self):
        self.dict1=dict()
        self.dict2=dict()
        
        self.list2=[]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.dict1:
            self.dict1[userId]=[tweetId]
        else:
            self.dict1[userId].append(tweetId)
        
        self.list2.append([userId,tweetId])
        
        
        
    def getNewsFeed(self, userId: int):
        if userId not in self.dict2:
            if userId in self.dict1:
                self.dict1[userId].reverse()
                self.dict1[userId]=self.dict1[userId][:10]
                return self.dict1[userId]
            else:
                return None
        elif self.dict2[userId]==[]:
            if userId in self.dict1:
                self.dict1[userId]=self.dict1[userId][:10]
                
                return self.dict1[userId]
            else:
                return None
        else:
            list3=[]
            
            for i in self.list2:
                if i[0]==userId or i[0] in self.dict2[userId]:
                    list3.append(i[1])
            list3.reverse()
            list3=list3[:10]        
            return list3[:10]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.dict2:
            self.dict2[followerId]=[followeeId]
        else:
            if followeeId not in self.dict2[followerId]:
                self.dict2[followerId].append(followeeId)
             
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.dict2 and followeeId in self.dict2[followerId]:
            self.dict2[followerId].remove(followeeId)
