class node():
    def __init__(self, value):
        self.value = value;
        self.right = None;
        self.left = None;

    def insert(self, value):
        if(self.value > value):
            if (self.left is None):
                self.left = node(value);
            else:
                self.left.insert(value);
        elif(self.value< value):
            if (self.right is None):
                self.right = node(value)
            else:
                self.right.insert(value)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()
    

def main():
    root = node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.PrintTree()

if __name__ == "__main__":
    main()