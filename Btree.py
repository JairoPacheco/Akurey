from Bnode import BNode
# class that represent the tree
class BTree:
    def __init__(self, orderM=4):
        self.orderM = orderM
        self.root = BNode(orderM)

    # this funtion call the Bnode funtion to insert a new value
    def insert(self, value):
        state = self.root.insert(value)
        # if the current node is full, it calls the split_root funtion to create a new tree
        if state == -1:
            self.split_root(self.root)

    # funtion that prints the tree an tries to create a matrix
    def tomatrix(self):
        print("****************************")
        list = print_rec(self.root, 0,[])
        print("columnas: ")
        print(list)
        print("filas: ")
        print("Lo siento no pude implementar esta parte")
        print("Para implementar la idea que tenía necesitaría un metodo buscar para obtener la referencia en el Btree de cada valor en la lista columna")
        print("Una vez tenga esto mi idea era hacer el print_rec usando de root cada una de las referencias de la lista de columnas")
        print("Entonces esto me devolvería una lista con todos los nodos hijos y tendría también los hermanos para poder crear la matriz")
        print("De igual manera creo que esto no solucionaría el problema porque sería demasiado tiempo el que tomaría para crear la matriz")
        print("De nuevo, lo siento mucho, hace mucho tiempo que no trabajo con árboles y menos con árboles de este tipo")
        print("Estoy seguro de que debe existir una manera mucho más fácil de resolverlo, sin embargo no se me ocurrió")

    # funtion that recive a node and make it into 2 new children
    def split_root(self,ptr):
        # create the 2 new nodes
        child0 = BNode(ptr.orderM)
        child1 = BNode(ptr.orderM)
        i = 0
        # get the frist values until the mid of the parent node and put them in to the new children node
        while i < ptr.orderM // 2:
            child0.subtrees[i] = ptr.subtrees[i]
            child0.data[i] = ptr.data[i]
            child0.count += 1
            i += 1
        child0.subtrees[i] = ptr.subtrees[i]
        mid = i
        # skip the middle value of the node
        i += 1  # skip
        j = 0
        # get the values after the center value of the parent node and put them on the new node
        while i < ptr.count:
            child1.subtrees[j] = ptr.subtrees[i]
            child1.data[j] = ptr.data[i]
            child1.count += 1
            j += 1
            i += 1
        child1.subtrees[j] = ptr.subtrees[i]
        # put the middle value of the parent node in the first space and add the childrens to the parent
        ptr.data[0] = ptr.data[mid]
        ptr.subtrees[0] = child0
        ptr.subtrees[1] = child1
        ptr.count = 1

# recursive print that goes to all the tree until there is no more subtrees and then it starts printing the nodes
def print_rec(ptr, level,columList):
    if ptr != None:
        i = ptr.count - 1
        while i >= 0:
            print_rec(ptr.subtrees[i + 1], level + 1,columList)
            if ptr.data[i] != None:
                columList.append(ptr.data[i])
            lastValue = 0
            for j in range(level):
                print("   ", end="")
                lastValue = lastValue + 1

            print(ptr.data[i])
            i -= 1
        print_rec(ptr.subtrees[0], level + 1, columList)
    return columList