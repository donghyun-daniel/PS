class Node:
    def __init__(self, item, lc, rc):
        self.item = item
        self.lc=lc
        self.rc=rc

def preorder(node):
    print(node.item, end='')
    if node.lc!='.':
        preorder(tree[node.lc])
    if node.rc!='.':
        preorder((tree[node.rc]))

def inorder(node):
    if node.lc != '.':
        inorder(tree[node.lc])
    print(node.item, end='')
    if node.rc != '.':
        inorder((tree[node.rc]))

def postorder(node):
    if node.lc != '.':
        postorder(tree[node.lc])
    if node.rc != '.':
        postorder((tree[node.rc]))
    print(node.item, end='')


N=int(input())
tree={}
for i in range(N):
    s,l,r = input().split()
    tree[s]=Node(s, l, r)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])