# challenge 2: LFU(Least Frequently Used) with LRU(Least Recently Used)

class LFUTieCache:
    def __init__(self, capacity):
        self.capacity= capacity
        self.storage={}

    def get(self, key):
        if key not in self.storage:
            return None
        entry= self.storage.pop(key)
        entry["count"] +=1
        self.storage[key] =entry
        return entry["value"]


    def put(self, key, value):
        if key in self.storage:
            entry= self.storage.pop(key)
            entry["value"]= value
            entry["count"] +=1
            self.storage[key]= entry
        else:
            if len(self.storage) == self.capacity:
               #1. storing the least count items in the cache
               min_count= min(e["count"] for e in self.storage.values())
               #2. Finding the first key with min_count (LRU tie-breaker)
               victim_key= None
               for k, entry in self.storage.items(): 
                # looping through cache keys and entrys
                  if entry["count"] == min_count:
                      victim_key= k
                      break
               self.storage.pop(victim_key)

            self.storage[key]= {"value": value, "count": 1}

# test case

cache_2= LFUTieCache(3)

cache_2.put("patient name", "Rory James")
cache_2.put("patient age", 34)
cache_2.put("patient status", "Emergency")

print(f"Retrieving patient name : {cache_2.get("patient name")}")
print(f"...Retrieving patient age : {cache_2.get("patient age")}")
print(f"...Retrieving patient status : {cache_2.get("patient status")} ")

user_input= input("Enter a patient name: ").strip()

cache_2.put("patient name", user_input)
print(f"Updating....\n")

print(f"New patient name: {cache_2.get("patient name")}")



    









             

