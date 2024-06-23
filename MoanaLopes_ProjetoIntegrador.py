# ----- Importando a biblioteca RANDOM ----- #
import random

# ----- Declarando as variáveis de controle do jogo ----- #
chances = 5
numMin = 0
numMax = 100

# ----- Instruções do jogo para o jogador ----- #
print('Bem-vindo(a) ao Jogo da Adivinhação!')
print('Você terá %d chances para acertas o número entre %d e %d que irei gerar aleatoriamente.' %(chances, numMin, numMax))
print('Se você errar, darei dicas para a sua próxima tentativa.')
print('Boa sorte! =)\n')

# ----- Cria classe a ser utilizada como 'exceção' para a estrutura 'TRY... EXCEPT' ----- #
class numOutsideRange(Exception):
    pass

# ----- Função do jogo ----- #
def guessNumber():
    rndNum = random.randint(numMin, numMax) # Gera número aleatório entre os valores mínimo e máximo definidos
    # print(rndNum)
    guessesLeft = chances # O jogador iniciará o jogo com X tentativas

    # ----- Loop que irá receber palpite do jogador e verificar se foi correto ou errado ----- #
    while guessesLeft > 0:
        numGuessed = input('Dê o seu palpite: ')
        
        try:
            numGuessed = int(numGuessed) # Armazena o palpite do jogador e o converte de STRING para INTEIRO

            # ----- Condição que lançará "exceção" caso entrada esteja fora do limite definido ----- #
            if numGuessed < numMin or numGuessed > numMax:
                raise numOutsideRange # Chama o EXCEPT "numOutsideRange"
            
            # ----- Condicional que verifica se o palpite foi certo ou não ----- #
            if numGuessed == rndNum: # Acertou!
                print('\nParabéns! Você acertou! O número secreto era: %d =)\n' %rndNum)
                break
            else: # Errou!
                # ----- Se essa foi a última chance, o jogador perdeu o jogo ----- #
                if guessesLeft == 1:
                    print('\nVocê perdeu! O número secreto era: %d. =(\n' %rndNum)
                    break
                # ----- Se ainda tem alguma tentativa, o jogo dará dicas para o jogador ----- #
                if numGuessed < rndNum:
                    print('\nVocê errou! O número secreto é maior que %d.\n' %numGuessed)
                else:
                    print('\nVocê errou! O número secreto é menor que %d.\n' %numGuessed)

                # ----- Diminui uma tentativa do jogador a cada erro ----- #
                guessesLeft -= 1
                print('Você tem mais %d tentativa(s).\n' %guessesLeft)

        # ----- Caso entrada não seja número, um erro será lançado e pedirá que um valor válido ----- #
        except ValueError:
            print('\nPor favor, insira um número válido.\n')
        # ----- A mesma coisa acontecerá para entrada fora do intervalo definido ----- #
        except numOutsideRange:
            print("\nO número é está entre %d e %d.\nPor favor, insira um número dentro do intervalo.\n" %(numMin, numMax))

    # ----- Loop WHILE para que repita o INPUT até receber uma entrada válida do jogador ----- #
    while True:
        # ----- Verifica se o jogador que iniciar uma nova partida ----- #
        try:
            newGame = int(input('Gostaria de jogar novamente?\nSim: 1\nNão: 2\n')) # Armazena a opção escolhida e a converte de STRING para INTEIRO
            # ----- Condição que lançará "exceção" caso entrada esteja seja diferente de 1 ou 2 ----- #
            if newGame != 1 and newGame != 2:
                raise numOutsideRange # Chama o EXCEPT "numOutsideRange"
            # ----- Chama novamente a função "guessNumber" para reiniciar o jogo ou a finaliza ----- #
            guessNumber() if newGame == 1 else print('\nAté a próxima!')
            break
        # ----- Caso entrada não seja número, um erro será lançado e pedirá um valor válido ----- #
        except ValueError:
            print('\nPor favor, entre com uma opção válida.\n') 
        # ----- Mesma coisa acontecerá caso opção escolhida seja diferente de 1 ou 2 ----- #
        except numOutsideRange:
            print('\nPor favor, escolha uma opção válida.\n')

# ----- Chama a função do jogo ----- #
guessNumber()
