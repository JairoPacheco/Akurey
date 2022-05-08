import random
from Btree import BTree


def main():
    btree = BTree(2)
    for i in range(0, 10):
        btree.insert(random.randint(1, 200))
    btree.tomatrix()


if __name__ == '__main__':
    main()