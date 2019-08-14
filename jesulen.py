class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 1

    def __str__(self):
        return str(self.key)
        
class rbTree():
    def __init__(self):
        self.null = Node('null')
        self.null.color = 1
        self.root = self.null.parent = self.null.left = self.null.right = self.null
       
    def search(self, key):
        '''Receives an key and return the respective node if it's on tree, and self.null if isn't.'''
        i = self.root
        while i != self.null and key != i.key:
            if key < i.key:
                i = i.left
            else:
                i = i.right
        return i

    def inOrder(self, node):
        '''Run across the tree and print its data in order, recursively'''
        if node != self.null:
            self.inOrder(node.left)
            print(node)
            self.inOrder(node.right)

    def minimum(self, i):
        '''Returns the node with the lowest key after the node that was informed.'''
        while i.left != self.null:
            i = i.left
        return i

    def leftRotate(self, x):
        '''Receveis a node (x), and rotates it to left of node (y), becoming its left son.'''
        y = x.right
        x.right = y.left

        if y.left != self.null:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.null:
            self.root = y

        elif x is x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rightRotate(self, x):
        '''Receives a node (x), and rotates it to left of a node (y), becoming its right son.'''
        y = x.left
        x.left = y.right

        if y.right != self.null:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == self.null:
            self.root = y

        elif x is x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def insertFixUp(self, z):
        '''Receives a node and fix its position, color and your ancestral color and position, if it is necessary.'''
        while z.parent.color == 0:

            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right 

                if y.color == 0:

                    z.parent.color = 1
                    y.color = 1
                    z.parent.parent.color = 0
                    z = z.parent.parent

                elif y.color == 1:

                    if z is z.parent.right:
                        z = z.parent
                        self.leftRotate(z)

                    if z is z.parent.left:
                        z.parent.color = 1
                        z.parent.parent.color = 0
                        self.rightRotate(z.parent.parent)

            elif z.parent is z.parent.parent.right:
                y = z.parent.parent.left

                if y.color == 0:

                    z.parent.color = 1
                    y.color = 1
                    z.parent.parent.color = 0
                    z = z.parent.parent

                elif y.color == 1:

                    if z is z.parent.left:
                        z = z.parent
                        self.rightRotate(z)

                    if z is z.parent.right:
                        z.parent.color = 1
                        z.parent.parent.color = 0
                        self.leftRotate(z.parent.parent)

        self.root.color = 1 

    def insert(self, key):
        '''Insert a new node into a red black tree.'''
        z = Node(key)
        y = self.null
        x = self.root

        while x != self.null:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.null:
            self.root =z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.null
        z.right = self.null
        z.color = 0
        
        self.insertFixUp(z)

    def transplant(self, u, v):
        '''Receives a node (or subtree) u, and substitutes this node (or subtree) for the node (or tree) v.'''
        if u.parent == self.null:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def deleteFixUp(self, x):
        '''Fix the first, second, and fourth proprieties of red black tree, after a deletion has occurred.'''
        while x != self.root and x.color == 1:
            
            if x is x.parent.left:
                w = x.parent.right

                if w.color == 0:
                    w.color = 1
                    x.parent.color = 0
                    self.leftRotate(x.parent)
                    w = x.parent.right

                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.parent

                elif w.right.color == 1:
                    w.left.color = 1
                    w.color = 0
                    self.rightRotate(w)
                    w = x.parent.right

                elif w.right.color == 0:
                    w.color = x.parent.color
                    x.parent.color = 1
                    w.right.color = 1
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left

                if w.color == 0:
                    w.color = 1
                    x.parent.color = 0
                    self.rightRotate(x.parent)
                    w = x.parent.left

                if w.right.color == 1 and w.left.color == 1:
                    w.color = 0
                    x = x.parent

                elif w.left.color == 1:
                    w.right.color = 1
                    w.color = 0
                    self.leftRotate(w)
                    w = x.parent.left

                elif w.left.color == 0:
                    w.color = x.parent.color
                    x.parent.color = 1
                    w.left.color = 1
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 1

    def delete(self, z):
        '''Receives a Node object and delete it from its tree.'''
        y = z
        y_original_color = y.color
        
        if z.left == self.null:
            x = z.right
            self.transplant(z, z.right)

        elif z.right == self.null:
            x = z.left
            self.transplant(z, z.left)

        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right 

            if y.parent == z:
                x.parent = y 

            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left 
            y.left.parent = y
            y.color = z.color 

        if y_original_color == 1:
            self.deleteFixUp(x)

