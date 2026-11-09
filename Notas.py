'''
#Operações Matemáticas e print

print("Bem vindo ao Senai")
print(1 + 3) #mais
print(10 - 5) #Menos
print(20 * 50) #Multiplicação simples
print(100 / 36) #Resultado da Divisão
print(9 ** 8) #Potenciacão
print(40 % 7) #Resto da divisão
print(47 // 2) #Resultado da divisão inteira



#Variaveis
nome= 'Kauã Kenzo Matsuo'
Idade= 30

print(f'Meu nome é {nome}, com {Idade} anos.')

#Entrada
nome= input('Digite seu nome: ')
print(f'Seu nome é {nome}')

idade_1 = input('Digite a idade 1: ')
idade_2 = input('Digite a idade 2: ')

soma_idades = idade_1 + idade_2

print(f'A soma das idades é {soma_idades}')


#Escreva um programa que leia o raio de uma esfera, e
#calcule o seu volume e área.

raio = float(input('Digite o raio: '))

Volume = (4/3) * 3.141592 * (raio ** 3)
Area = 4 * 3.141592 * (raio ** 2)

print(f'O volume é: {Volume:.2f} \nE a Área é: {round(Area, 2)}')


#Strings
senai = 'Luis Eulálio'

#Fatiamento
print(senai[5])
print(senai[0:4])
print(senai[3:])
print(senai[:9])

#Análise
print(len(senai)) #Quantas letras tem?
print(senai.count('l')) #Retorna a frequência de um determinado caractere
print(senai.find('l')) #Encontra um determinado caractere
print(senai.rfind('l')) #Encontra o caractere do final

#Transformações
print(senai.upper())
print(senai.lower())
print(senai.replace('l', 'p'))

#Entrada de dados v1
nome_completo = input('Digite seu nome completo: ').strip()

maiusculo = nome_completo.upper()
minusculo = nome_completo.lower()
letras_s = len(nome_completo.replace(' ',''))
primeiro = nome_completo.split()
p_nome = len(primeiro[0])

print(f'Em maiusculas: {maiusculo}'
      f'\nEm minusculos: {minusculo}'
      f'\nLetras sem espaço: {letras_s}'
      f'\nQnts no primeiro nome: {p_nome}')


#Entrada de dados v2
nome = input('Digite o seu nome: ').strip()

#3.1 - Tira os espaços e conta sem espaço
nome_sem_espaco = nome.replace(' ','')
quantidade_letras_sem_espaco_v1 = len(nome_sem_espaco)

#3.2 - Conta os espaços e subtrai
total_letras = len (nome)
quantidade_espacos = nome. count(' ')
quantidade_letras_sem_espaco_v2 = total_letras - quantidade_espacos

#4.1 - Encontra o primeiro espaço e conta até o primeiro espaço
posicao_primeiro_espaco = nome.find(' ')
primeiro_nome = nome[0:posicao_primeiro_espaco]
quantidade_letras_1_nome_v1 = len(primeiro_nome)

#4.2 - Encontrar o primeiro espaço, é igual encontrar a primeira palavra
quantidade_letras_1_nome_v2 = nome.find(' ')

#4.3 - Cria uma lista, e conta o primeiro da lista
lista_nomes = nome.split()
quantidade_letras_1_nome_v3 = len(lista_nomes[0])

print(f'O nome em maiusculo: {nome.upper()}'
f'\n0 nome em minusculo: {nome.lower()}'
f'\nA quantidade de letras sem espaço v1: {quantidade_letras_sem_espaco_v1}'
f'\nA quantidade de letras sem espaço v2: {quantidade_letras_sem_espaco_v2}'
f'\nA quantidade de letras no 1 nome e : {quantidade_letras_1_nome_v1}'
f'\nA quantidade de letras no 1 nome e : {quantidade_letras_1_nome_v2}'
f'\nA quantidade de letras no 1 nome é : {quantidade_letras_1_nome_v3}')


#1
altura = float(input('Digite sua altura: '))

if altura < 1.0:
    print(f'Pode entrar')
else:
    print(f'Não pode entrar')


#2
altura = float(input('Altura:'))
peso = float(input('Peso:'))

#or - OU

if altura > 1.2 and peso < 120:
    print(f'Liberado')
else:
    print(f'Não pode entrar')

#3
numero = float(input('Digite um numero: '))

if numero > 0:
    print('Positivo')
elif numero == 0:
    print('Neutro')
else:
    print('Negativo')


#Pedra, Papel e Tesoura  -------------------------------------------------------------

import random
import time


jogador = int(input(f'Digite:\n'
                      f'1-Pedra\n'
                      f'2-Papel\n'
                      f'3-Tesoura\n'
                      f'Qual a sua tentativa? '))


time.sleep(1)
print(f'JO')
time.sleep(1)
print(f'KEM')
time.sleep(1)
print(f'PO')
time.sleep(1)
print(f'Ainda pensando...')
time.sleep(1)


pc = random.randint(1,3)


print(f'Você jogou {jogador}, e o pc jogou {pc}.')


while True:
    if jogador == pc:
        print(f'Empatou')
        break
    elif jogador < 1 or jogador > 3:
        print('Seu pilantra "O", digita certo...')
        break
    if jogador == 1 and pc == 3 or jogador > pc:
        print(f'Voce ganhou!')
        break
    else:
        print(f'Voce perdeu')
        break


#for -------------------------------------------------------------

#1
for i in range(1,11):
    print('*')


#1
for i in range(1,11):
    print(i)


#1
for i in range(10,0,-1):
    print(i)

#Tabuada -------------------------------------------------------------
numero = int(input('Tabuada de qual numero?: '))

for i in range(11):
    print(f'{numero} x {i} = {numero * i}')



soma = 0

for i in range(1,6):
    n = int(input('N = '))
    soma = soma + n

print(f'A média é {soma / i}')


#from operator import add -------------------------------------------------------------

numero = int(input('Digite um numero para fatorar: '))

i = 1
fatorial = 1

while i <= numero:
    fatorial = fatorial * 1
    i += 1

print(f'O fatorial é:\n'
    f'{numero}! = {fatorial}')


#While True -------------------------------------------------------------

while True:
    n = input('Deseja continuar? [S/N]: ').strip().upper()[0]

    if n == 'N':
        break


#Meu impar ou par -------------------------------------------------------------

import random
import time


while True:
    e = input('Impar ou par? [I/P]: ').strip().upper()[0]
    while e not in 'PI':
        e = input('Impar ou par? [I/P]: ').strip().upper()[0]
    j = int(input('Digite um numero entre 1 e 10: '))
    while j < 1 or j > 10:
        j = int(input('Digite um numero entre 1 e 10: '))

    time.sleep(1)
    print('-----------------------------------------------\n'
          '---------------------IMPAR---------------------')
    time.sleep(1)
    print('-----------------------------------------------\n'
          '----------------------OU-----------------------')
    time.sleep(1)
    print('-----------------------------------------------\n'
          '----------------------PAR----------------------\n'
          '-----------------------------------------------')

    r = ''
    pc = random.randint(1,10)
    c = int((j + pc) % 2)

    if e == 'P':
        if c == 0:
            print(f'PAR - Voce ganhou!\n'
                  f'Pc:{pc} e Você:{j}.')
        else:
            print(f'PAR - Voce Perdeu!\n'
                  f'Pc:{pc} e Você:{j}.')
    elif e == 'I':
        if c != 0:
            print(f'IMPAR - Voce ganhou!\n'
                  f'Pc:{pc} e Você:{j}.')
        else:
            print(f'IMPAR - Voce Perdeu!\n'
                  f'Pc:{pc} e Você:{j}.')
    else:
        print('Algo esta errado, tente novamente.\n'
              '')

#Impar ou par do provessor ---------------------------------------

import random
vitorias = 0

while True:
escolha = input('Par ou Ímpar[P/I]: ').strip(). upper() [0]
while escolha not in 'PI':
escolha = input('Par ou İmpar[P/I]: '). strip(). upper() [0]

n = int(input('N [Digite um número entre 1 e 10]: '))
while n < 1 or n > 10:
n = int(input('N [Digite um número entre 1 e 10]: '))

pc = random. randint(1, 10)

if ((n + pc) % 2 == 0 and escolha == 'P') or ((n + pc) % 2 != 0 and escolha == 'I'):
print(f'Ganhou! - Soma - {n + pc}')
vitorias += 1
else:
print(f'Perdeu! - Soma - {n + pc} - Vitórias {vitorias}')
break

try:
    n = int(input('N: '))
    x = 10/0

except ZeroDivisionError:
    print('Não podemos dividir por 0')
except ValueError:
    print('Só aceitamos números')


while True:
    try:
        while True:
            n1 = int(input('N1: '))
            while n1 < 1:
                n1 = int(input('N1: '))
            n2 = int(input('N2: '))

            print(f'A divisão dá: {n1 / n2}')

    except ZeroDivisionError:
        print('Não pode 0')
    except ValueError:
        print('Só números')


#Funções -------------------------------------------------------------

'''
from time import process_time_ns


