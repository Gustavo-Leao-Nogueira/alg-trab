#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from funcoes import *
from time import sleep


lista_de_deputados = []
lista_de_partidos = []

while True:
    opcao = menu()

    if opcao == '1':
        lista_de_partidos.append(cadastrar_partido(lista_de_partidos))
    elif opcao == '2':
        listarItens('Partidos:', lista_de_partidos, True)
        espera= input()
    elif opcao == '3':
        lista_de_deputados.append(cadastrar_deputado(lista_de_deputados, lista_de_partidos))
    elif opcao == '4':
        alterar_deputado(lista_de_deputados, lista_de_partidos)
    elif opcao == '5':
        listarItens('Deputados:', lista_de_deputados, True)
        espera= input()
    elif opcao == '6':
        listarItensTipo(lista_de_partidos, lista_de_deputados)
        espera= input()
    elif opcao == '7':
        avaliar_deputado(lista_de_deputados, lista_de_partidos)
    elif opcao == '8':
        listar_avaliacao(lista_de_deputados, lista_de_partidos)
    elif opcao == '0':
        print('Saindo!') 
        sleep(1)       
        break
    else:
        print('Saindo!')  
        sleep(1)      
        break