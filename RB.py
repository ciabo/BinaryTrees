import ABR

class RBTree(ABR.Tree):
    def __init__(self):
        ABR.Tree.__init__(self)
        self.color = "Black"

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color

    def leftRoutate(self,tree, x):
        y=x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() != None:
            y.getLeft().setP(x) #Put the left subTree of y in the right subTree of x
        y.setP(x.getP()) #Y became the son of x parent
        if x.getP() == None: #if x is the root
            tree.changeRoot(y)
        elif x == x.getP().getLeft():
            x.getP().setLeft(y)
        else:
            x.getP().setRight(y)
        y.setLeft(x)
        x.setP(y)
