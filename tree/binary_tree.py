'''
Binary Tree
'''

def binary_tree_list(root):
    return [root, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1,[new_branch, [], []])
    return root

def insert_right(root, new_branch):
    pass
