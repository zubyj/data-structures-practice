import ctypes

class DynamicArray(object):
    
    def __init__(self):
        self.size = 1 # total size of array
        self.n =  0 # actual elements in array
        self.arr = (self.size * ctypes.py_object)()
    
    def append(self, ele):
        # precheck - array isn't full.
        if self.n == self.size:
            self.resize()

        self.arr[self.n] = ele
        self.n += 1

    def resize(self):
        self.size *= 2
        A = (self.size * ctypes.py_object)()
        for i in range(self.n):
            A[i] = self.arr[i]
        self.arr = A
        return

    def delete(self):
        if self.n == 0:
            print('cannot delete from empty array')
            return
        self.arr[self.n-1] = 0
        self.n -= 1

    def appendAt(self, index, ele):
        if (self.size == self.n): 
            self.resize()
        
        if index < 0 or index > self.n-1:
            print('index out of range')
            return

        for i in range(self.n-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        # 1 8 2 3 4 5
        self.arr[index] = ele
        self.n += 1

    def removeAt(self, index):
        if (self.n == 0):
            print('cannot remove from empty list')
            return
        
        # 1 2 3 4 5
        # remove index 2
        # 1 3 4 5
        
        # at index + 1 to end, shift each elem left one. 
        # at the end, remove the last element

        for i in range(index, self.n-1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.n-1] = 0
        self.n -= 1
        
    def getArray(self):
        return self.arr

    def len(self):
        return self.n

def main():
    da = DynamicArray()
    da.append(1)
    da.append(2)
    da.appendAt(1, 5)
    da.append(5)
    da.removeAt(0)
    for i in range(da.len()):
        print(da.getArray()[i])

if __name__ == "__main__":
    main()
