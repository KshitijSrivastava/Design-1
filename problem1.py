"""

## Problem 1:
Design Hashmap (https://leetcode.com/problems/design-hashmap/)

Time Complexity:
Insertion O(1)
Deletion O(1)
"""



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return  f"{self.key}/{self.value}"

        
class MyHashMap:

    def __init__(self):
        self.max_size = 10000    # Size of the hashmap
        self.arr = [ None for i in range(self.max_size) ] # create a array of the size
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)                             #Create a node
        if self.arr[ key % self.max_size ] is None:         #if the array location is empty
            self.arr[ key % self.max_size ] = node          #place node at that location
            return
            
        temp = self.arr[ key % self.max_size ]              #find the head for the location
        
        while temp:                                         #Loop over the linkedlist
            if temp.key == key:                             # if the node equals key
                temp.value = value                            #replce the value
                return
            
            if temp.next is None:                           #if the node is the last node
                break                                       #quit the while loop
            
            temp = temp.next                                #If not last node, go to next node
        
        temp.next = node                                    # place the new node in next of temp

    def get(self, key: int) -> int:
        #print(self.arr)
        if self.arr[ key % self.max_size ] is None:
            return -1
        
        temp = self.arr[ key % self.max_size ]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return -1

    def remove(self, key: int) -> None:
        if self.arr[ key % self.max_size ] is None:         #if the position is empty
            return      
        
        prev = None                                         #previous pointer
        temp = self.arr[ key % self.max_size ]              #temp pointer
        
        while temp:                                         #Loop overall the pointers 
            if temp.key == key:                             #if temp key is same as user key
                
                if prev == None:                             # if the temp is the first element
                    self.arr[ key % self.max_size ] = temp.next #point to the element after firstnod
                else:
                    prev.next = temp.next                   # prev.next points to temp.next
                del temp
                return
            
            prev = temp                                     #prev pointer becomes current pointer
            temp = temp.next                                # temp pointer points to next
            
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)