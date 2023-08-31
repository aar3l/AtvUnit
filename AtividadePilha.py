import os
import random as rd
import webbrowser

# Zhael aaron - Periodo 4 - N01
def clear():
    os.system('cls')

pilha = []

def pilhaVazia(pilha=pilha):
    if len(pilha) == 0:
        return True
    else:
        return False

for a in range(15):
    pilha.append(rd.randint(0,21))

comando1 = '''
valorAppend = input("Digite o que quer adicionar na pilha: ")
if len(str(valorAppend)) == 0:
    pass
else:
    if valorAppend.isnumeric() == True:
        pilha.append(int(valorAppend))
    else:
        pilha.append((valorAppend))'''

comando2 = '''
if pilhaVazia(pilha) == True:
    input("A pilha está vazia, digite qualquer coisa para voltar. ")
else:
    pilha.pop(-1)'''

comando3 = '''
if pilhaVazia(pilha) == True:
    input("A pilha está vazia, digite qualquer coisa para voltar. ")
else:
    print(f"Indice {len(pilha)-1}: [{pilha[-1]}]")
    input("Digite qualquer coisa para voltar. ")'''

comando4 = '''
if pilhaVazia(pilha) == True:
    input("A pilha está vazia, digite qualquer coisa para voltar. ")
else:
    for index in range(len(pilha)):
        indexReverso = len(pilha)-index-1
        print(f"Indice {indexReverso}: [{pilha[indexReverso]}]")
    input("Digite qualquer coisa para voltar. ")'''

comando5 = '''
if pilhaVazia(pilha) == True:
    input("A já pilha está vazia, digite qualquer coisa para voltar. ")
else:
    pilha = []'''

comando6 = 'ativo = False'

comandos = {
    "1":comando1,
    "empilhar":comando1,
    "2":comando2,
    "desempilhar":comando2,
    "3":comando3,
    "exibir valor no topo":comando3,
    "4":comando4,
    "exibir pilha inteira":comando4,
    "5":comando5,
    "esvaziar pilha":comando5,
    "6":comando6,
    "terminar":comando6
    }
ativo = True
while ativo == True:
    clear()
    print(pilha)
    comando = ""
    print('''
1 - Empilhar
2 - Desempilhar
3 - Exibir valor no topo
4 - Exibir pilha inteira
5 - Esvaziar pilha
6 - Terminar

''')
    comando = str(input("Digite sua opção: "))
    clear()
    try:
        exec(comandos[comando.lower()])  
    except KeyError:
        pass

webbrowser.open("https://cdn.discordapp.com/attachments/737443181439746159/1146791520062681209/upscaler-imagem_2023-08-31_095349875-2x.png")
