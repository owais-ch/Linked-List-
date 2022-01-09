'''Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]'''


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dict1=dict()
        self.count=0
        
    def get(self, key: int) -> int:
            
        if key in self.dict1:
            amount=self.dict1[key]
            del self.dict1[key]
            self.dict1[key]=amount
            return self.dict1[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.dict1:
            del self.dict1[key]
            self.dict1[key]=value
            #self.count+=1
        elif self.count==self.capacity:
            del self.dict1[next(iter(self.dict1))]
            self.dict1[key]=value
        else:
            self.dict1[key]=value
            self.count+=1
