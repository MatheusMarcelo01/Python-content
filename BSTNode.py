class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
        
        root = BSTNode(42) #cria um nó, no caso "42"
        root.left = BSTNode(10)       #cria um nó filho a esquerda '10'
        root.right = BSTNode(90)      #cria um nó filho a direita '90'
        root.left.left = BSTNode(2)    #cria um filho para o nó da esquerda, no caso '10', no valor '2'
        
        #a seguir implementação de busca:
        
        class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
 
    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self
