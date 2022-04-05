from cmath import inf

metrics = {
	'nodes': 0
}

def prun_branch(node):
	node.value = 'pruned'
	for inode in node.children:
		prun_branch(inode)

def minmax_ab(node, maximazing, alpha, beta, reversed_children=False):
	metrics['nodes'] += 1

	if node.value is not None:
		return node.value

	if maximazing:
		maxValue = -inf
		is_break = False
		for inode in node.children if not reversed_children else node.children[::-1]:
			if is_break:
				prun_branch(inode)
			else:
				value = minmax_ab(inode, not maximazing, alpha, beta, reversed_children=reversed_children)
				maxValue = max(maxValue, value)

				alpha = max(alpha, value)
				if beta <= alpha:
					is_break = True

		node.value = maxValue
	else:
		minValue = +inf
		is_break = False
		for inode in node.children if not reversed_children else node.children[::-1]:
			if is_break:
				prun_branch(inode)
			else:
				value = minmax_ab(inode, not maximazing, alpha, beta, reversed_children=reversed_children)
				minValue = min(minValue, value)

				beta = min(beta, value)
				if beta <= alpha:
					is_break = True

		node.value = minValue

	return node.value