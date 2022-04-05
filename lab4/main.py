from cmath import inf
from anytree import Node, RenderTree
import json

f = open('tree.json')
json_tree = json.load(f)

tree = {}
for node in json_tree:
	if not node['parent']:
		tree[node['name']] = Node(
			node['name'],
			value=node['value'] if 'value' in node else None
		)
	else:
		tree[node['name']] = Node(
			node['name'],
			parent=tree[node['parent']],
			value=node['value'] if 'value' in node else None
		)


is_first_step_max = False

metric = 0

def minmax(node, maximazing):
	global metric
	metric += 1

	if node.value is not None:
		return node.value

	children_values = [minmax(inode, level + 1) for inode in node.children]
	node.value = (
		max(children_values) if level % 2 == int(not is_first_step_max)
		else min(children_values)
	)
	return node.value

minmax(tree['root'], 0)

# def minmax_ab(node, level, alpha, beta):
# 	global metric
# 	metric += 1

# 	if node.value is not None:
# 		return node.value

# 	children_values = [minmax(inode, level + 1) for inode in node.children]

# 	if level % 2 == int(not is_first_step_max):
# 		node.value = ( max(children_values) )
# 	else:
# 		node.value = ( min(children_values) )
# 	return node.value

# minmax_ab(tree['root'], 0, +inf, -inf)


print(metric)
print('FIRST', 'MAX' if is_first_step_max else 'MIN')
for pre, fill, node in RenderTree(tree['root']):
	print('%s%s = %s' % (pre, node.name, node.value))