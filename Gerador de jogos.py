#Bibliotecas
import random
import time
#Inicialização de variaveis
sorteio = []
qtJogos = 0
num = 0
jogos = []
j=0

print('***** Gerador De Jogos *****')
#Quantidade de jogos
qtJogos = int(input('Quantos jogos você deseja?'))

#Laço de repetiçao para o número de jogos
for c in range(1,qtJogos +1):
    print(f'{c}º jogo')
    #Laço de repetição para gerar os 6 números do jogo
    for n in range(0,6):
        #Essa variavel guarda um número aleatório de 1 a 60
            num = random.randint(1,60)
        #Se o número que está na variavel ja tiver sido sorteado ele irá ignorar esse número
        # e sortear outro
            while num in sorteio:
                num = 0
                num = random.randint(1,60)
        #Se não for um numero repetido ele armazena na lista com o restante
            sorteio.append(num)

    print(sorteio)
    sorteio.clear()
    time.sleep(2)


