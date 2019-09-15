# -*- coding: utf-8 -*-
import os
reg_a = 0
reg_b = 0
reg_flag = ['0','0','0']
op = 0

def menu_inicial():
    os.system('cls')
    try:
        menu = int(input('Seja muito bem vindo à ULA.PY\n\n\
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
    except ValueError:
        os.system('clear')
        processa_menu_inicial(menu_inicial())

    return menu
    
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
    aux = '{:0>4}'.format(bin(reg_a)[2:])
    print('Registrador A ',aux[-4:])
    os.system('pause')

def le_reg_b():
    global reg_b
    aux = '{:0>4}'.format(bin(reg_b)[2:])
    print('Registrador B ',aux[-4:])
    os.system('pause')

def le_reg_flag():
    if(reg_a == 0):
        reg_flag[2] = '1'
    else: reg_flag[2] = '0'
    print('\n\n\
 _____ Indicação de Carry\n\
|\n\
|  ____ Indicação de Resultado negativo de subtração\n\
| |\n\
| |  ___ Indicação de Zero no acumulador\n\
| | |\n\
| | |\
')
    print(reg_flag[0], reg_flag[1], reg_flag[2])
    os.system('pause')

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
    global op, reg_a, reg_b, reg_flag
    reg_flag = ['0','0','0']
    
    


    
    if op == '00':
        reg_a += reg_b
        if(reg_a > 15):
            reg_flag[0] = '1'
        reg_a = int((bin(reg_a)[-4:]),2)
        
        return
    
    elif op == '01':
        if(reg_b > reg_a):
            reg_flag[1] = '1'     # Indica resultado negativo
        reg_a = max(reg_a,reg_b) - min(reg_a,reg_b)
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





<<<<<<< HEAD
=======
print('\
 ___________________ Indicação de Overflow\
|\
| __________________ Indicação de Resultado negativo de subtração\
||\
|| _________________ Indicação de Zero no acumulador\
|||\
|||\
|||\
')








>>>>>>> f9441743f2d1960436644f260ccc455e34e7a0b0




