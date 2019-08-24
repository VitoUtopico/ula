

def menu_inicial():
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
    print( 'registrador a')

def def_reg_b():
    pass

def le_reg_a():
    pass

def le_reg_b():
    pass

def le_reg_flag():
    pass

def def_op():
    pass

def exec_ula():
    pass



def processa_menu_inicial(entrada):
    if entrada == 1:  return def_reg_a()
    if entrada == 2:  return def_reg_b()
    if entrada == 3:  return le_reg_a()
    if entrada == 4:  return le_reg_b()
    if entrada == 5:  return le_reg_flag()
    if entrada == 6:  return def_op()
    if entrada == 7:  return exec_ula()
    if entrada == 8:  return 
        
    
processa_menu_inicial(menu_inicial())
