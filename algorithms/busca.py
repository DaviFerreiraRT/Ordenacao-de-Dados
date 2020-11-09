import Node
import Tree
def busca_iterativa(self, key: int):
    return self._busca_iterativa(self.root, key)


def _busca_iterativa(self, node: Node, key: int):
    if node != None:
        current_node = node
        while current_node != None:
            print("Chave visitada :{}".format(current_node.key))
            if  node.actual.key == key:
                return True
            elif key <= current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
if __name__ == "__main__":
    lista=[115,98,34,56,25,95,25,132,130,133]
    testes=[115,34]

    arvore=Tree()
    busca_iterativa=34
    for i in lista:
        arvore.insert(i)
    print("Árvore Imprimida: \n")
    arvore.print_tree(arvore.root)

    
    