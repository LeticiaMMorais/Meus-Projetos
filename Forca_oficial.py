
import random
import os

# Extensibilidade (desafio 10) -- obs: as funções foram definidas em especial para os códigos que se repetem ou para facilitar o uso.

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

#  Gráficos (desafio 7): vai imprimir uma lista a cada erro
def desenho_forca(erros):
    desenho_da_forca = [['_________________','|                |','|','|','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|','|','|','|','_____'], 
                        ['_________________','|                |','|              (°-°)','|                |','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|               /|','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|               /|\ ','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|               /|\ ','|               /','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|               /|\ ','|               / \ ','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|               /|\ ','|              _/ \_','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|              _/|\_ ','|              _/ \_','|','|','_____'],
                        ['_________________','|                |','|            *´(°-°)`*','|              _/|\_ ','|              _/ \_','|','|','_____'],
                        ['_________________','|                |','|           *´(x o x)`*','|              _/|\_ ','|              _/ \_','|','|','_____']]
    for linha in desenho_da_forca[erros]:
        print(linha)

def desenho_forca_dificil(erros):
    desenho_da_forca = [['_________________','|                |','|','|','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|                |','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|              _/|\_ ','|','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|              _/|\_ ','|               / \ ','|','|','_____'],
                        ['_________________','|                |','|              (°-°)','|              _/|\_ ','|              _/ \_','|','|','_____']]
    for linha in desenho_da_forca[erros]:
        print(linha)

def fim_de_jogo():
    print('-----------------------------------------------------------------------------------------')
    print(' _______   __   __      __     ____    _______          __   _______   _______   _______ ')
    print('|   ____| |__| |  \    /  |   |    \  |   ____|        |  | |   _   | |  _____| |   _   |')
    print('|  |____   __  |   \  /   |   |  |\ \ |  |____         |  | |  | |  | |  |  __  |  | |  |')
    print('|   ____| |  | |  \ \/ /  |   |  | | ||   ____|     __ |  | |  | |  | |  | |_ | |  | |  |')
    print('|  |      |  | |  |\__/|  |   |  |_/ /|  |____     (  \|  | |  |_|  | |  |__| | |  |_|  |')
    print('|__|      |__| |__|    |__|   |_____/ |_______|     \_____| |_______| |_______| |_______|')
    print('-----------------------------------------------------------------------------------------')

# Dificuldade (desafio 3): onde vai retornar o número de tentativas a partir da escolha da dificuldade
def dificuldade():
    tentativas = 0
    global dific
    print('----------------------------------------------------------')
    while True:
        dific = input('Escolha uma dificuldade:\n-Fácil\n-Médio\n-Difícil\n-')
        
        if dific.upper() == 'FÁCIL':
            tentativas = 10
            break
        elif dific.upper() == 'MÉDIO':
            tentativas = 7
            break
        elif dific.upper() == 'DIFÍCIL':
            tentativas = 4
            break
        else:
            print('Erro! Tente novamente\n')
    limpar()
    return tentativas

#Registro de jogadores (desafio 5): vai adicionar na lista dicionários com nome e idade dos jogadores
def registro_de_jogadores(jogadores,num):
    for numero in range(num):
        jogador = {}
        jogador['nome']= input(f'Jogador {numero+1}, escreva seu nome/apelido: ')
        jogador['idade'] = input(f'Jogador {numero+1}, digite sua idade: ')
        jogadores.append(jogador)
    print(jogadores)


def escolha_de_palavra(palavras):
    print('----------------------------------------------------------')
    print('Categorias:')
    for palavra in palavras.keys():
        print('-', palavra)
    while True:
        escolha = input('Escolha uma categoria da palavra que deseja jogar: ')
        if escolha.upper() == 'COMIDAS':
            palavra_escolhida = random.choice(palavras['Comidas'])
            break
        elif escolha.upper() == 'ANIMAIS':
            palavra_escolhida = random.choice(palavras['Animais'])
            break
        elif escolha.upper() == 'PAÍSES':
            palavra_escolhida = random.choice(palavras['Países'])
            break
        else:
            print('Erro! Tente novamente\n')
    limpar()
    return palavra_escolhida

def jogar_de_novo():
    while True:
        jogar_novamente = input('Você deseja jogar novamente?S/N:  ')
        if jogar_novamente.lower() in 'sn':
            break
        else:
            print('Erro! Digite apenas S ou N.')
    if jogar_novamente.upper() == 'N':
        print('------------------Obrigada por jogar!-------------------')
        sair = True
    else:
        sair = False
    return sair

