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


import tkinter as tk
from tkinter import messagebox

class DataStructuresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Estruturas de Dados")

        self.linked_list = LinkedList()
        self.stack = Stack()
        self.binary_tree = BinaryTree()

        self.setup_ui()

    def setup_ui(self):
        # Menu de seleção
        tk.Label(self.root, text="Escolha a Estrutura de Dados:").grid(row=0, column=0, columnspan=2)

        self.structure_var = tk.StringVar(value="Lista Ligada")
        tk.Radiobutton(self.root, text="Lista Ligada", variable=self.structure_var, value="Lista Ligada").grid(row=1, column=0)
        tk.Radiobutton(self.root, text="Pilha", variable=self.structure_var, value="Pilha").grid(row=1, column=1)
        tk.Radiobutton(self.root, text="Árvore Binária", variable=self.structure_var, value="Árvore Binária").grid(row=1, column=2)

        # Inserir e excluir dados
        tk.Label(self.root, text="Valor:").grid(row=2, column=0)
        self.input_entry = tk.Entry(self.root)
        self.input_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Inserir", command=self.insert_data).grid(row=2, column=2)

        tk.Label(self.root, text="Excluir Valor:").grid(row=3, column=0)
        self.delete_entry = tk.Entry(self.root)
        self.delete_entry.grid(row=3, column=1)
        tk.Button(self.root, text="Excluir", command=self.delete_data).grid(row=3, column=2)

        # Exibição dos dados
        self.display_label = tk.Label(self.root, text="")
        self.display_label.grid(row=4, column=0, columnspan=3)

    def insert_data(self):
        data = self.input_entry.get()
        if data.isdigit():
            data = int(data)
            selected_structure = self.structure_var.get()

            if selected_structure == "Lista Ligada":
                self.linked_list.insert(data)
                self.display_label.config(text="Lista Ligada: " + str(self.linked_list.display()))
            elif selected_structure == "Pilha":
                self.stack.push(data)
                self.display_label.config(text="Pilha: " + str(self.stack.display()))
            elif selected_structure == "Árvore Binária":
                self.binary_tree.insert(data)
                self.display_label.config(text="Árvore Binária: " + str(self.binary_tree.in_order_traversal()))

            self.input_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

    def delete_data(self):
        data = self.delete_entry.get()
        if data.isdigit():
            data = int(data)
            selected_structure = self.structure_var.get()

            if selected_structure == "Lista Ligada":
                self.linked_list.delete(data)
                self.display_label.config(text="Lista Ligada: " + str(self.linked_list.display()))
            elif selected_structure == "Pilha":
                self.stack.delete(data)
                self.display_label.config(text="Pilha: " + str(self.stack.display()))
            elif selected_structure == "Árvore Binária":
                self.binary_tree.delete(data)
                self.display_label.config(text="Árvore Binária: " + str(self.binary_tree.in_order_traversal()))

            self.delete_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructuresApp(root)
    root.mainloop()
