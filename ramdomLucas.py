import random

print(random.random()) # Valor 0 até 5
print(random.randint(0,5)) # Valor inteiros do mínimo ao máximo

numeros = input('Digite um número')
if numeros:
    print ('Número errado!!!')
else :
    print ('Número correto!!')