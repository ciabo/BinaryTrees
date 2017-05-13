class Node:
    def __init__(self,key,nil):
        if key==None:
            self.key = "nil"
            self.left = self
            self.right = self
            self.p = self
        else:
            self.key=key
            self.left = nil
            self.right = nil
            self.p = nil

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def setP(self, p):
        self.p = p

    def getP(self):
        return self.p

    def getLeft(self):
        return self.left

    def setLeft(self,l):
        self.left=l

    def getRight(self):
        return self.right

    def setRight(self, r):
        self.right = r

    def height(self,node):
        if node.key=="nil":
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1


class Tree:
    def __init__(self):
        self.nil = Node(None, None)
        self.root = self.nil

    def setRoot(self, key):
        self.root = Node(key,self.nil)

    def changeRoot(self,node):
        self.root=node

    def getRoot(self):
        return self.root

    def insert(self, key):
        if self.root is self.nil:
            self.setRoot(key)
            self.root.setP(self.nil)
            return self.root
        else:
            return self.insertNode(key, self.root)

    def insertNode(self, key, currentNode):
        if key <= currentNode.getKey():
            if currentNode.getLeft().getKey()!="nil":
                self.insertNode(key, currentNode.getLeft())
            else:
                currentNode.setLeft(Node(key,self.nil))
                currentNode.getLeft().setP(currentNode)
                return currentNode.getLeft()
        elif key > currentNode.getKey():
            if currentNode.getRight().getKey()!="nil":
                self.insertNode(key, currentNode.getRight())
            else:
                currentNode.setRight(Node(key,self.nil))
                currentNode.getRight().setP(currentNode)
                return currentNode.getRight()


    def inorder(self):
        def _inorder(v):
            if v.getKey() == "nil":
                return
            if v.getLeft().getKey() != "nil":
                _inorder(v.getLeft())
            print(v.getKey())
            if v.getRight().getKey() != "nil":
                _inorder(v.getRight())
        _inorder(self.root)

    def treeSearch(self, k, currentNode):
        while currentNode and k != currentNode.getKey():
            if k < currentNode.getKey():
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
        if currentNode:
            return currentNode
        print("Elemento non presente")

    def serialize(self):
        self.serializeM(self.root)

    def serializeM(self,node):
            print("",node.getKey(),"(",end="")
            if(node.getLeft()) is not None:
                self.serializeM(node.getLeft())
            else:
                print("X ,",end="")
            if (node.getRight()) is not None:
                self.serializeM(node.getRight())
            else:
                print(" X ) ,",end="")


