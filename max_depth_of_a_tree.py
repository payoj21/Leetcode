def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # DFS
    max_depth = [0]

    def depth(node, node_depth):
        if not node:
            return node_depth
        node_depth += 1
        if node_depth > max_depth[0]:
            max_depth[0] = node_depth
        depth(node.left, node_depth)
        depth(node.right, node_depth)

    depth(root, 0)
    return max_depth[0]