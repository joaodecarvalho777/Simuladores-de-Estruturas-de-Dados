class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def delete(self, data):
        if not self.top:
            return

        if self.top.data == data:
            self.top = self.top.next
            return

        current = self.top
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        nodes = []
        current = self.top
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.data < current.data:
            if not current.left:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if not current.right:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, root, data):
        if not root:
            return root

        if data < root.data:
            root.left = self._delete_recursive(root.left, data)
        elif data > root.data:
            root.right = self._delete_recursive(root.right, data)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_larger_node = self._get_min(root.right)
            root.data = min_larger_node.data
            root.right = self._delete_recursive(root.right, min_larger_node.data)

        return root

    def _get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def in_order_traversal(self):
        nodes = []
        self._in_order_traversal_recursive(self.root, nodes)
        return nodes

    def _in_order_traversal_recursive(self, node, nodes):
        if node:
            self._in_order_traversal_recursive(node.left, nodes)
            nodes.append(node.data)
            self._in_order_traversal_recursive(node.right, nodes)