def quebra_de_linha():
    print('===========================================')
'''
def mensagem(x):
    quebra_de_linha()
    print(x)
    quebra_de_linha()

def area(x,y):
    return x * y

def volume(x, y, z):
    return area(x, y) * z

#Quebra_linha()
#mensagem('Bem vindo ao SENAI')
#mensagem('Bem vindo ao SENAI')
#print(area(5,8) * 5)
#print(volume(5,10,5))


 #Escreva um programa que tenha a função média(), que
 receba 5 parametros e retorne qual é a média.



def media(x, y, z, a, b):
    return (x + y + z + a) / 5


print(media(5,6,7,4,5))


#Tuplas -------------------------------------------------------------
#()
carro = ('Ferrari', 'Vermelha', 2026)

#Fatiamento
print(carro[1])
print(carro[0:2])
print(carro[-1])


#Interação
#1
for i in carro:
    print(i)

#2
for i in range(0, len(carro)):
    print(carro[i])

#3
print(enumerate(carro))

for pos, carac in enumerate(carro):
    print(f'{pos} - {carac}')

#Comandos -------------------------------------------------------------

idades = (8, 9, 22, 25, 43, 87, 65, 49)

print(max(idades))
print(min(idades))
print(sum(idades))
print((idades)/ len(idades))
print(sorted(idades))
print(sorted(idades, reverse=True))


#Filmes ---------------------------------------------------------------

filmes = ('Homem aranha','Transformers','Rei Leão','Toy story 5','007',
          'Backrooms','Devorador de estrelas','Obsseção','Odisseia')



print(f'1 - Apenas os 3 primeiros: {filmes[0:3]}\n'
      f'2 - Os 2 ultimos mais assistidos: {filmes[7:10]}\n'
      f'3 - A lista em ordem alfabética: {sorted(filmes)} \n'
      f'4 - Em que posição está o Rei Leão: {filmes.index('Rei Leão') + 1}\n')


#Filmes professor ------------------------------------------------------

#1
print(f'Os 3 primeiros mais assistidos:')
for i in range(3):
    print(filmes[i])

#2
print(f'Os 2 últimos mias assistidos:')
for i in range(-1, -3, -1):
    print(filmes[i])

#3
print(f'A lista em ordem alfabética: ')
for i in sorted(filmes):
    print(i)
#4
print(f'A posição do Rei Leão é {filmes.index('Rei Leão')}')


#Lista -----------------------------------------------------------
carro = ['Ferrari', 'Vermelha', 2026]

#Alteração
carro[1] = 'Amarelo'

#Adição
carro.insert(1,'Gasolina')
carro.append('979 cV')
print(carro)

#Remover Informações
carro.pop(4) # Remove por posição
carro.remove('Gasolina')
print(carro)

#Entrada
lista_idades = []

for i in range(5):
    lista_idades.append(int(input('N: ')))

print(lista_idades)


#Operações
a = [1,2,3]
b = [3,2,1]
print(a + b)
print(a * 2)

#Cópias de listas

a = [1,2,3]
b = a[:]

b.append(4)
print(b)
print(a)


lista_numeros = []

while True:
    try:
        i = (int(input('N: ')))

        if i < 0:
            break
        lista_numeros.append(i)

    except ValueError:
        print('só aceitamos números')


print(lista_numeros)

#Listas aninhadas ---------------------------------------

#Linha
Alunos = [['Maria', 22], ['João', 53], ['thiago', 32]]

#Acesso aos dados
#print(Alunos[1][0])

Alunos = []
dados = []

for i in range(3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    Alunos.append(dados[:])
    dados.clear()

    print(Alunos)


#Coluna
Alunos = [['Maria', 22], ['João', 53], ['thiago', 32]]
Alunos = ['Maria', 'João', 'thiago'], [22, 53, 32]

Alunos = [[], []]

for i in range(3):
    Alunos[0].append(input('Idade: '))
    Alunos[1].append(int(input('Idade: ')))

print(Alunos)


#Dicionarios -----------------------------------------------------------
df = {'Nome' : 'Luis Tatin', 'Idade' : 45}

print(df['Nome']) # Acesso à informações
df['Sexo'] = 'M'  # Inserir informações
del df['Idade']   # Remover informações

#Mostrar dados
print(df) # Retorna a estrutura completa
print(df.values()) # Retorna a apenas os valores
print(df.keys()) # retorna apenas as chaves
print(df.items()) # Retorna a estrutura completa

#Itera os valores em sequência
quebra_de_linha()
for i in df.values():
    print(i)

#Itera as chaves em sequência
quebra_de_linha()

for i in df.keys():
    print(i)

#Criação de lista auxiliar
chaves = [i for i in df.keys()]
print(chaves)


#Como fazer um dicionário
# - Lista com Dicionário
df = [{'Marca' : 'A', 'Modelo' : 'X', 'Ano' : 2000},
      {'Marca' : 'B', 'Modelo' : 'Y', 'Ano' : 2001},
      {'Marca' : 'C', 'Modelo' : 'Z', 'Ano' : 2002}]

#Exemplo Manual
df = []
carro = {}
try:
    for i in range(3):
        carro['Marca'] = input('Marca: ')
        carro['Modelo'] = input('Modelo: ')
        carro['Ano'] = input('Ano: ')

        df.append(carro.copy())

    print(df)
except ValueError:
    print('Só aceitamos números')



#2 - Dicionário com Listas --------------------------------------

df = {'Marca': ['A', 'B', 'C'],
      'Modelo': ['X', 'Y', 'Z'],
      'Ano': [2000, 2001, 2002]}

#print(f'A média é {sum(df["Ano"])/len(df["Ano"])}')
#Exemplo Manual
df = {}

#Input do dicionário com 1 linha
df['Marca'] = [input('Marca: ') for i in range(3)]
df['Modelo'] = [input('Modelo: ') for i in range(3)]
df['Ano'] = [int(input('Ano: ')) for i in range(3)]

for i, j in df.items():
    print(f'{i} - {j}')


#Exemplo compatível de uma lista

marcas = []

for i in range(3):
    marcas.append(input('Digite uma Marca: '))

df['Marca'] = marcas[:]



#Atividade ----------------------------------------------------
df = []

try:
    while True:
        pessoas = {}
        q = int(input('Quantos cadastros quer fazer?: '))
        for i in range(q):
            pessoas['Nome'] = input('Nome: ').strip().upper()
            pessoas['Sexo'] = input('Sexo: ').strip().upper()
            pessoas['Idade'] = int(input('Idade: '))

            df.append(pessoas)

        adultos = 0
        media = sum(pessoas['Idade'] for pessoas in df) / len(df)

        for pessoas['Idade'] in df:
            if pessoas['Idade'] > media:
                adultos += 1


        print(f'Atividade alunos\n'
              f'total cadastradas: {len(df)} pessoas\n'
              f'Média de idade: {sum(df['Idade'])/len(pessoas)}\n'
              f'Mulheres: {len(df['Sexo']['F'])} mulheres\n'
              f'Acima da idade: {adultos} acima da idade \n')
except ValueError:
    print('Aceitamos apenas numeros')
'''



#



















