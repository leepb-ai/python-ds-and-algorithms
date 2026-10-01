
class MinHeap:
    def __init__(self):
        self.heap: list= []

    def _parent(self,i: int):
        return (i-1)//2

    def _left_child(self,i: int):
        return 2 * i + 1

    def _right_child(self, i:int):
        return 2 * i + 2

    def _sift_up(self):
            i= len(self.heap)-1 # setting i as the index for last element in list
            while i > 0 and self.heap[i] < self.heap[self._parent(i)]: 
                # comparing last element to successive parents 
                parent_idx= self._parent(i)
                self.heap[parent_idx] , self.heap[i] = self.heap[i], self.heap[parent_idx] # reversing order of parent and element
                i= parent_idx

    def push(self, val):
        self.heap.append(val) # inserting val into the end of the list
        self._sift_up()

     

    
            
        
