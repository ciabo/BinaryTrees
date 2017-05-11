import ABR
import RB


MyRBTree=RB.RBTree()
MyRBTree.insert(3)
MyRBTree.insert(1)
MyRBTree.insert(7)
MyRBTree.insert(2)

#test=MyRBTree.treeSearch(3,MyRBTree.getRoot())
#MyRBTree.rightRotation(MyRBTree,test)
#print("Radice: ",MyRBTree.getRoot().getKey())
MyRBTree.inorder()