class arvoreTitulos:
    def __init__(self):
        self.titulos_cadastrados = rbTree()

    def cadastrar_titulo(self, titulo):
        if self.titulos_cadastrados.search(titulo) is self.titulos_cadastrados.null:
            self.titulos_cadastrados.insert(titulo)
        else:
            print('Erro: Título Eleitoral informado já se encontra cadastrado.')

    def listar_titulos(self):
        if self.titulos_cadastrados.root is self.titulos_cadastrados.null:
            print('Não constam títulos na árvore.')
        else:
            self.titulos_cadastrados.inOrder(self.titulos_cadastrados.root)

    def descadastrar_titulo(self, titulo):
        titulo = self.titulos_cadastrados.search(titulo)
        if titulo is not self.titulos_cadastrados.null:
            self.titulos_cadastrados.delete(titulo)
        else:
            print('Erro: Título Eleitoral informado não consta no cadastro.')

class Candidatos:
    def __init__(self):
        self.candidatos_cadastrados = {'Nulos': 0}

    def __str__(self):
        candidatos_atuais = []
        for i in self.candidatos_cadastrados:
            if i != 'Nulos':
                candidatos_atuais.append('Candidato: {}, Número: {}'.format(self.candidatos_cadastrados.get(i)[0], i))
        return str('\n'.join(candidatos_atuais))

    def cadastrar_candidato(self, candidato, numero):
        if self.candidatos_cadastrados.get(numero) is None:
            self.candidatos_cadastrados[numero] = [candidato, 0]
        else:
            print('Erro: Número de candidato já cadastrado. Escolha outro número.')

class Votacao:
    def __init__(self, arvore_titulos):
        self.arvore_votacao_atual = rbTree()
        self.candidatos = Candidatos()
        self.database_de_titulos = arvore_titulos

    def adicionar_voto(self, titulo, voto):

        if self.database_de_titulos.titulos_cadastrados.search(titulo) is not self.database_de_titulos.titulos_cadastrados.null:
            if self.arvore_votacao_atual.search(titulo) is self.arvore_votacao_atual.null:
                
                if self.candidatos.candidatos_cadastrados.get(voto) is not None:
                    self.candidatos.candidatos_cadastrados[voto][1] += 1
                    self.arvore_votacao_atual.insert(titulo)
                else:
                    self.candidatos.candidatos_cadastrados['Nulos'] += 1
                    self.arvore_votacao_atual.insert(titulo)
            else:
                print('Erro: Título informado já realizou votação.') 
        else:
            print('Erro: Título informado não está registrado.')

    def __str__(self):
        votacao_parcial = []
        for i in self.candidatos.candidatos_cadastrados:
            if i != 'Nulos':
                votacao_parcial.append('Candidato: {}, Número: {}, Votos: {}'.format(self.candidatos.candidatos_cadastrados.get(i)[0], i, self.candidatos.candidatos_cadastrados.get(i)[1]))
            else:
                votacao_parcial.append('Votos nulos: {}'.format(self.candidatos.candidatos_cadastrados.get(i)))

        return str('\n'.join(votacao_parcial))

    def resultado_parcial(self):
        print(self)

    def resetar_votacao_atual(self):
        self.arvore_votacao_atual = rbTree()