# Sistema de pontuação (desafio 6): o jogador começa com 600 pontos e a cada erro perde 100 pontos e a cada acerto ganha 100 + 25 pontos bônus (dependendo das tentativas restantes) + 50 pontos bônus por acertos consecultivos.
# Regra adicional(desafio 4): se a pontuação <= 0 o jogo termina e se acertar 3 letras consecultivas ganha uma pontuação bônus de 50 pontos.
def verificar_chute(palavra_secreta, espacos, erro, tentativas, dific, dica):
    errou = False
    acertou = False
    lista_de_chutes = []
    global pontuacao
    pontuacao = 600
    acertos_consecultivos = 0
    print('Você tem', pontuacao, 'pontos')
    while acertou==False and errou==False:
        chute = input('Digite uma letra:  ')
        posicao = 0
        nao_tem_letra = True
        if chute.upper() in lista_de_chutes:
            print('Essa letra já foi')
        for i in palavra_secreta:
            if (chute.upper() == i.upper()):
                espacos[posicao] = i
                nao_tem_letra = False
            posicao += 1
        if nao_tem_letra == False and chute.upper() not in lista_de_chutes:
            pontuacao += 100
            print('Você ganhou 100 pontos por acertar a letra!')
            acertos_consecultivos += 1 
            if tentativas - erro <= 3:
                pontuacao += 25
                print('Você ganhou 25 pontos bônus por acertar a letra com base as tentativas de erro')
            if acertos_consecultivos >= 3:
                pontuacao += 50
                print('Você ganhou 50 pontos por acertar', acertos_consecultivos,'letras consecultivas!')
            print('Agora você tem', pontuacao, 'pontos')
        if chute not in lista_de_chutes:
            if nao_tem_letra == True and chute.upper() not in lista_de_chutes:
               print('Na palavra não existe essa letra')
               erro += 1
               print (f'Você perdeu 100 pontos')
               pontuacao -= 100
               print('Você tem', pontuacao, 'pontos')
               acertos_consecultivos = 0
            if erro == tentativas or pontuacao == 0:
                limpar()
                print('-='*55)
                print('Você perdeu o jogo!')
                print('A palavra era:', palavra_secreta)
                fim_de_jogo()
                errou = True
        
        lista_de_chutes.append(chute.upper()) 
        print('-'*45)
        print(dica)
        if dific.upper() == 'DIFÍCIL':
            desenho_forca_dificil(erro)
        else:
            desenho_forca(erro)
        print(espacos)

        if '_' not in espacos:
            limpar()
            print('-='*55)
            print('VOCÊ GANHOU!!')
            print('A palavra era:', palavra_secreta)
            fim_de_jogo()
            acertou = True
    return acertou

# Banco de palavras (desafio 1): onde a chave é a categoria da palavra e o valor é uma lista de palavras (que serão escolhidas na função escolha_de_palavras())
# Dicas (desafio 2): dependendo da palavra escolhida, será imprimido uma dica contida no dicionário
def forca():
    sair = False
    erro = 0 
    palavras = {'Comidas': ['pizza', 'arroz', 'banana', 'feijoada', 'abacate', 'uva', 'pepino', 'caju', 'bife', 'abacaxi', 'salada'], 'Animais': ['falcao', 'cachorro', 'gato', 'raposa', 'galinha', 'elefante', 'abelha', 'aranha', 'borboleta', 'cavalo', 'camelo',], 'Países': ['Italia', 'Egito', 'Cuba', 'Vietna', 'Luxemburgo', 'Canada', 'Japao', 'Kuwait', 'Colombia', 'Argentina', 'Madagascar'] }
    dicas_das_palavras = {'pizza': 'Dica: Famosa na Itália', 'arroz': 'Dica: Consumimos todos os dia', 'banana': 'Dica: amarela', 'feijoada': 'Dica: Prato tradicional Brasileiro', 'abacate': 'Dica: Ultilizado em um típico prato mexicano', 'uva': 'Dica: tem lindos cachos', 'pepino': 'Dica: Longo e verde', 'caju': 'Dica: Castanha', 'bife': 'Dica: Proteína', 'abacaxi': 'Dica: É um grande rei', 'salada': 'Dica: Mistura', 'falcao': 'Dica: Ave de rapina', 'cachorro': 'Dica: Um bom companheiro', 'gato': 'Dica: Rei do Egito Antigo', 'raposa': 'Dica: Dora Aventureira', 'galinha': 'Dica: Bota ovo',
                     'elefante': 'Dica: Maior mamífero terrestre', 'abelha': 'Dica: Vivem em uma hierarquia', 'aranha': 'Dica: Rendeira', 'borboleta': 'Dica: Metamorfose', 'cavalo': 'Dica: Usado como meio de tranporte', 'camelo': 'Dica: Deserto', 'Italia': 'Dica: Conhecida pelo movimento renascentista', 'Egito': 'Dica: Possui um famoso rio como fonte de energia', 'Cuba': 'Dica: Comunista', 'Vietna': 'Dica: Marcado por sua grande guerra junto aos EUA, logo após a Segunda Guerra Mundial', 'Luxemburgo': 'Dica: Um dos primeiros a ingressar na UE', 'Canada': 'Dica: Multicultural', 'Japao': 'Dica: Arquipélogo', 'Kuwait': 'Conhecido pela sua grande quantidade de petróleo', 'Colombia': 'Dica: O segundo país mais populoso da América do Sul', 'Argentina': 'Dica: Um dos principais produtoras de alimento do mundo', 'Madagascar': 'Dica: Nome de um filme'}
    tentativas = 0
    while True:
        start = input('Vamos Começar?S/N\n')
        if start.lower() in 'sn':
            break
        else:
            print('Erro! Digite apenas S ou N.')
    if start.upper() == 'S':
        while sair == False:
            limpar()
            tentativas = dificuldade()
            limpar()
            print('Você tem', tentativas, 'chances de errar')
            palavra_escolhida = escolha_de_palavra(palavras)
            dica = dicas_das_palavras[palavra_escolhida]
            print('O jogo irá terminar quando acertar ou errar a palavra ou se sua potuação ficar em 0')
            print(dica)
            palavra_secreta = palavra_escolhida
            espacos = []
            qnt_letras = len(palavra_secreta)
            for letra in palavra_secreta:
                if letra == ' ':
                    espacos.append(' ')
                else:
                    espacos.append('_')
            qnt_letras = len(espacos)
            print('A palavra possui', qnt_letras, 'letras\n', espacos)
            if dific.upper() == 'DIFÍCIL':
                desenho_forca_dificil(erro)
            else:
                desenho_forca(erro)
            acertou = verificar_chute(palavra_secreta,espacos, erro, tentativas, dific, dica)
            print('Você fez',pontuacao, 'pontos')
            sair = jogar_de_novo()
    else:
        print('------------------Obrigada por jogar!-------------------')   
        
