from deputado import *
from partido import *
import os

def escrever(titulo, texto):
    print(f"{'#'*20}{'['+titulo+']'}{'#'*20}")
    print(texto)
    print(f"{'#'*20}{'#'*len('['+titulo+']')}{'#'*20}")

def isInLista(lista, verificar, opcao):
    for cont, item in enumerate(lista):
        if opcao == 'sigla':
            if item.sigla == verificar:
                return True
        if opcao == 'numero':
            if item.numero == verificar:
                return True
        if opcao == 'nome':
            if item.nome == verificar:
                return True
        if opcao == 'indice':
            if cont == int(verificar):
                return True
    return False

def cadastrar_partido(partidos):
    sigla = input('Digite a sigla do partido: ')
    while isInLista(partidos, sigla, 'sigla'):
        sigla = input('Redigite outra sigla do partido: ')
    numero = input('Digite o número do partido: ')
    while isInLista(partidos, numero, 'numero'):
        numero = input('Redigite outra numero do partido: ')
    return Partido(sigla, numero)

def cadastrar_deputado(deputados, partidos):
    nome = input('Digite o nome do deputado: ')
    while isInLista(deputados, nome, 'nome'):
        nome = input('Redigite outro nome para o deputado: ')
    numero = input('Digite o número do deputado: ')
    while isInLista(deputados, numero, 'numero'):
        numero = input('Redigite outro número para o deputado: ')
    listarItens('Partidos:', partidos, True)
    opcao = input('Escolha o partido: ')
    while opcao.isnumeric() == False:
        opcao = input('Redigite o partido: ')
    while isInLista(partidos, opcao, 'indice') == False:
        opcao = input('Redigite o partido: ')
    partido = partidos[int(opcao)]
    return Deputado(nome, partido, numero)

def getDeputado(lista, verificar, opcao):
    for cont, item in enumerate(lista):
        if opcao == 'nome':
            if item.nome == verificar:
                return cont 
        if opcao == 'numero':
            if item.numero == verificar:
                return cont
    return False

 
    

def avaliar_deputado(deputados, partidos):  
    deputado = 0
    opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
    while opcao.isnumeric() == False:
        opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
    while opcao != '1' and opcao != '2' and opcao != '0':
        opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
        while opcao.isnumeric() == False:
            opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
    if opcao == '1':
        numero = input('Digite o numero do deputado: ')
        while isInLista(deputados, numero, 'numero') == False:
            numero = input('Redigite outro nome para o deputado: ')
        deputado = getDeputado(deputados, numero, 'numero')
        opcao = input('Escolha o a avaliação: [1-5] ')
        while opcao.isnumeric() == False:
            opcao = input('Escolha o a avaliação: [1-5] ')
        while int(opcao) < 0 or int(opcao) > 5:
            opcao = input('Redigite o partido: ')
        deputados[deputado].indicadorDeCorrupcao = opcao
    elif opcao == '2':
        nome = input('Digite o nome do deputado: ')
        while isInLista(deputados, nome, 'nome') == False:
            nome = input('Redigite outro nome para o deputado: ')
        deputado = getDeputado(deputados, nome, 'nome')
        listarItens('Partidos:', partidos, True)
        opcao = input('Escolha o a avaliação: [1-5] ')
        while opcao.isnumeric() == False:
            opcao = input('Escolha o a avaliação: [1-5] ')
        while int(opcao) < 0 or int(opcao) > 5:
            opcao = input('Redigite o partido: ')
        deputados[deputado].indicadorDeCorrupcao = opcao
    
def alterar_deputado(deputados, partidos):  
    deputado = 0
    opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
    while opcao.isnumeric() == False:
        opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
    while opcao != '1' and opcao != '2' and opcao != '0':
        opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
        while opcao.isnumeric() == False:
            opcao = input('Deputado, escolha: [1- Número ou 2 - Nome ou 0 - sair] ')
    if opcao == '1':
        numero = input('Digite o numero do deputado: ')
        while isInLista(deputados, numero, 'numero') == False:
            numero = input('Redigite outro nome para o deputado: ')
        deputado = getDeputado(deputados, numero, 'numero')
        listarItens('Partidos:', partidos, True)
        opcao = input('Escolha o partido: ')
        while opcao.isnumeric() == False:
            opcao = input('Redigite o partido: ')
        while isInLista(partidos, opcao, 'indice') == False:
            opcao = input('Redigite o partido: ')
        partido = partidos[int(opcao)]
        deputados[deputado].partido = partido
    elif opcao == '2':
        nome = input('Digite o nome do deputado: ')
        while isInLista(deputados, nome, 'nome') == False:
            nome = input('Redigite outro nome para o deputado: ')
        deputado = getDeputado(deputados, nome, 'nome')
        listarItens('Partidos:', partidos, True)
        opcao = input('Escolha o partido: ')
        while opcao.isnumeric() == False:
            opcao = input('Redigite o partido: ')
        while isInLista(partidos, opcao, 'indice') == False:
            opcao = input('Redigite o partido: ')
        partido = partidos[int(opcao)]
        deputados[deputado].partido = partido
    
    

def listarItens(titulo, lista, numeros=True, partido=False, avaliacao=False):
    print(f"{'#'*20}{'['+titulo+']'}{'#'*20}")
    for cont, item in enumerate(lista):
        if partido == False or avaliacao == False: 
            if numeros == True:        
                print(f"# \t {cont} - {item} \t #")
            else:
                print(f"# \t {item} \t #")
        elif avaliacao != False:
            if item.indicadorDeCorrupcao == 4 or item.indicadorDeCorrupcao == 5:
                if numeros == True:        
                    print(f"# \t {cont} - {item} \t #")
                else:
                    print(f"# \t {item} \t #")
        elif partido != False:
            if item.partido == partido:
                if numeros == True:        
                    print(f"# \t {cont} - {item} \t #")
                else:
                    print(f"# \t {item} \t #")

    print(f"{'#'*20}{'#'*len('['+titulo+']')}{'#'*20}")

def listarItensTipo(partidos, deputados):
    listarItens('Partidos:', partidos, True)
    opcao = input('Escolha o partido: ')
    while opcao.isnumeric() == False:
        opcao = input('Redigite o partido: ')
    while isInLista(partidos, opcao, 'indice') == False:
        opcao = input('Redigite o partido: ')
    partido = partidos[int(opcao)]
    listarItens('Deputados:', deputados, True, partido)
    
def listar_avaliacao(deputados, partidos): 
    listarItens('Deputados:',deputados,True,False,True)

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    escrever('Menu:', '''# \t 0 - Sair \t #
# \t 1 - Cadastrar Partido \t #
# \t 2 - Listar Partido \t # 
# \t 3 - Cadastrar Deputado \t # 
# \t 4 - Alterar Deputado \t # 
# \t 5 - Relatório de deputados \t # 
# \t 6 - Relatório de deputados por partido \t # 
# \t 7 - Avaliar deputados \t #''')

    escolha = input('Escolha:')
    return escolha