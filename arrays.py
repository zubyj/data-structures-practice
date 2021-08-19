# https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/

import ctypes
  
class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''
      
    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default capacity
        self.A = self.make_array(self.capacity)
          
    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n
      
    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not (0 <= k < self.n):
            print('Out of bounds index')
        return self.A[k]
          
    def append(self, ele):
        """
        Add element to end of the array
        """
        if (self.capacity == self.n):
            self._resize(2 * self.capacity)
        
        self.A[self.n-1] = ele
        self.n +=1 

  
    def insertAt(self,item,index):
        """
         This function inserts the item at any specified index.
        """
        if not (0 <= index <= self.n):
            print('Please enter a valid index')
        
        if (self.capacity == self.n):
            self.A._resize(2 * self.n)
        
        #   [a, b, c, d]  -> [a, b, f, c, d] 
        # [a, b, c ,d] -> [a, b, c, c, d]
        # insert f at 2nd index
        # 

        for i in range(index+1, self.n-1):
            self.A[i+1] = self.A[i]
        self.A[index] = item
        self.n +=1 
          
    def delete(self):
        """
        This function deletes item from the end of array
        """
        if (self.n == 0):
            print("cannot delete from empty array")
        self.A[self.n-1] = 0
        self.n -= 1
          
      
    def removeAt(self,index):
        """
        This function deletes item from a specified index..
        """ 
        if (self.n == 0):
            print("cannot delete from empty array")    

        if not (0 <= index <= self.n):
            print('Please enter a valid index')
    

        if (index == self.n-1):
            self.A[index] = 0
            self.n -=1
            return
        
        '''
        [a, b, c, d, e] -> [a, b, d, e]
        1. the index of every element after removed goes down by 1
        '''
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
        
        self.A[self.n-1] = 0
        self.n -=1
          
    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap)

        for i in range(self.n-1):
            B[i] = self.A[i]
        
        self.A = B
        self.capacity = new_cap

          
    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()

def main():
    arr = DynamicArray()
    arr.append(1)
    len(arr)
    arr.append(2)
    print(len(arr))
    print(arr[0])
    arr.append(100)
    print(len(arr))
    print(arr.capacity)

if __name__ == "__main__":
    main()


    