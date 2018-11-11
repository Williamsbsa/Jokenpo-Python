from random import randint
from time import sleep

scorePlayer1 = 0
scorePlayer2 = 0
escolhaPlayer1 = 0
escolhaPlayer2 = 0

mostrarEstatisticas = 'novo'
nEmpates = 0
nRounds = 0
nTesouraP1 = 0
nPapelP1 = 0
nPedraP1 = 0
nTesouraP2 = 0
nPapelP2 = 0
nPedraP2 = 0
nErrosP1 = 0
nErrosP2 = 0

modoJogo = 0
modo = 0

while mostrarEstatisticas == 'novo':
    scorePlayer1 = 0
    scorePlayer2 = 0
    escolhaPlayer1 = 0
    escolhaPlayer2 = 0

    nEmpates = 0
    nRounds = 0
    nTesouraP1 = 0
    nPapelP1 = 0
    nPedraP1 = 0
    nTesouraP2 = 0
    nPapelP2 = 0
    nPedraP2 = 0
    nErrosP1 = 0
    nErrosP2 = 0

    modoJogo = 0
    modo = 0

    print('ESCOLHA O MOODO DE JOGO')
    print('DIGITE - 1 - PARA PLAYER X PLAYER; DIGITE - 2 - PARA PLAYER X PC; DIGITE - 3 - PARA PC X PC.')
    modoJogo = int(input())
    if modoJogo != 1 and modoJogo !=2 and modoJogo !=3:
        while modoJogo != 1 and modoJogo !=2 and modoJogo !=3:
            print('COMANDO INVALIDO')
            print('DIGITE - 1 - PARA JOGADOR X JOGADOR; DIGITE - 2 - PARA JOGADOR X PC; DIGITE - 3 - PARA PC X PC.')
            modoJogo = int(input())

    if modoJogo == 1:
        print()
        print()
        print('JOGADOR X JOGADOR')
        print("DIGITE - 5 - PARA MODO CAMPEONATO MELHOR DE 5, - 13 - PARA MELHOR DE 13 E - 21 - PARA MELHOR DE 21")
        modo = int(input())

        if modo != 5 and modo != 13 and modo != 21:
            while modo != 5 and modo != 13 and modo != 21:
                print('COMANDO INVALIDO.')
                print("DIGITE - 5 - PARA MODO CAMPEONATO MELHOR DE 5, - 13 - PARA MELHOR DE 13 E - 21 - PARA MELHOR DE 21")
                modo = int(input())

        if modo == 5:
            while scorePlayer1 < 3 and scorePlayer2 < 3:    #Melhor de cinco.
                print('- 1 -  PEDRA')
                print('- 2 -  PAPEL')
                print('- 3 -  TESOURA')
                escolhaPlayer1 = int(input('Jogador um, sua jogada - '))
                print('\n' * 100)
                escolhaPlayer2 = int(input('Jogador dois, sua jogada - '))
                print('\n' * 100)
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!')
                print('=-' * 11)

                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player1 = PEDRA < PAPEL = Player 2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player1 = PEDRA < TESOURA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player1 = PAPEL < PEDRA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Player1 = PAPEL < TESOURA = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player1 = TESOURA < PEDRA = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Player1 = TESOURA < PAPEL = Player 2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Player1 = PEDRA - PEDRA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Player1 = PAPEL - PAPEL = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Player1 = TESOURA - PAPEL = Player 2')
                else:
                    if (escolhaPlayer1 == 1) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nPedraP1 = nPedraP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer1 == 2) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nPapelP1 = nPapelP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer1 == 3) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nTesouraP1 = nTesouraP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer2 == 1) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPedraP2 = nPedraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    elif (escolhaPlayer2 == 2) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPapelP2 = nPapelP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    elif (escolhaPlayer2 == 3) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nTesouraP2 = nTesouraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    else:
                        nErrosP1 = nErrosP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador um e dois, escolha invalida')
                nRounds = nRounds + 1
                print('Player1 - ', scorePlayer1, 'X', scorePlayer2, ' - Player2')
                print()
                print()

        if modo == 13:
            while scorePlayer1 < 7 and scorePlayer2 < 7:  # Melhor de 13.
                print('- 1 -  PEDRA')
                print('- 2 -  PAPEL')
                print('- 3 -  TESOURA')
                escolhaPlayer1 = int(input('Jogador um, sua jogada - '))
                escolhaPlayer2 = int(input('Jogador dois, sua jogada - '))
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!')
                print('=-' * 11)

                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player1 = PEDRA < PAPEL = Player 2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player1 = PEDRA < TESOURA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player1 = PAPEL < PEDRA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Player1 = PAPEL < TESOURA = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player1 = TESOURA < PEDRA = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Player1 = TESOURA < PAPEL = Player 2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Player1 = PEDRA - PEDRA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Player1 = PAPEL - PAPEL = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Player1 = TESOURA - PAPEL = Player 2')
                else:
                    if (escolhaPlayer1 == 1) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nPedraP1 = nPedraP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer1 == 2) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nPapelP1 = nPapelP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer1 == 3) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nTesouraP1 = nTesouraP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer2 == 1) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPedraP2 = nPedraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    elif (escolhaPlayer2 == 2) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPapelP2 = nPapelP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    elif (escolhaPlayer2 == 3) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nTesouraP2 = nTesouraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    else:
                        nErrosP1 = nErrosP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador um e dois, escolha invalida')
                nRounds = nRounds + 1
                print('Player1 - ', scorePlayer1, 'X', scorePlayer2, ' - Player2')
                print()
                print()

        if modo == 21:
            while scorePlayer1 < 11 and scorePlayer2 < 11:    #melhor de 21
                print('- 1 -  PEDRA')
                print('- 2 -  PAPEL')
                print('- 3 -  TESOURA')
                escolhaPlayer1 = int(input('Jogador um, sua jogada - '))
                escolhaPlayer2 = int(input('Jogador dois, sua jogada - '))
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!')
                print('=-' * 11)

                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player1 = PEDRA < PAPEL = Player 2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player1 = PEDRA < TESOURA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player1 = PAPEL < PEDRA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Player1 = PAPEL < TESOURA = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player1 = TESOURA < PEDRA = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Player1 = TESOURA < PAPEL = Player 2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Player1 = PEDRA - PEDRA = Player 2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Player1 = PAPEL - PAPEL = Player 2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Player1 = TESOURA - PAPEL = Player 2')
                else:
                    if (escolhaPlayer1 == 1) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nPedraP1 = nPedraP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer1 == 2) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nPapelP1 = nPapelP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer1 == 3) and (escolhaPlayer2 != 1 and escolhaPlayer2 != 2 and escolhaPlayer2 != 3):
                        scorePlayer1 = scorePlayer1 + 1
                        nTesouraP1 = nTesouraP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador dois, escolha invalida')
                    elif (escolhaPlayer2 == 1) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPedraP2 = nPedraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    elif (escolhaPlayer2 == 2) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPapelP2 = nPapelP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    elif (escolhaPlayer2 == 3) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nTesouraP2 = nTesouraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador um, escolha invalida')
                    else:
                        nErrosP1 = nErrosP1 + 1
                        nErrosP2 = nErrosP2 + 1
                        print('Jogador um e dois, escolha invalida')
                nRounds = nRounds + 1
                print('Player1 - ', scorePlayer1, 'X', scorePlayer2, ' - Player2')
                print()
                print()


    if modoJogo == 2:
        print()
        print()
        print('JOGADOR X PC')
        print("DIGITE - 5 - PARA CAMPEONATO MELHOR DE 5, - 13 - PARA MELHOR DE 13 E - 21 - PARA MELHOR DE 21")
        modo = int(input())

        if modo != 5 and modo != 13 and modo != 21:
            while modo != 5 and modo != 13 and modo != 21:
                print('COMANDO INVALIDO.')
                print("DIGITE - 5 - PARA MODO CAMPEONATO MELHOR DE 5, - 13 - PARA MELHOR DE 13 E - 21 - PARA MELHOR DE 21")
                modo = int(input())

        if modo == 5:
            while scorePlayer1 < 3 and scorePlayer2 < 3:
                print('- 1 -  PEDRA')
                print('- 2 -  PAPEL')
                print('- 3 -  TESOURA')
                escolhaPlayer2 = randint(1, 3)
                escolhaPlayer1 = int(input('Jogador um, sua jogada - '))
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!')
                print('=-' * 11)

                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player = PEDRA < PAPEL = Computador')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player = PEDRA < TESOURA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player = PAPEL < PEDRA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Player = PAPEL < TESOURA = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player = TESOURA < PEDRA = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Player = TESOURA < PAPEL = Computador')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Player = PEDRA - PEDRA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Player = PAPEL - PAPEL = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Player = TESOURA - PAPEL = Computador')
                else:
                    if (escolhaPlayer2 == 1) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPedraP2 = nPedraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                    elif (escolhaPlayer2 == 2) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPapelP2 = nPapelP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                    elif (escolhaPlayer2 == 3) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nTesouraP2 = nTesouraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                nRounds = nRounds + 1
                print('Player - ', scorePlayer1, 'X', scorePlayer2, ' - Computador')
                print()
                print()

        if modo == 13:
            while scorePlayer1 < 7 and scorePlayer2 < 7:
                print('- 1 -  PEDRA')
                print('- 2 -  PAPEL')
                print('- 3 -  TESOURA')
                escolhaPlayer2 = randint(1, 3)
                escolhaPlayer1 = int(input('Jogador um, sua jogada - '))
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!')
                print('=-' * 11)

                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player = PEDRA < PAPEL = Computador')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player = PEDRA < TESOURA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player = PAPEL < PEDRA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Player = PAPEL < TESOURA = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player = TESOURA < PEDRA = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Player = TESOURA < PAPEL = Computador')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Player = PEDRA - PEDRA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Player = PAPEL - PAPEL = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Player = TESOURA - PAPEL = Computador')
                else:
                    if (escolhaPlayer2 == 1) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPedraP2 = nPedraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                    elif (escolhaPlayer2 == 2) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPapelP2 = nPapelP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                    elif (escolhaPlayer2 == 3) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nTesouraP2 = nTesouraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                nRounds = nRounds + 1
                print('Player - ', scorePlayer1, 'X', scorePlayer2, ' - Computador')
                print()
                print()

        if modo == 21:
            while scorePlayer1 < 11 and scorePlayer2 < 11:
                print('- 1 -  PEDRA')
                print('- 2 -  PAPEL')
                print('- 3 -  TESOURA')
                escolhaPlayer2 = randint(1, 3)
                escolhaPlayer1 = int(input('Jogador um, sua jogada - '))
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO!!')
                print('=-' * 11)

                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player = PEDRA < PAPEL = Computador')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player = PEDRA < TESOURA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Player = PAPEL < PEDRA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Player = PAPEL < TESOURA = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Player = TESOURA < PEDRA = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Player = TESOURA < PAPEL = Computador')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Player = PEDRA - PEDRA = Computador')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Player = PAPEL - PAPEL = Computador')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Player = TESOURA - PAPEL = Computador')
                else:
                    if (escolhaPlayer2 == 1) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPedraP2 = nPedraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                    elif (escolhaPlayer2 == 2) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nPapelP2 = nPapelP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                    elif (escolhaPlayer2 == 3) and (escolhaPlayer1 != 1 and escolhaPlayer1 != 2 and escolhaPlayer1 != 3):
                        scorePlayer2 = scorePlayer2 + 1
                        nTesouraP2 = nTesouraP2 + 1
                        nErrosP1 = nErrosP1 + 1
                        print('Jogador, escolha invalida')
                nRounds = nRounds + 1
                print('Player - ', scorePlayer1, 'X', scorePlayer2, ' - Computador')
                print()
                print()

    if modoJogo == 3:
        print()
        print()
        print('PC X PC')
        print("DIGITE - 1 - PARA UM ROUND OU - 50 - PARA 50 ROUNDS")
        modo = int(input())

        if modo != 1 and modo != 50:
            while modo != 1 and modo != 50:
                print('COMANDO INVALIDO.')
                print("DIGITE - 1 - PARA UM ROUND OU - 50 - PARA 50 ROUNDS")
                modo = int(input())

        if modo == 1:
            escolhaPlayer1 = randint(1, 3)
            escolhaPlayer2 = randint(1, 3)
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!')
            print('=-' * 11)
            if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                scorePlayer2 = scorePlayer2 + 1
                nPedraP1 = nPedraP1 + 1
                nPapelP2 = nPapelP2 + 1
                print('Papel embrulha a Pedra!')
                print('Computador1 = PEDRA < PAPEL = Computador2')
            elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                scorePlayer1 = scorePlayer1 + 1
                nPedraP1 = nPedraP1 + 1
                nTesouraP2 = nTesouraP2 + 1
                print('Pedra esmaga a Tesoura!')
                print('Computador1 = PEDRA < TESOURA = Computador2')
            elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                scorePlayer1 = scorePlayer1 + 1
                nPapelP1 = nPapelP1 + 1
                nPedraP2 = nPedraP2 + 1
                print('Papel embrulha a Pedra!')
                print('Computador1 = PAPEL < PEDRA = Computador2')
            elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                scorePlayer2 = scorePlayer2 + 1
                nPapelP1 = nPapelP1 + 1
                nTesouraP2 = nTesouraP2 + 1
                print('Tesoura corta o papel!')
                print('Computador1 = PAPEL < TESOURA = Computador2')
            elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                scorePlayer2 = scorePlayer2 + 1
                nTesouraP1 = nTesouraP1 + 1
                nPedraP2 = nPedraP2 + 1
                print('Pedra esmaga a Tesoura!')
                print('Computador1 = TESOURA < PEDRA = Computador2')
            elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                scorePlayer1 = scorePlayer1 + 1
                nTesouraP1 = nTesouraP1 + 1
                nPapelP2 = nPapelP2 + 1
                print('Tesoura corta o Papel!')
                print('Computador1 = TESOURA < PAPEL = Computador2')
            elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                nEmpates = nEmpates + 1
                nPedraP1 = nPedraP1 + 1
                nPedraP2 = nPedraP2 + 1
                print("EMPATE")
                print('Computador1 = PEDRA - PEDRA = Computador2')
            elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                nEmpates = nEmpates + 1
                nPapelP1 = nPapelP1 + 1
                nPapelP2 = nPapelP2 + 1
                print('EMPATE')
                print('Computador1 = PAPEL - PAPEL = Computador2')
            elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                nEmpates = nEmpates + 1
                nTesouraP1 = nTesouraP1 + 1
                nTesouraP2 = nTesouraP2 + 1
                print('EMPATE')
                print('Computador1 = TESOURA - PAPEL = Computador2')
            nRounds = nRounds + 1
            print(' Computador1 - ', scorePlayer1, 'X', scorePlayer2, ' - Computador2')
            print()
            print()

        if modo == 50:
            while nRounds < 50:
                escolhaPlayer1 = randint(1, 3)
                escolhaPlayer2 = randint(1, 3)
                print('JO')
                print('KEN')
                print('PO!!')
                print('=-' * 11)
                if escolhaPlayer1 == 1 and escolhaPlayer2 == 2:
                    scorePlayer2 = scorePlayer2 + 1
                    nPedraP1 = nPedraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Computador1 = PEDRA < PAPEL = Computador2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 3:
                    scorePlayer1 = scorePlayer1 + 1
                    nPedraP1 = nPedraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Computador1 = PEDRA < TESOURA = Computador2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 1:
                    scorePlayer1 = scorePlayer1 + 1
                    nPapelP1 = nPapelP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Papel embrulha a Pedra!')
                    print('Computador1 = PAPEL < PEDRA = Computador2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 3:
                    scorePlayer2 = scorePlayer2 + 1
                    nPapelP1 = nPapelP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('Tesoura corta o papel!')
                    print('Computador1 = PAPEL < TESOURA = Computador2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 1:
                    scorePlayer2 = scorePlayer2 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print('Pedra esmaga a Tesoura!')
                    print('Computador1 = TESOURA < PEDRA = Computador2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 2:
                    scorePlayer1 = scorePlayer1 + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('Tesoura corta o Papel!')
                    print('Computador1 = TESOURA < PAPEL = Computador2')
                elif escolhaPlayer1 == 1 and escolhaPlayer2 == 1:
                    nEmpates = nEmpates + 1
                    nPedraP1 = nPedraP1 + 1
                    nPedraP2 = nPedraP2 + 1
                    print("EMPATE")
                    print('Computador1 = PEDRA - PEDRA = Computador2')
                elif escolhaPlayer1 == 2 and escolhaPlayer2 == 2:
                    nEmpates = nEmpates + 1
                    nPapelP1 = nPapelP1 + 1
                    nPapelP2 = nPapelP2 + 1
                    print('EMPATE')
                    print('Computador1 = PAPEL - PAPEL = Computador2')
                elif escolhaPlayer1 == 3 and escolhaPlayer2 == 3:
                    nEmpates = nEmpates + 1
                    nTesouraP1 = nTesouraP1 + 1
                    nTesouraP2 = nTesouraP2 + 1
                    print('EMPATE')
                    print('Computador1 = TESOURA - PAPEL = Computador2')
                nRounds = nRounds + 1
                print('Computador1 - ', scorePlayer1, 'X', scorePlayer2, ' - Computador2')
                print()
                print()

    if scorePlayer1 > scorePlayer2 and modoJogo == 1:
        print('VITORIA DO PLAYER1')
        print()
        print()
    elif scorePlayer1 > scorePlayer2 and modoJogo == 2:
        print('VITORIA DO PLAYER')
        print()
        print()
    elif scorePlayer2 > scorePlayer1 and modoJogo == 1:
        print('VITORIA DO PLAYER2')
        print()
        print()
    elif scorePlayer1 > scorePlayer2 and modoJogo == 3:
        print('VITORIA DO COMPUTADOR1')
        print()
        print()
    elif scorePlayer2 > scorePlayer1 and modoJogo == 2:
        print('VITORIA DO COMPUTADOR')
        print()
        print()
    elif scorePlayer2 > scorePlayer1 and modoJogo == 3:
        print('VITORIA DO COMPUTADOR2')
        print()
        print()
    else:
        print('EMPATE')
    print("DIGITE - estatisticas - PARA VER AS ESTATISTICAS DO JOGO")
    print("DIGITE - novo - PARA JOGAR NOVAMENTE")
    mostrarEstatisticas = str(input())
    if mostrarEstatisticas == 'estatisticas':
        if modo == 5:
            print('MELHOR DE 5')
        elif modo == 13:
            print('MELHOR DE 13')
        else:
            print('MELHOR DE 21')

        print('NUMERO DE ROUNDS - ', nRounds)
        print('EMPATES - ', nEmpates)
        if modoJogo == 1:
            print('JOGADOR UM : ')
        elif modoJogo == 2:
            print('JOGADOR : ')
        elif modoJogo == 3:
            print('COMPUTADOR UM : ')
        print('NUMERO DE PEDRAS JOGADAS - ', nPedraP1)
        print('NUMERO DE PAPEIS JOGADOS - ', nPapelP1)
        print('NUMERO DE TESOURAS JOGADAS - ', nTesouraP1)
        print('NUMERO DE ERROS - ', nErrosP1)
        if modoJogo == 1:
            print('JOGADOR DOIS : ' )
        if modoJogo == 2:
            print('COMPUTADOR : ')
        if modoJogo == 3:
            print('COMPUTADOR DOIS : ')
        print('NUMERO DE PEDRAS JOGADAS - ', nPedraP2)
        print('NUMERO DE PAPEIS JOGADOS - ', nPapelP2)
        print('NUMERO DE TESOURAS JOGADAS - ', nTesouraP2)
        print('NUMERO DE ERROS - ', nErrosP2)
        print('DIGITE - novo - PARA JOGAR NOVAMENTE')
        mostrarEstatisticas = str(input())