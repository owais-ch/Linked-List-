'''Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]'''

class MyHashMap:

    def __init__(self):
        self.dict1=dict()

    def put(self, key: int, value: int) -> None:
        self.dict1[key]=value
            

    def get(self, key: int) -> int:
        if key in self.dict1:
            return self.dict1[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.dict1:
            self.dict1.pop(key)
            return self.dict1
        else:
            return -1
