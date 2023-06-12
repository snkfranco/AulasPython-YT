#-------------------------------------------------------
# Estruturas condicionais e Estruturas de repetição
#-------------------------------------------------------

# Estruturas condicionais

idade = 18

if idade >= 18:
    print("Você tem permissão para acessar o conteúdo.")
else:
    print("Desculpe, você não tem permissão para acessar o conteúdo.")

numero = 7

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#-------------------------------------------------------

# Estruturas de repetição

contador = 0

while contador <= 5:
    print(contador)
    contador += 1


frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)