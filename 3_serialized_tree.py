""" 
    Problem: 
        Given the root to a binary tree, 
        implement serialize(root), 
        which serializes the tree into a string, and deserialize(s), 
        which deserializes the string back into the tree.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# String -> Tree
def deserialize(data):
    def helper():
        #Get the next node
        val = next(vals)
        #If its #, then is an empty node
        if val == '#':
            return None
        node = Node(val)
        #Recursively call helper for left child
        node.left = helper()
        #Recursively call helper for right child
        node.right = helper()
        return node
    #Generate an iterator over the list of values
    vals = iter(data.split())
    return helper()

# Tree -> String
def serialize(tree):
    #Base case
    if not tree:
        #In case some child is None
        return '#'
    return '{} {} {}'.format(tree.val, serialize(tree.left), serialize(tree.right))

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
