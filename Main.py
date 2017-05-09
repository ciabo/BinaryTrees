import ABR
import RB


MyRBTree=RB.RBTree()
MyRBTree.insert(3)
MyRBTree.insert(1)
MyRBTree.insert(2)
MyRBTree.insert(7)
MyRBTree.insert(5)
MyRBTree.insert(9)
test=MyRBTree.treeSearch(3,MyRBTree.getRoot())
MyRBTree.leftRoutate(MyRBTree,test)
print("Radice: ",MyRBTree.getRoot().getKey())
MyRBTree.inorder()
