class BNode:
    def __init__(self, orderM):
        self.data = [None] * (orderM + 1)
        self.subtrees = [None] * (orderM + 2)
        self.count = 0
        self.orderM = orderM

    def insert_into(self, value, index):
        j = self.count
        while j > index:
            self.data[j] = self.data[j - 1]
            self.subtrees[j + 1] = self.subtrees[j]
            j -= 1
        self.data[index] = value
        self.subtrees[index + 1] = self.subtrees[index]
        self.count += 1

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
        # binary_search
        while index < self.count and self.data[index] < value:
            index += 1

        if self.subtrees[index] == None:  # Leaf node
            self.insert_into(value, index)
        else:
            state = self.subtrees[index].insert(value)
            if state == -1:
                self.split(index)
        return -1 if self.count > self.orderM else 1