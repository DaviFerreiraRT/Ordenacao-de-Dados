import Node
class Tree(object):
    def __init__(self):
        self.root = None
        self.number_of_spaces = 10

    def insert(self, key):
        node = Node(key)

        if self.root == None:
            self.root = node
        else:
            current = self.root
            while True:
                previus = current
                if key <= current.key:
                    current = current.left
                    if current == None:
                        previus.left = node
                        break
                else:
                    current = current.right
                    if current == None:
                        previus.right = node
                        break
