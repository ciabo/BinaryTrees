import ABR
import RB


MyRBTree=ABR.Tree()
for i in range(1001):
    MyRBTree.insert(i)

#test=MyRBTree.treeSearch(3,MyRBTree.getRoot())
#MyRBTree.rightRotation(MyRBTree,test)
#print("Radice: ",MyRBTree.getRoot().getKey())
MyRBTree.inorder()
print("height: ",MyRBTree.getRoot().height(MyRBTree.getRoot()))

