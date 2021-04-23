#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:47:43 2021

@author: matheus
"""

import tkinter as tk
from abc import ABC, abstractmethod

class Aplicacao(tk.Frame):
    
    def __init__(self, parente, *args, **kwargs):
        super().__init__(parente, *args, **kwargs)
        self._parente = parente
        self._variable = tk.StringVar()
        self.invoker = Invoker(self)
    
    def criar(self):
        tela = tk.Label(self, textvariable=self._variable)
        tela.pack()
        abrir=tk.Button(self, text='Abrir', command=(
                lambda: self.invoker.call_command(command='Abrir')))
        abrir.pack()
        fechar=tk.Button(self, text='Fechar', command=(
                lambda: self.invoker.call_command(command='Fechar')))
        fechar.pack()
        salvar=tk.Button(self, text='Salvar', command=(
                lambda: self.invoker.call_command(command='Salvar')))
        salvar.pack()
        
    def muda_tela(self, texto):
        self._variable.set(texto)
        
class Invoker(Aplicacao):
    
    def __init__(self, app):
        self.resposta = None
        self.app = app
    
    def call_command(self, command=None):
        self.resposta = eval(command)().execute()
        self.retrieve_value()
        
    def retrieve_value(self):
        self.app.muda_tela(self.resposta)
        
class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass
    
class Abrir(Command):
    
    def execute(self):
        return "O arquivo foi aberto"
    
class Salvar(Command):
    
    def execute(self):
        return "O arquivo foi salvo"
    
class Fechar(Command):
    
    def execute(self):
        return "O arquivo foi fechado"
    
janela = tk.Tk()
app = Aplicacao(janela)
app.pack()
app.criar()

janela.mainloop()


        