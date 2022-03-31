from anytree import Node, RenderTree
import json

f = open('tree.json')
json_tree = json.load(f)

tree = {}
for node in json_tree:
	if not node['parent']:
		tree[node['name']] = Node(
			node['name'],
			value=node['value'] if 'value' in node else -1
		)
	else:
		tree[node['name']] = Node(
			node['name'],
			parent=tree[node['parent']],
			value=node['value'] if 'value' in node else -1
		)

for pre, fill, node in RenderTree(tree['root']):
	print('%s%s = %s' % (pre, node.name, node.value))