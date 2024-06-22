"""
Author: João de Carvalho & Bráulio Mac-mahon
Date: 22/06/2024

Descrição: Este aplicativo em Python utiliza Tkinter para criar uma interface gráfica interativa para manipular
uma Árvore Binária. Ele permite inserir, remover, pesquisar e percorrer a árvore (em ordem, pré-ordem e pós-ordem).
A árvore é desenhada visualmente na tela, usando círculos para nós e linhas para conexões entre eles. Os botões na
interface acionam ações correspondentes na estrutura da árvore, atualizando a visualização conforme as operações
são executadas.

Este código implementa uma aplicação de árvore binária utilizando Tkinter para a interface gráfica.
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

color1 = '#393946'
color2 = '#FFFFFF'

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete(self.root, key)
        if not deleted:
            raise ValueError(f"O valor {key} não foi encontrado na árvore")

    def _delete(self, root, key):
        if root is None:
            return root, False  # Adicionar retorno de indicador de falha

        if key < root.val:
            root.left, deleted = self._delete(root.left, key)
        elif key > root.val:
            root.right, deleted = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right, True
            elif root.right is None:
                return root.left, True

            temp_val = self._min_value_node(root.right)
            root.val = temp_val.val
            root.right, _ = self._delete(root.right, temp_val.val)
            return root, True

        return root, deleted

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        res = []
        if node:
            res = self._inorder(node.left)
            res.append(node.val)
            res = res + self._inorder(node.right)
        return res

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        res = []
        if node:
            res.append(node.val)
            res = res + self._preorder(node.left)
            res = res + self._preorder(node.right)
        return res

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        res = []
        if node:
            res = self._postorder(node.left)
            res = res + self._postorder(node.right)
            res.append(node.val)
        return res

class BinaryTreeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary Tree")
        self.center_window()
        self.canvas = tk.Canvas(master, width=800, height=600, bg=color1, highlightbackground=color1)
        self.canvas.pack()

        self.tree = BinaryTree()

        control_frame = tk.Frame(master, bg=color1)
        control_frame.pack()

        self.insert_button = tk.Button(control_frame, text="Inserir", command=self.insert, bg='#4caf50', fg='white')
        self.insert_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(control_frame, text="Remover", command=self.delete, bg='#f44336', fg='white')
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.search_button = tk.Button(control_frame, text="Pesquisar", command=self.search, bg='#2196f3', fg='white')
        self.search_button.grid(row=0, column=3, padx=5, pady=5)

        self.inorder_button = tk.Button(control_frame, text="Em ordem", command=self.inorder, bg='#ffc107', fg='black')
        self.inorder_button.grid(row=0, column=4, padx=5, pady=5)

        self.preorder_button = tk.Button(control_frame, text="Pré-ordem", command=self.preorder, bg='#ffc107', fg='black')
        self.preorder_button.grid(row=0, column=5, padx=5, pady=5)

        self.postorder_button = tk.Button(control_frame, text="Pós-ordem", command=self.postorder, bg='#ffc107', fg='black')
        self.postorder_button.grid(row=0, column=6, padx=5, pady=5)

        self.draw_tree()

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root:
            self._draw_tree(self.tree.root, 400, 50, 200)

    def _draw_tree(self, node, x, y, dx):
        if node:
            if node.left:
                self.canvas.create_line(x, y, x-dx, y+60, fill='#ffffff')
                self._draw_tree(node.left, x-dx, y+60, dx//2)
            if node.right:
                self.canvas.create_line(x, y, x+dx, y+60, fill='#ffffff')
                self._draw_tree(node.right, x+dx, y+60, dx//2)
            self.canvas.create_oval(x-15, y-15, x+15, y+15, outline='#ffffff', fill='#3f51b5')
            self.canvas.create_text(x, y, text=str(node.val), fill='#ffffff')

    def insert(self):
        value = self.get_value_from_user()
        if value is not None:
            self.tree.insert(value)
            self.draw_tree()

    def delete(self):
        value = self.get_value_from_user()
        if value is not None:
            try:
                self.tree.delete(value)
                self.draw_tree()
            except ValueError as e:
                messagebox.showerror("Error", str(e))


    def search(self):
        value = self.get_value_from_user()
        if value is not None:
            result = self.tree.search(value)
            if result:
                messagebox.showinfo("Resultado da pesquisa", f"O valor {value} foi encontrado na árvore.")
            else:
                messagebox.showinfo("Resultado da pesquisa", f"O Valor {value} não foi encontrado na árvore.")

    def inorder(self):
        result = self.tree.inorder()
        messagebox.showinfo("Travessia em Ordem", f"Em ordem: {result}")

    def preorder(self):
        result = self.tree.preorder()
        messagebox.showinfo("Travessia em Pré-ordem", f"Pré-ordem: {result}")

    def postorder(self):
        result = self.tree.postorder()
        messagebox.showinfo("Travessia Pós-ordem", f"Pós-ordem: {result}")

    def get_value_from_user(self):
        value = simpledialog.askinteger("Input", "Digite um valor:")
        return value

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x645')
    root.config(bg=color1)
    app = BinaryTreeApp(root)
    root.mainloop()