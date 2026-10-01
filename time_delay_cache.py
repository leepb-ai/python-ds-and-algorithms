# challenge 3 Timed-Aware Cache
import time


class TimedCache:
    def __init__(self):
        self.storage= {}
        
    def put(self,key,value,ttl: int): # time to live(ttl) in seconds
        expiration_time= ttl+ time.time()
        if key in self.storage:
            entry= self.storage.pop(key)
            entry["value"]= value
            entry["count"] +=1
            entry["expires_at"]= expiration_time
            self.storage[key]= entry
        else: 
            self.storage[key]= {"value": value, "count": 1, "expires_at": expiration_time}


    def get(self,key):
        time_now= time.time()
        if key not in self.storage:
            return None
        entry= self.storage.pop(key)
        if time_now > entry["exprires at"]:
            self.storage.pop(key)
        else:
            entry["count"] +=1 
            return entry["value"]

    def self_cleaned(self) -> int:
        removed_count= 0
        now= time.time()
        for key in list(self.storage.keys()):
            if now > self.storage[key]["expires_at"] :
                self.storage.pop(key)
                print(f"{key} Expired!")
                removed_count +=1
            return removed_count

# Test Case

cache= TimedCache()

cache.put("temp", "secret_data", ttl_seconds=2)

print("Immediate get:", cache.get("temp"))

# wait 2.5 seconds
time.sleep(2.5)

print("Get after 2.5s:", cache.get("temp"))
