from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('='*20 + ' Escolha uma opção: ' + '='*20 +
      '\n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')

escolha = int(input('Qual é asua jogada? '))

print('\nO resultado foi...\n')

time.sleep(2)

if escolha > 2:
    print('Reinicie jogo e tente novamente (Error: Número inválido)')

elif pc == 0:  # PC jogando Pedra
    if escolha == 0:  # Pedra
        print(
            f'Empatou!!! \nSeu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
    if escolha == 1:  # Papel
        print(
            f'Parabéns!!! \nVocê ganhou! Seu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
    if escolha == 2:  # Tesoura
        print(
            f'Que pena!!! \nVocê perdeu! Seu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
elif pc == 1:  # PC jogando Papel
    if escolha == 0:  # Pedra
        print(
            f'Que pena!!! \nVocê perdeu! Seu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
    if escolha == 1:  # Papel
        print(
            f'Empatou!!! \nSeu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
    if escolha == 2:  # Tesoura
        print(
            f'Parabéns!!! \nVocê ganhou! Seu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
elif pc == 2:  # PC jogando Tesoura
    if escolha == 0:  # Pedra
        print(
            f'Parabéns!!! \nVocê ganhou! Seu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
    if escolha == 1:  # Papel
        print(
            f'Que pena!!! \nVocê perdeu! Seu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
    if escolha == 2:  # Tesoura
        print(
            f'Empatou!!! \nSeu computador jogou {itens[pc]} e você jogou {itens[escolha]}')
