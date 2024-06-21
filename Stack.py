"""
Author: João de Carvalho & Bráulio Mac-mahon
Date: 22/06/2024

Descrição: Este aplicativo em Python com Tkinter simula operações de uma pilha. Permite inserir elementos (push),
remover o último inserido (pop) e visualizar o elemento no topo (peek). A interface gráfica usa botões para interação
e um Canvas para representar visualmente os elementos da pilha. Caixas de diálogo fornecem feedback e interação para
entrada de valores. Ideal para aprendizado de estruturas de dados básicas de forma interativa e visualmente intuitiva.

Este código implementa uma aplicação de pilhas utilizando Tkinter para a interface gráfica.
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

color1 = '#393946'
color2 = '#FFFFFF'

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Remover de uma pilha vazia")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Ver elemento no topo")

    def is_empty(self):
        return len(self.items) == 0

class StackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Operações de pilha")
        self.canvas = tk.Canvas(master, width=200, height=300, bg=color1, highlightbackground=color1)
        self.canvas.pack()

        self.stack = Stack()

        self.push_button = tk.Button(master, width=10, font='Arial 15', text="Push", command=self.push)
        self.push_button.pack(side=tk.LEFT)

        self.pop_button = tk.Button(master, width=10, font='Arial 15', text="Pop", command=self.pop)
        self.pop_button.pack(side=tk.LEFT)

        self.peek_button = tk.Button(master, width=10, font='Arial 15', text="Peek", command=self.peek)
        self.peek_button.pack(side=tk.LEFT)

        self.draw_stack()

    def draw_stack(self, text_color=color2):
        self.canvas.delete("all")
        x, y = 100, 50
        for item in reversed(self.stack.items):
            self.canvas.create_rectangle(x-25, y-15, x+25, y+15, outline=color2)
            self.canvas.create_text(x, y, text=str(item), fill=text_color)
            y += 30

    def push(self):
        value = self.get_value_from_user()
        if value is not None:
            self.stack.push(value)
            self.draw_stack()

    def pop(self):
        try:
            self.stack.pop()
            self.draw_stack()
        except IndexError as e:
            messagebox.showerror("Erro", str(e))

    def peek(self):
        try:
            value = self.stack.peek()
            messagebox.showinfo("Valor do Topo", f"O valor do topo é {value}")
        except IndexError as e:
            messagebox.showerror("Erro", str(e))

    def get_value_from_user(self):
        value = simpledialog.askinteger("Input", "Digite um valor:")
        return value

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg=color1)
    root.resizable(width=False, height=False)
    app = StackApp(root)
    root.mainloop()