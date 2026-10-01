# challenge 1 - Tracked LRU Cache

class TrackedLRUCache:
    def __init__(self,capacity):
        self.capacity= capacity
        self.storage= {}

    def get(self,key):
        if key not in self.storage:
            return None
        entry= self.storage.pop(key)
        entry["count"] +=1
        self.storage[key] =entry
        return entry["value"]

    

    def put(self,key,value):
        if key in self.storage:
            entry= self.storage.pop(key) # pops matching key and stores it as entry
            entry["value"]= value # assigns new value to existing key
            self.storage[key]= entry
        if len(self.storage)== self.capacity:
            least_accessed= next(iter(self.storage)) #  stores the first item in the dictionary as the least accessed
            self.storage.pop(least_accessed) #removing least accessed item
        self.storage[key]= {"value":value,"count":1} 

    def get_count(self, key):
        if key  not in self.storage:
            return None
        return self.storage[key]["count"]
        


# Test case
cache= TrackedLRUCache(2)
cache.put("x",100)
cache.put("y",200)

assert cache.get("x") == 100
print(f"Count of x: {cache.get_count("x")}")

cache.put("z", 300)

print(f"Value of y is {cache.get("y")}")
print(f"Value of x is {cache.get("x")}")
print(f"Value of z is {cache.get("z")}")

cache.put("x",400)
print(f"New value of x is {cache.get("x")}")