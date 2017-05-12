import random
import ABR
import RB
from timeit import default_timer as timer

ranges=[50,100,700]
randValueList=[random.sample(range(1, 1000), 50) , random.sample(range(1, 1000), 100) , random.sample(range(1, 1000), 700)]

for r in range(0,3):
    ABRTree = ABR.Tree()
    ABRTreeRandom = ABR.Tree()
    RBTree = RB.RBTree()
    RBTreeRandom = RB.RBTree()
    for i in range(0,ranges[r]):
        ABRTree.insert(i)
        ABRTreeRandom.insert(randValueList[r][i])
        RBTree.insert(i)
        RBTreeRandom.insert(randValueList[r][i])

    print("The height of ", ranges[r], " elements standard tree is: ", ABRTree.getRoot().height(ABRTree.getRoot()))
    start = timer()
    ABRTree.insert(10000)
    end = timer()
    print("And the time for insert a value is: ", end - start, " seconds")
    print("The height of ", ranges[r], " elements random tree is: ", ABRTreeRandom.getRoot().height(ABRTreeRandom.getRoot()))
    start = timer()
    ABRTreeRandom.insert(10000)
    end = timer()
    print("And the time for insert a value is: ", end - start, " seconds")
    print("The height of ", ranges[r], " elements RB tree is: ", RBTree.getRoot().height(RBTree.getRoot()))
    start = timer()
    RBTree.insert(10000)
    end = timer()
    print("And the time for insert a value is: ", end - start, " seconds")
    print("The height of ", ranges[r], " elements random RB tree is: ", RBTreeRandom.getRoot().height(RBTreeRandom.getRoot()))
    start = timer()
    RBTreeRandom.insert(10000)
    end = timer()
    print("And the time for insert a value is: ", end - start, " seconds")
    print("")