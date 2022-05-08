import random
from Btree import BTree


def main():
    #Create the tree
    btree = BTree(2)
    #insert random numbers to the tree
    for i in range(0, 10):
        btree.insert(random.randint(1, 200))
    #Execute the tomatrix funtion
    btree.tomatrix()


if __name__ == '__main__':
    main()