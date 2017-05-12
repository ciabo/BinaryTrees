class RBNode():
    def __init__(self,key,nil):
        if key==None:
            self.key = "nil"
            self.left = self
            self.right = self
            self.p = self
            self.color = "black"
        else:
            self.key=key
            self.left = nil
            self.right = nil
            self.p = nil
            self.color="black"

    def height(self,node):
        if node.key=="nil":
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

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

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color





class RBTree():
    def __init__(self):
        self.nil=RBNode(None,None)
        self.nil.setColor("black")
        self.root=self.nil

    def setRoot(self, key):
        self.root = RBNode(key,self.nil)

    def changeRoot(self,node):
        self.root=node

    def getRoot(self):
        return self.root

    def leftRotation(self, x):
        y=x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft().getKey() != "nil":
            y.getLeft().setP(x) #Put the left subTree of y in the right subTree of x
        y.setP(x.getP()) #Y became the son of x parent
        if x.getP().getKey() == "nil": #if x is the root
            self.changeRoot(y)
        elif x == x.getP().getLeft():
            x.getP().setLeft(y)
        else:
            x.getP().setRight(y)
        y.setLeft(x)
        x.setP(y)

    def rightRotation(self,x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        if y.getRight().getKey() != "nil":
            y.getRight().setP(x)
        y.setP(x.getP())
        if x.getP().getKey() == "nil":
            self.changeRoot(y)
        elif x == x.getP().getLeft():
            x.getP().setLeft(y)
        else:
            x.getP().setRight(y)
        y.setRight(x)
        x.setP(y)

    def insert(self, key):
        if self.root is self.nil:
            self.setRoot(key)
            self.root.setColor("red")
            self.fixUp(self.root)
        else:
            self.insertNode(key, self.root)

    def insertNode(self, key, currentNode):
        if key <= currentNode.getKey():
            if currentNode.getLeft().getKey()!="nil":
                k=0
                self.insertNode(key, currentNode.getLeft())
            else:
                k=0
                currentNode.setLeft(RBNode(key,self.nil))
                currentNode.getLeft().setP(currentNode)
                currentNode.getLeft().setColor("red")
                self.fixUp(currentNode.getLeft())
                return currentNode.getLeft()
        elif key > currentNode.getKey():
            if currentNode.getRight().getKey() != "nil":
                self.insertNode(key, currentNode.getRight())
            else:
                currentNode.setRight(RBNode(key,self.nil))
                currentNode.getRight().setP(currentNode)
                currentNode.getRight().setColor("red")
                self.fixUp(currentNode.getRight())
                return currentNode.getRight()

    def fixUp(self,z):
        while(z.getP().getColor()=="red"): #means that there are two red nodes in sequence
            if z.getP()==z.getP().getP().getLeft(): #if z's father is the left son of z's grandfather
                y=z.getP().getP().getRight() #y is z's uncle (the right son of z's grandfather)
                if y.getColor()=="red":
                    z.getP().setColor("black")
                    y.setColor("black")
                    z.getP().getP().setColor("red")
                    z=z.getP().getP()
                else:
                    if z==z.getP().getRight():
                        z=z.getP()
                        self.leftRotation(z)
                    z.getP().setColor("black")
                    z.getP().getP().setColor("red")
                    self.rightRotation(z.getP().getP())
            else:
                y = z.getP().getP().getLeft()
                if y.color == "red":
                    z.getP().setColor("black")
                    y.setColor("black")
                    z.getP().getP().setColor("red")
                    z = z.getP().getP()
                else:
                    if z == z.getP().getLeft():
                        z = z.getP()
                        self.rightRotation(z)
                    z.getP().setColor("black")
                    z.getP().getP().setColor("red")
                    self.leftRotation(z.getP().getP())
        self.root.setColor("black")

    def inorder(self):
        def _inorder(v):
            if v.getKey() == "nil":
                return
            if v.getLeft().getKey() != "nil":
                _inorder(v.getLeft())
            print(v.getKey()," ",v.getColor())
            if v.getRight().getKey() != "nil":
                _inorder(v.getRight())
        _inorder(self.root)



