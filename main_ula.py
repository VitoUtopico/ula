# -*- coding: utf-8 -*-
import os
reg_a = 0
reg_b = 0
op = 0

def menu_inicial():
    os.system('cls')
    return int(input('Seja muito bem vindo à ULA.PY\n\n\
          Menu Principal da ULA\n\n\
              1. Definir registrador A\n\
              2. Definir registrador B\n\
              3. Ler registrador A (Acc)\n\
              4. Ler registrador B\n\
              5. Ler registrador de flags\n\
              6. Definir operação\n\
              7. Executar ULA\n\
              8. Sair\n\n\
          Escolha a opção => '))
    
def def_reg_a():
    global reg_a
    try:
        reg_a = int(input('Insira o valor do registrador A: '),2)
    except ValueError:
        print('\n\nA ULA aceita apenas valores binários')
        def_reg_a()

def def_reg_b():
    global reg_b
    try:
        reg_b = int(input('Insira o valor do registrador B: '),2)
    except ValueError:
         print('\n\nA ULA aceita apenas valores binários')
         def_reg_b()
def le_reg_a():
    global reg_a
    print('Registrador A ',bin(reg_a)[2:])
    os.system('pause')

def le_reg_b():
    global reg_b
    print('Registrador B ',bin(reg_b)[2:])
    os.system('pause')

def le_reg_flag():
    pass

def def_op():
    global op
    os.system('cls')
    op = input('\
               00 -> Soma\n\
               01 -> Subtração\n\
               10 -> AND\n\
               11 -> OR\n\
               \nEscolha o operador => ')
   
def exec_ula():
    global op, reg_a, reg_b
    if op == '00':
        reg_a += reg_b
        return
    elif op == '01':
        reg_a -= reg_b
        return
    elif op == '10':
        reg_a = reg_a & reg_b
        return
    elif op == '11':
        reg_a = reg_a | reg_b
        return



def processa_menu_inicial(entrada):
    if entrada == 1:  
        def_reg_a()
    elif entrada == 2:
        def_reg_b()
    elif entrada == 3:
        le_reg_a()
    elif entrada == 4:
        le_reg_b()
    elif entrada == 5:
        le_reg_flag()
    elif entrada == 6:
        def_op()
    elif entrada == 7:
        exec_ula()
    elif entrada == 8:
        return 
    processa_menu_inicial(menu_inicial())
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
processa_menu_inicial(menu_inicial())
