def solution(n):
    root = n ** 0.5
    if root == int(root):
        return (root + 1) ** 2
    return -1