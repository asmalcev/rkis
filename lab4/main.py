from cmath import inf
from anytree import Node, RenderTree
import json
from sys import argv

from minmax import minmax, metrics as m1
from minmax_ab import minmax_ab, metrics as m2

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


is_first_step_max = (
	True
	if len(argv) < 2
	else argv[1] == 'max'
)
is_ab = (
	False
	if len(argv) < 3
	else argv[2] == 'ab'
)
is_reverse = (
	False
	if len(argv) < 4
	else argv[3] == 'reverse'
)

if is_ab:
	minmax_ab(tree['root'], is_first_step_max, -inf, +inf, reversed_children=is_reverse)
	print('Количество посещенных вершин: %d' %  (m2['nodes']))
else:
	minmax(tree['root'], is_first_step_max, reversed_children=is_reverse)
	print('Количество посещенных вершин: %d' %  (m1['nodes']))

for pre, fill, node in RenderTree(tree['root']):
	print('%s%s = %s' % (pre, node.name, node.value))
