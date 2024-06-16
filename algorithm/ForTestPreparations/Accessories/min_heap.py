class Heap:
    def __init__(self) -> None:
        self.heap=[]

    def push(self, x):
        self.heap.append(x)
        i = len(self.heap) -1
        while(i>0):
            p = (i -1) //2
            if self.heap[p] >= x:
                break

            self.heap[i]= self.heap[p]
            i=p
        
        self.heap[i] = x

    def top(self):
        if len(self.heap) != 0:
            return self.heap[0]
        else:
            return -1
        
    def pop(self):
        if len(self.heap) == 0:
            return
        
        root_value = self.heap[0]
        x = self.heap.pop()
        if len(self.heap) == 0:
            return root_value
        
        self.heap[0] = x
        i = 0
        while i * 2 + 1 < len(self.heap):
            child_left = i * 2 + 1
            child_right = i * 2 + 2
            if (
                child_right < len(self.heap)
                and self.heap[child_right] > self.heap[child_left]
            ):
                child_left = child_right
            if self.heap[child_left] <= x:
                break
            self.heap[i] = self.heap[child_left]
            i = child_left
        self.heap[i] = x
        return root_value

    def print_heap(self):
        if not self.heap:
            print("Heap is empty")
            return
        
        depth=0
        next_level = 2**depth

        for i, value in enumerate(self.heap):
            if i == next_level-1:
                print()
                depth += 1
                next_level += 2**depth
            print(value, end=" ")
        print("\n")

#検証
def main():
    h = Heap()
    h.push(2)
    h.push(5)
    h.push(7)
    h.push(4)
    h.push(8)
    h.push(6)

    h.print_heap()

    

if __name__=="__main__":
    main()