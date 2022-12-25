from anytree import Node

def traverse(root):
    counter = 0
    if len(root.children) > 0:
        for child in root.children:
            counter += traverse(child)
            root.size += child.size
        if root.size <= 100000:
            counter += root.size
    return counter

# P1
cur_node = None
root = None

with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('$ cd'):
            dir_name = line[5:-1]
            if root is None:
                root = Node(dir_name, size=0)
                cur_node = root
            elif dir_name == '..':
                cur_node = cur_node.parent
            else:
                cur_node = Node(dir_name, parent=cur_node, size=0)
        elif not line.startswith('dir') and not line.startswith('$'):
            Node(line[:-1].split(' ')[1], parent=cur_node, size=int(line.split(' ')[0]))

print(traverse(root))

# P2
min_delete = root.size - 40000000

def smallest(root, min_delete, small_delete):
    if len(root.children) > 0:
        if root.size >= min_delete and root.size < small_delete:
            small_delete = root.size
        for child in root.children:
            small_delete = smallest(child, min_delete, small_delete)
    return small_delete

print(smallest(root, min_delete, 70000000))
