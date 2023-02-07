#  Uma função computador_escolhe_jogada que recebe, como parâmetros, os números
# n e m descritos acima e devolve um inteiro correspondente à próxima jogada do 
# computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de 
# acordo com a estratégia vencedora.

def computador_escolhe_jogada(n,m):
    jogada = m
    jogada_ok = False
    while jogada_ok == False:
        pecas_rest = n - jogada
        resto = float(pecas_rest % (m + 1))
        if resto == 0:
            return jogada
            jogada_ok = True
        else:
            jogada -= 1
            if jogada == 0:
                return m

#   Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita
# que o jogador informe sua jogada e verifica se o valor informado é válido. Se 
# o valor informado for válido, a função deve devolvê-lo; caso contrário, deve 
# solicitar novamente ao usuário que informe uma jogada válida.

def usuario_escolhe_jogada(n, m):
    jog_U_inval = True
    print("Entre com o número de peças que deseja retirar, entre 1 e", m, "peça(s).")
    while jog_U_inval:
        jogada_U = float(input("Peças: "))
        if jogada_U % 1 != 0: #jog_U_inval = True
            print("Valor deve ser inteiro!")
        else:
            if jogada_U > m: #jog_U_inval = True
                print("Valor deve ser menor ou igual a", m,"!!")
            else:
                if jogada_U == 0: #jog_U_inval = True
                    print("Você é obrigado a tirar pelo menos uma peça!!")
                else:
                    if jogada_U < 0: #jog_U_inval = True
                        print("Digite um número inteiro positivo!!")
                    else:
                        jog_U_inval = False
                        jogada_U = int(jogada_U)
    return jogada_U

def computador_decide(nn, mm):
    resto = float(nn % (mm+1))
    if resto == 0:
        print("")
        print("Você começa!")
        print("")
        return "Usuário"
    else:
        print("")
        print("Computador começa!")
        print("")
        return "Computador"

#   Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe
# os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário 
# (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser 
# feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, 
# deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas 
# na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função 
# imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

def partida():
    verif = False
    while verif == False:
        n = int(input("Entre com o número de peças iniciais do jogo. N: "))
        m = int(input("Agora com o número máx de peças a serem retiradas por jogada. M: "))
        if n >= m:
            verif = True
        else:
            print("Valor de n deve ser >= m")

    quem_joga = computador_decide(n, m)

    while n > 0:
        if quem_joga == "Computador":
            jogada = computador_escolhe_jogada(n,m)
            n -= jogada
            print("---COMPUTADOR------------------------")
            print("Retirou", jogada, "peças.")
            print("Restaram no jogo", n, "peças.")
            print("-------------------------------------")
            quem_joga = "Usuário"
        else:
            jogada = usuario_escolhe_jogada(n,m)
            n -= jogada
            print("---USUÁRIO---------------------------")
            print("Retirou", jogada,"peças.")
            print("Restaram no jogo", n, "peças.")
            quem_joga = "Computador"
    if quem_joga == "Computador":
        print("Você ganhou!")
        return "Você ganhou!"
    else:
        print("O computador ganhou!")
        return "O computador ganhou!"

#Campeonatos
# Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem
#é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você
#deverá criar uma outra função chamada campeonato. Essa nova função deve realizar
#três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas
#e indicar o vencedor do campeonato. O placar deve ser impresso na forma:
#Placar: Você ??? X ??? Computador

def campeonato():
    n_partidas = 3
    i = 1
    Cont_us = 0
    Cont_comp = 0
    while i <= n_partidas:
        print("")
        print("**** Rodada", i,"****")
        print("")
        res_unica = partida()
        if res_unica == "Você ganhou!":
            Cont_us += 1
        else:
            Cont_comp += 1
        i += 1
    print("")
    print("Placar: Você ", Cont_us ,"X", Cont_comp ,"Computador")
    print("")
    print("**** Final do campeonato! ****")
    print("")
#------------------------------------------------------------------------------
print("Seja bem vindo ao jogo de NIM!!!!")
print("-----------------------------------------")
print("Esse jogo se inicia com 'n' peças inicialmente dispostas numa mesa ou tabuleiro.")
print("Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo 'm' peças cada um.")
print("Quem tirar as últimas peças possíveis ganha o jogo.")
print("-----------------------------------------")
print("")
print("Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
print("")

escolha = int(input())
if escolha == 1:
    print("")
    print("Voce escolheu uma partida!")
    print("")
    partida()
else:
    print("")
    print("Voce escolheu um campeonato!")
    print("")
    campeonato()
