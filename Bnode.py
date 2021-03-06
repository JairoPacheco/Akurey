# class that represents the nodes in the tree
class BNode:
    def __init__(self, orderM):
        self.data = [None] * (orderM + 1) #keys
        self.subtrees = [None] * (orderM + 2)
        self.count = 0
        self.orderM = orderM

    # this funtion inserts the value in the index we want and increase count, that is the number of elements tha are in the current node
    def insert_into(self, value, index):
        j = self.count
        while j > index:
            self.data[j] = self.data[j - 1]
            self.subtrees[j + 1] = self.subtrees[j]
            j -= 1
        self.data[index] = value
        self.subtrees[index + 1] = self.subtrees[index]
        self.count += 1

    # is very similar to the split root but this one is use when the split is been done to a children of a node
    def split(self, index):
        ptr = self.subtrees[index]
        child0 = BNode(ptr.orderM)
        child1 = BNode(ptr.orderM)
        i = 0
        while i < ptr.orderM // 2:
            child0.subtrees[i] = ptr.subtrees[i]
            child0.data[i] = ptr.data[i]
            child0.count += 1
            i += 1
        child0.subtrees[i] = ptr.subtrees[i]
        mid = i
        i += 1  # skip
        j = 0
        while i < ptr.count:
            child1.subtrees[j] = ptr.subtrees[i]
            child1.data[j] = ptr.data[i]
            child1.count += 1
            j += 1
            i += 1
        child1.subtrees[j] = ptr.subtrees[i]

        self.insert_into(ptr.data[mid], index)
        self.subtrees[index] = child0
        self.subtrees[index + 1] = child1

    def insert(self, value):
        index = 0
        # it goes through the current node until it finds the position where the new value should be
        while index < self.count and self.data[index] < value:
            index += 1
        # if his childrens are none the call insert_into
        if self.subtrees[index] == None:  # Leaf node
            self.insert_into(value, index)
        # call this if we need to split a children node
        else:
            state = self.subtrees[index].insert(value)
            if state == -1:
                self.split(index)
        # if the current node has more elements than what he shout we return a -1 and make the split
        return -1 if self.count > self.orderM else 1