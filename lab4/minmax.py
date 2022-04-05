metrics = {
	'nodes': 0
}

def minmax(node, maximazing, reversed_children=False):
	metrics['nodes'] += 1

	if node.value is not None:
		return node.value

	children_values = [
		minmax(inode, not maximazing, reversed_children=reversed_children)
		for inode in
		(
			node.children[::-1] if reversed_children
			else node.children
		)
	]

	if maximazing:
		node.value = max(children_values)
	else:
		node.value = min(children_values)

	return node.value