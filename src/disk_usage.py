def total_size(node):
    if node is None:
        return 0

    if node.get("type") == "file":
        return node.get("size", 0)

    if node.get("type") == "dir":
        total = 0
        for child in node.get("children", []):
            total += total_size(child)
        return total

    return 0
