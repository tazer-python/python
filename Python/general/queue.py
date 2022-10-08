class queue:
    def __init__(self, length):
        self.length = length;
        self.arr = [None for i in range(length)];
        self.front = -1;

    def enqueue(self, value):
        new_arr = [value];
        self.front += 1;
        for i in self.arr:
            if len(new_arr) < self.length:
                new_arr.append(i);
            else:
                pass
        
        self.arr = new_arr;

    def dequeue(self):
        if(self.front >= len(self.arr)):
            self.front -=1
        else:
            pass
        self.arr[self.front] = None;

    def PrintStack(self):
        print(self.arr);

def main():
    q = queue(5);
    q.enqueue(17);
    q.enqueue(15);
    q.enqueue(14)
    q.enqueue(30)
    q.enqueue(19)
    q.enqueue(5)
    print("initial queue :");
    q.PrintStack();
    q.dequeue()
    print("final queue: ")
    q.PrintStack()

main()