# Multijogador (desafio 9):  no primeiro turno, um dos jogadores irá colocar sua palavra e uma dica (mestre da rodada); no segundo turno, o outro jogador irá tentar a palavra (jogador da rodada).
def forcamultijogador():
    sair = False
    erro = 0 
    tentativas = 0
    while True:
        start = input('Vamos Começar?S/N\n')
        if start.lower() in 'sn':
            break
        else:
            print('Erro! Digite apenas S ou N.')
    if start.upper() == 'S':
        while sair == False:
            palavra_secreta = input('Mestre, escreva sua palavra secreta: ')
            dica = input('Insira a dica para a palavra secreta: ')
            dica = 'Dica: '+ dica
            limpar()
            print('Jogador, já pode jogar!')
            print('Insira a dificuldade para estabelecer o número de tentativas')
            tentativas = dificuldade()
            print(dica)
            espacos = []
            qnt_letras = len(palavra_secreta)
            for letra in palavra_secreta:
                if letra == ' ':
                    espacos.append(' ')
                else:
                    espacos.append('_')
            qnt_letras = len(espacos)
            print('A palavra possui', qnt_letras, 'letras\n', espacos)
            if dific.upper() == 'DIFÍCIL':
                desenho_forca_dificil(erro)
            else:
                desenho_forca(erro)
            acertou = verificar_chute(palavra_secreta,espacos, erro, tentativas, dific, dica)
            if acertou == True:
                print('O mestre perdeu :( \nO jogador venceu com', pontuacao,'pontos!')
            else:
                print('O jogador perdeu :(\nO mestre venceu!')
            sair = jogar_de_novo()
    else:
        print('------------------Obrigada por jogar!-------------------')  


print('-='*55)
print(' ______   _______   __      __         __      __   __   __   __   ____    _______         ____       _______ ')
print('|   _  \ |   ____| |  \    /  |       \  \    /  / |__| |  \ |  | |    \  |   _   |       /    \     |   _   |')
print('|  |_> | |  |____  |   \  /   |  ___   \  \  /  /   __  |   \|  | |  |\ \ |  | |  |      /  /\  \    |  | |  |')
print('|   _ \  |   ____| |  \ \/ /  | |___|   \  \/  /   |  | |  \ |  | |  | | ||  | |  |     /  /__\  \   |  | |  |')
print('|  |_> | |  |____  |  |\__/|  |          \    /    |  | |  |\   | |  |_/ /|  |_|  |    /  ______  \  |  |_|  |')
print('|_____/  |_______| |__|    |__|           \__/     |__| |__| \__| |_____/ |_______|   /__/      \__\ |_______|')
print('                   __   _______   _______   _______     ____        ____          ________')
print('                  |  | |   _   | |  _____| |   _   |   |    \      /    \        |        |')
print('                  |  | |  | |  | |  |  __  |  | |  |   |  |\ \    /  /\  \       |        ●')
print('               __ |  | |  | |  | |  | |_ | |  | |  |   |  | | |  /  /__\  \      |       /|\ ')
print('              (  \|  | |  |_|  | |  |__| | |  |_|  |   |  |_/ / /  ______  \     |       / \ ')
print('               \_____| |_______| |_______| |_______|   |_____/ /__/      \__\    |_____')
print('-='*55)
print(' ')
jogadores = []
while True:
    modo_de_jogo = input('Como deseja jogar?\n - solo \n - multiplayer\n')
    if modo_de_jogo.lower() == 'solo' or modo_de_jogo.lower() == 'multiplayer':
        break
    else:
        print('Erro! digite corretamente')
if modo_de_jogo.upper() == 'SOLO':
    registro_de_jogadores(jogadores,1)
    forca()
elif modo_de_jogo.upper() == 'MULTIPLAYER':
    registro_de_jogadores(jogadores,2)
    forcamultijogador()