import random
import ABR
import RB
from timeit import default_timer as timer

ABRTree1=ABR.Tree()
ABRTree2=ABR.Tree()
ABRTree3=ABR.Tree()
ABRTreeRandom1=ABR.Tree()
ABRTreeRandom2=ABR.Tree()
ABRTreeRandom3=ABR.Tree()

RBTree1=RB.RBTree()
RBTree2=RB.RBTree()
RBTree3=RB.RBTree()
RBTreeRandom1=RB.RBTree()
RBTreeRandom2=RB.RBTree()
RBTreeRandom3=RB.RBTree()

valueList=random.sample(range(1, 1000), 50)
for i in range(50):
    ABRTree1.insert(i)
    RBTree1.insert(i)
    ABRTreeRandom1.insert(valueList[i])
    RBTreeRandom1.insert(valueList[i])

valueList=random.sample(range(1, 1000), 100)
for i in range(100):
    ABRTree2.insert(i)
    RBTree2.insert(i)
    ABRTreeRandom2.insert(valueList[i])
    RBTreeRandom2.insert(valueList[i])

valueList=random.sample(range(1, 1000), 700)
for i in range(700):
    ABRTree3.insert(i)
    RBTree3.insert(i)
    ABRTreeRandom3.insert(valueList[i])
    RBTreeRandom3.insert(valueList[i])

print("The height of 50 elements RB tree is: ", RBTree1.getRoot().height(RBTree1.getRoot()))
print("The height of 100 elements RB tree is: ", RBTree2.getRoot().height(RBTree2.getRoot()))
print("The height of 700 elements RB tree is: ", RBTree2.getRoot().height(RBTree2.getRoot()))
print("The height of 50 elements random RB tree is: ", RBTreeRandom1.getRoot().height(RBTreeRandom1.getRoot()))
print("The height of 100 elements random RB tree is: ", RBTreeRandom2.getRoot().height(RBTreeRandom2.getRoot()))
print("The height of 700 elements random RB tree is: ", RBTreeRandom3.getRoot().height(RBTreeRandom3.getRoot()))

print("The height of 50 elements standard tree is: ", ABRTree1.getRoot().height(ABRTree1.getRoot()))
print("The height of 100 elements standard tree is: ", ABRTree2.getRoot().height(ABRTree2.getRoot()))
print("The height of 700 elements standard tree is: ", ABRTree3.getRoot().height(ABRTree3.getRoot()))
print("The height of 50 elements standard random tree is: ", ABRTreeRandom1.getRoot().height(ABRTreeRandom1.getRoot()))
print("The height of 100 elements standard random tree is: ", ABRTreeRandom2.getRoot().height(ABRTreeRandom2.getRoot()))
print("The height of 700 elements standard random tree is: ", ABRTreeRandom3.getRoot().height(ABRTreeRandom3.getRoot()))

start=timer()
RBTree1.insert(10000)
end=timer()
print("Time for insert value in 50 elements RB tree is: ",end-start," seconds")

start=timer()
RBTree2.insert(10000)
end=timer()
print("Time for insert value in 100 elements RB tree is: ",end-start," seconds")

start=timer()
RBTree3.insert(10000)
end=timer()
print("Time for insert value in 700 elements RB tree is: ",end-start," seconds")

start=timer()
RBTreeRandom1.insert(10000)
end=timer()
print("Time for insert value in 50 elements random RB tree is: ",end-start," seconds")

start=timer()
RBTreeRandom2.insert(10000)
end=timer()
print("Time for insert value in 100 elements RB tree is: ",end-start," seconds")

start=timer()
RBTreeRandom3.insert(10000)
end=timer()
print("Time for insert value in 700 elements RB tree is: ",end-start," seconds")

#---------------------------!!!-----------------------#
#Now ABR
start=timer()
ABRTree1.insert(10000)
end=timer()
print("Time for insert value in 50 elements standard tree is: ",end-start," seconds")

start=timer()
ABRTree2.insert(10000)
end=timer()
print("Time for insert value in 100 elements standard tree is: ",end-start," seconds")

start=timer()
ABRTree3.insert(10000)
end=timer()
print("Time for insert value in 700 elements standard tree is: ",end-start," seconds")

start=timer()
ABRTreeRandom1.insert(10000)
end=timer()
print("Time for insert value in 50 elements standard random tree is: ",end-start," seconds")

start=timer()
ABRTreeRandom2.insert(10000)
end=timer()
print("Time for insert value in 100 elements standard random tree is: ",end-start," seconds")

start=timer()
ABRTreeRandom3.insert(10000)
end=timer()
print("Time for insert value in 700 elements standard tree is: ",end-start," seconds")