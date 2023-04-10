pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Importações
import random

#Definindo jogada do computador
opcoes=[pedra, papel, tesoura]
computador=random.choice(opcoes)

#Definindo jogada do usuário
print('Informe sua Jogada!')
usuario=input('Escreva Pedra, Papel ou Tesoura: ')
usuario=usuario.lower()

if usuario=='papel':
  usuario=papel
elif usuario=='tesoura':
  usuario=tesoura
else:
  usuario=pedra

#Exibindo as jogadas  
print('')
print('')
print('Sua jogada!')
print(usuario)
print('')
print('Jogada do computador!')
print(computador)
print('')
print('')

#Descobrindo o resultado
if usuario==pedra and computador==tesoura or usuario==papel and computador==pedra or usuario==tesoura and computador==papel:
  print('Parabéns, você venceu!')
elif usuario==pedra and computador==papel or usuario==papel and computador==tesoura or usuario==tesoura and computador==pedra:
  print('Poxa, não foi dessa vez :( ')
else:
  print('Empate! Jogue novamente.')
