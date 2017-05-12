class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

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
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def getChildren(self):
        children = []
        if self.left != None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)
        return children


class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def changeRoot(self,node):
        self.root=node

    def getRoot(self):
        return self.root

    def insert(self, key):
        if self.root is None:
            self.setRoot(key)
            self.root.setP(None)
            return self.root
        else:
            return self.insertNode(key, self.root)

    def insertNode(self, key, currentNode):
        if key <= currentNode.getKey():
            if currentNode.getLeft():
                self.insertNode(key, currentNode.getLeft())
            else:
                currentNode.setLeft(Node(key))
                currentNode.getLeft().setP(currentNode)
                return currentNode.getLeft()
        elif key > currentNode.getKey():
            if currentNode.getRight():
                self.insertNode(key, currentNode.getRight())
            else:
                currentNode.setRight(Node(key))
                currentNode.getRight().setP(currentNode)
                return currentNode.getRight()


    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.getLeft() is not None:
                _inorder(v.getLeft())
            print(v.getKey())
            if v.getRight() is not None:
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