'''
############# Criando Títulos Eleitorais Aleatórios #################
titulos_eleitorais = [i for i in range(5000000, 5005000)]
import random
random.shuffle(titulos_eleitorais)

database = arvoreTitulos()
for i in titulos_eleitorais:
    database.cadastrar_titulo(i)


############# Criando a Árvore de Votação e Adicionando os Candidados ################
votação_atual = Votacao(database)

votação_atual.candidatos.cadastrar_candidato('Biroliro', 17)
votação_atual.candidatos.cadastrar_candidato('Luladraoroboumeucoracao', 13)
print(votação_atual.candidatos)

titulos_que_vao_votar = []
for i in range(500):
    titulos_que_vao_votar.append(random.randint(5000000, 5005000))
    #lista randomica gerada, podem haver títulos randômicos repetidos o que significaria que alguém já votou com o título em questão

votos = [13, 17, 00]

############# Adicionando os Votos na Árvore de Votação ##########################
for i in titulos_que_vao_votar:
    random.shuffle(votos) #o voto é aleatório, já que o shuffle randomiza a lista de votos possíveis
    votação_atual.adicionar_voto(i, votos[0]) #i é o título votante, 

############ Tentando Realizar Votação com Títulos Inexistentes ##################

for i in range(6000000, 6000005):
    random.shuffle(votos)
    votação_atual.adicionar_voto(i, votos[0])

print(votação_atual.resultado_parcial())

############ Descadastrando TODOS os títulos ########################
for i in titulos_eleitorais:
    database.descadastrar_titulo(i)

database.listar_titulos()
'''
import random
import sys
# -*- coding: latin-1 -*-
# coding: utf-8

Titulos = arvoreTitulos()
votação_atual = Votacao(Titulos)
print("Eleições - Contagem e Checagem de Votos")

def menu():                                       
    while True:
        print('''
                MENU
            
                [1]Cadastramento de Titulos de Eleitor
                [2]Votação
                [3]Cadastrar Candidatos
                [4]Sair do Programa
                ''')

        op = int(input("Qual é a opção desejada? \n"))

        if op == 1:
            menu_cadastrar()
        elif op == 2:
            menu_votação()
        elif op == 3:
            while True:
                candidato=input('Digite o nome do candidato a ser cadastrado(0 para voltar):\n')
                if candidato=='0':
                    menu()
                numero=int(input('Digite o número do candidato a ser cadastrado:\n'))
                votação_atual.candidatos.cadastrar_candidato(candidato,numero)
        elif op == 4:
            print("Finalizando...")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente")

def menu_cadastrar():                
    while True:
        print('''
                CADASTRAR
                
                [1]Cadastrar Título
                [2]Descadastrar Título
                [3]Carregar Título
                [4]Voltar
                ''')
        op = int(input("Qual é a opção desejada? \n"))                # Aqui ocorrerá o cadastramento dos títulos
        if op == 1:
            while True:
                titulo=int(input('Digite um título a ser cadastrado(0 para voltar):\n'))
                if titulo == 0:
                    menu_cadastrar()
                Titulos.cadastrar_titulo(titulo)
        elif op == 2:                                                
            while True:
                titulo=int(input('Digite um título a ser descadastrado(0 para voltar):\n'))
                if titulo == 0:
                    menu_cadastrar()
                Titulos.descadastrar_titulo()
        elif op == 3:                                                 # Carregar a árvore com títulos aleatórios
            titulosgerados = [i for i in range(5000000, 5000500)]
            random.shuffle(titulosgerados)
            for i in titulosgerados:
                Titulos.cadastrar_titulo(i)
        elif op == 4:
            menu()
        else:
            print("Opção inválida. Tente novamente")

def menu_votação():
    while True:
        print('''
                VOTAÇÃO
                
                [1]Nova Votação
                [2]Adicionar Voto           
                [3]Gerar voto aleatório    
                [4]Resultado Parcial        
                [5]Listar títulos 
                [6]Voltar
                ''')
        ### APARECE NONE E TEM Q PEGAR OS TITULOS DA ÁRVORE (GERAR VOTO ALEATÓRIO)
        op = int(input("Qual é a opção desejada? \n"))

        if op == 1:
            votação_atual.resetar_votacao_atual()
        elif op == 2:
            while True:
                titulo=int(input('Digite o título a realizar o voto(0 para voltar):\n'))
                if titulo==0:
                    menu_votação()
                voto=int(input('Digite o voto a ser computado:\n'))
                votação_atual.adicionar_voto(titulo,voto)
        elif op == 3:
            opções=[0]
            for i in votação_atual.candidatos.candidatos_cadastrados:
                if i != "Nulos":
                    opções.append(i)
            titulos = [i for i in range(5000000, 5000500)]
            for i in titulos:
                random.shuffle(opções) 
                votação_atual.adicionar_voto(i, opções[0]) 
            #
        elif op == 4:
            print(votação_atual.resultado_parcial())
        elif op == 5:
            Titulos.listar_titulos()
        elif op == 6:
            menu()
        else:
            print("Opção inválida. Tente novamente")
menu()
