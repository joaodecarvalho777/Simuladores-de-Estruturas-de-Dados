"""
Author: João de Carvalho & Bráulio Mac-mahon
Date: 21/06/2024

Descrição: Este aplicativo em Python utiliza Tkinter para implementar uma interface gráfica que manipula uma lista encadeada.
Ele permite inserir elementos no início, final ou em uma posição específica da lista, além de remover elementos do início,
final ou de uma posição determinada. Também oferece funcionalidades para encontrar um valor ou posição na lista encadeada,
com feedback visual atualizado em um Canvas. A aplicação utiliza caixas de diálogo para interação com o usuário, como
solicitar valores ou posições para inserção, remoção ou busca na lista encadeada.

Este código implementa uma aplicação de lista ligada utilizando Tkinter para a interface gráfica.
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

color1 = '#393946'
color2 = '#FFFFFF'

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, value, position):
        if position == 0:
            self.insert_at_start(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Posição fora dos limites")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_first(self):
        if self.head:
            self.head = self.head.next
    
    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
    
    def remove_at_position(self, position):
        if position == 0:
            self.remove_first()
            return
        current = self.head
        for _ in range(position - 1):
            if current is None or current.next is None:
                raise IndexError("Posição fora dos limites")
            current = current.next
        if current.next:
            current.next = current.next.next

    def find_value(self, value):
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1

    def find_position(self, position):
        current = self.head
        for _ in range(position):
            if current is None:
                return None
            current = current.next
        return current.value if current else None

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("Nenhum")

class LinkedListApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Linked List')
        self.canvas = tk.Canvas(master, width=855, height=400, bg=color1, highlightbackground=color1)
        self.canvas.pack()
        
        self.linked_list = LinkedList()
        
        self.insert_start_button = tk.Button(master, relief='raised', text="Inserir no início", command=self.insert_at_start)
        self.insert_start_button.pack(side=tk.LEFT)

        self.insert_end_button = tk.Button(master, text="Inserir no fim", command=self.insert_at_end)
        self.insert_end_button.pack(side=tk.LEFT)
        
        self.insert_position_button = tk.Button(master, text="Inserir na posição", command=self.insert_at_position)
        self.insert_position_button.pack(side=tk.LEFT)

        self.remove_first_button = tk.Button(master, text="Remover o primeiro", command=self.remove_first)
        self.remove_first_button.pack(side=tk.LEFT)
        
        self.remove_last_button = tk.Button(master, text="Remover o último", command=self.remove_last)
        self.remove_last_button.pack(side=tk.LEFT)
        
        self.remove_position_button = tk.Button(master, text="Remove na posição", command=self.remove_at_position)
        self.remove_position_button.pack(side=tk.LEFT)
        
        self.find_value_button = tk.Button(master, text="Encontrar pelo valor", command=self.find_value)
        self.find_value_button.pack(side=tk.LEFT)
        
        self.find_position_button = tk.Button(master, text="Encontrar pela posição", command=self.find_position)
        self.find_position_button.pack(side=tk.LEFT)

    def draw_linked_list(self, text_color=color2, arrow_color=color2):
        self.canvas.delete("all")
        current = self.linked_list.head
        x, y = 50, 50
        while current:
            self.canvas.create_rectangle(x, y, x+50, y+30, outline=color2)
            self.canvas.create_text(x+25, y+15, text=str(current.value), fill=text_color)
            if current.next:
                self.canvas.create_line(x+50, y+15, x+100, y+15, arrow=tk.LAST, fill=arrow_color)
            current = current.next
            x += 100

    def insert_at_start(self):
        value = self.get_value_from_user()
        if value is not None:
            self.linked_list.insert_at_start(value)
            self.draw_linked_list()

    def insert_at_end(self):
        value = self.get_value_from_user()
        if value is not None:
            self.linked_list.append(value)
            self.draw_linked_list()
    
    def insert_at_position(self):
        value = self.get_value_from_user()
        if value is not None:
            position = self.get_position_from_user()
            if position is not None:
                try:
                    self.linked_list.insert_at_position(value, position)
                    self.draw_linked_list()
                except IndexError as e:
                    messagebox.showerror("Erro", str(e))

    def remove_first(self):
        self.linked_list.remove_first()
        self.draw_linked_list()

    def remove_last(self):
        self.linked_list.remove_last()
        self.draw_linked_list()

    def remove_at_position(self):
        position = self.get_position_from_user()
        if position is not None:
            try:
                self.linked_list.remove_at_position(position)
                self.draw_linked_list()
            except IndexError as e:
                messagebox.showerror("Erro", str(e))
    
    def find_value(self):
        value = self.get_value_from_user()
        if value is not None:
            position = self.linked_list.find_value(value)
            if position == -1:
                messagebox.showinfo("Resultado", "Valor não encontrado")
            else:
                messagebox.showinfo("Resultado", f"Valor encontrado na posição {position}")

    def find_position(self):
        position = self.get_position_from_user()
        if position is not None:
            value = self.linked_list.find_position(position)
            if value is None:
                messagebox.showinfo("Resultado", "Posição fora dos limites")
            else:
                messagebox.showinfo("Resultado", f"Valor {value} está na posição {position}")

    def get_value_from_user(self):
        value = simpledialog.askinteger("Input", "Digite um valor:")
        return value

    def get_position_from_user(self):
        position = simpledialog.askinteger("Input", "Digite uma posição:")
        return position

root = tk.Tk()
root.config(bg=color1)
root.resizable(width=False, height=False)
app = LinkedListApp(root)
root.mainloop()