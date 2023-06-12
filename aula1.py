#-------------------------------------------------------
# Bem vindos a primeira aula de Python - SNK Programming
#-------------------------------------------------------

from os import system

# Como printar no cmd textos, atualizações ou instruções. (Mencionar o \n)
print('Hello World')

# Como printar formatado, pulando linhas e escrevendo da forma que está no código.
print('''
Olá, tudo bem com você?
    Comigo está tudo bem\n''')

# Print de variáveis.
#print('O valor de x é: 50')

# Declarando a variável e printando no cmd.
x = 50
print('O valor de x é:',x)
print(f'O valor de x é: {x}')

# Pedindo input de uma variável e printar a mesma na tela.
y = input('\nDigite um valor para a variável y: ')
print(f'O valor de y é: {y}')
input('Aperte ENTER para continuar')

system('cd Pasta1')