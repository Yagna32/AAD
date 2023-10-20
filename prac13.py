class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left 
        self.right = right
    def children(self):
        return (self.left, self.right)
    def nodes(self):
        return (self.left, self.right) 
    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_code_tree(node,  binString=''):
    if type(node) is str:   
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l,  binString + '0')) 
    d.update(huffman_code_tree(r, binString + '1'))
    return d 

freq = {} 
lettrers = ['A','B','C','D','E','-']
prob = [0.5 ,0.35 ,0.5 ,0.1 ,0.4 ,0.2]
for c in range(len(lettrers)):
    freq[lettrers[c]] = prob[c]

freq = sorted(freq.items(), key=lambda x: x[1])    
nodes = freq 
while len(nodes) > 1:
    (key1, c1) = nodes[0]    
    (key2, c2) = nodes[1] 
    nodes = nodes[2:]                                                          
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1])
huffmanCode = huffman_code_tree(nodes[0][0]) 
print(huffmanCode)
