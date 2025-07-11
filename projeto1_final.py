def eh_tabuleiro(tab):
    """"
    Verifica se o argumento fornecido representa um tabueiro válido.

    Um tabuleiro válido é representado por um tuplo de tuplos contendo inteiros.
    Deve satisfazer as seguintes condições:
    - Ser um tabulero com no máximo 100 linhas
    - Cada elemento do tuplo deve ser outro tuplo
    - Todas as linhas devem ter o mesmo comprimento (mínimo 2)
    - Cada posição deve conter um inteiro: 1, -1 ou 0

    Args:
    - tab: Tabuleiro a verificar
    """
    if type(tab) != tuple or len(tab) < 2:
        return False
    for i in range(len(tab)):
        if type(tab[i]) != tuple or len(tab[0]) < 2 or len(tab[0]) != len(tab[i]) or len(tab[i]) > 100:
            return False
        for j in range(len(tab[i])):
            if tab[i][j] not in [-1, 0, 1] or type(tab[i][j]) != int:
                return False
    return True


def eh_posicao(posicao):
    """"
    Verifica se o argumrnto forncecido representa uma posição dum tabuleiro.

    Deve satisfaze a seguinte condição:
    - A posição é um inteiro positivo

    Args:
    - posicao: Posição do tabuleiro
    """
    if type(posicao) != int or posicao <= 0 or posicao >= 20000:
        return False
    return True


def obtem_dimensao(tab):
    """
    Devolve um tuplo com as dimensões do tabuleiro (m, n).

    Args:
    - tab: Tabuleiro a verificar
    """
    return len(tab), len(tab[0])


def obtem_valor(tab, posicao):
    """
    Devolve o valor que se encontra na posição fornecida.

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição do tabuleiro
    """
    c = 1  # Variável auxiliar para contar as posições
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if c == posicao:
                return tab[i][j]
            c += 1


def obtem_coluna(tab, posicao):
    """
    Devolve um tuplo com todas as posições que se encontram na mesma coluna que a posição indicada

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição do tabuleiro
    """
    # Declaração do tuplo da coluna a ser obtida 
    coluna = ()

    # Atualizar a posição para o primeiro elemnto da coluna
    while posicao - len(tab[0]) > 0:
        posicao -= len(tab[0])

    # Ciclo para atualizar o tuplo da coluna até ter todas as posições da coluna
    while posicao <= len(tab) * len(tab[0]):
        coluna += (posicao, )
        posicao += len(tab[0])

    return coluna


def obtem_linha(tab, posicao):
    """
    Devolve um tuplo com todas as posições que se encontram na mesma linha que a posição indicada

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição do tabuleiro
    """
    # Declaração do tuplo da linha a ser obtida e variável auxiliar
    linha = ()
    i = 0

    # Atualizar a posição para o primeiro elemento da linha
    while (posicao - 1) % len(tab[0]) != 0:
        posicao -= 1

    # Ciclo para atualizar o tuplo da linha até ter todas as posições da linha
    while i != len(tab[0]):
        linha += (posicao, )
        posicao += 1
        i += 1

    return linha


def obtem_diagonais(tab, posicao):
    """
    Devolve um tuplo formado por dois tuplos correspondentes às posicões 
    da diagonal e da antidiagonal que passam pela posição fornecida

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição do tabuleiro
    """
    # Declaração das diagonais a serem obtidas e variáveis auxiliares
    res = ()
    num_linhas = len(tab)
    num_colunas = len(tab[0])
    posicao2 = posicao
    diagonal = ()
    antidiagonal = ()
    # Obter as posições da primeira e última coluna do tabuleiro através de funções previamente criadas
    ultima_coluna = obtem_coluna(tab, len(tab[0])) 
    primeira_coluna = obtem_coluna(tab, 1)

    # Obter a diagonal descendente
    while posicao - (num_colunas + 1) > 0 and posicao not in primeira_coluna:
        posicao -= (num_colunas + 1)
    while posicao <= num_colunas * num_linhas:
        diagonal += (posicao, )
        if posicao in ultima_coluna:
            break
        posicao += (num_colunas + 1)

    # Obter a diagonal ascendente
    while posicao2 - (num_colunas - 1) > 1 and posicao2 not in ultima_coluna:
        posicao2 -= (num_colunas - 1)
    while posicao2 <= num_colunas * num_linhas:
        antidiagonal = (posicao2, ) + antidiagonal
        if posicao2 in primeira_coluna:
            break
        posicao2 += (num_colunas - 1)

    # Juntar a diagonal com a antidiagonal num só tuplo
    res = (diagonal, antidiagonal)
    return res


def tabuleiro_para_str(tab):
    """
    Devolve uma representativa do tabuleiro no formato de uma string.

    O tabuleiro deve ser representado por uma string em formato de matriz seguindo as seguintes condições:
    - As linhas devem estar separadas por '\n'
    - O jogador 1 deve ser representado por 'X'
    - O jogador 2 deve ser representado por 'O'
    - As posições vazias devem ser representadas por '+'
    - As posições de cada linha devem estar separadas por '---'
    - As posições de cada coluna devem estar separadas por '|'

    Args:
    - tab: Tabuleiro a converter
    """
    #Obtem um número de colunas e linhas do tabuleiro
    num_colunas = len(tab[0])
    num_linhas = len(tab)
    resultado = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            # Caso seja 1 adiciona à lista da linha 'X' que representa o jogador 1
            if tab[i][j] == 1:
                linha.append('X')
            # Caso seja -1 adiciona à lista da linha 'O' que representa o jogador 1
            elif tab[i][j] == -1:
                linha.append('O')
            # Caso seja 0 adiciona à lista da linha '+' que representa uma posição vazia
            else:
                linha.append('+')
        # Adiciona a linha ao resultado e adiciona entre os valores '---'
        resultado.append('---'.join(linha))
        # 
        if i != num_linhas - 1:
            # Adiciona os separadores '|' entre as colunas
            resultado.append('|   ' * (num_colunas - 1) + '|')
    # Converte a lista de strings em uma única string        
    return '\n'.join(resultado)


def eh_posicao_valida(tab, posicao):
    """
    Verifica se a posição fornecida corresponde a uma posição do tabuleiro.

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição a verificar
    """
    #Verificar argumentos
    if not eh_posicao(posicao) or not eh_tabuleiro(tab):
        raise ValueError("eh_posicao_valida: argumentos invalidos")
    # Se a posição for maior que o tamanho do tabuleiro, retorna False
    if posicao > len(tab) * len(tab[0]):
        return False
    else:
        return True


def eh_posicao_livre(tab, posicao):
    """
    Verifica que a posição fornecida corresponde a uma posição livre (não ocupada por pedras) no tabuleiro.

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição a verificar
    """
    #Verificar argumentos
    if not eh_posicao(posicao) or not eh_tabuleiro(tab) or not eh_posicao_valida(tab, posicao):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    # Se o valor da posição for igual a 0, retorna True. Caso contrário, retorna False.
    return obtem_valor(tab, posicao) == 0


def obtem_posicoes_livres(tab):
    """
    Devolve um tuplo com todas as posições livres no tabuleiro, ordenadas por ordem crescente.

    Args:
    - tab: Tabuleiro a verificar
    """
    # Criar tuplo vazio para armazenar as posições livres
    posicoes_livres = ()
    # Verificar argumentos
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    # Percorrer o as posições do tabuleiro e adicionar as posições livres ao tuplo
    for i in range(1, len(tab) * len(tab[0]) + 1):
        if obtem_valor(tab, i) == 0:
            posicoes_livres += (i, )
    return posicoes_livres


def obtem_posicoes_jogador(tab, jog):
    """
    Devolve um tuplo com todas as posições ocupadas por um determinado jogador no tabuleiro, ordenadas por ordem crescente.
    O jogador deve ser 1 ou -1 (1 para o jogador das pedras pretas ou -1 para os jogadores das pedras brancas).

    Args:
    - tab: Tabuleiro a verificar
    - jog: int(-1 ou 1): Identificador do jogador
    """
    # Criar tuplo vazio para armazenas as posições ocupadas pelo jogador
    posicoes_jogador = ()
    # Verificar argumentos
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (1, -1):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    # Percorrer as posições do tabuleiro e adicionar as posições ocupadas pelo jogador ao tuplo
    for i in range(1, len(tab) * len(tab[0]) + 1):
        if obtem_valor(tab, i) == jog:
                posicoes_jogador += (i, )
    return posicoes_jogador


def posicao_para_coordenadas(posicao, colunas):
    """
    Devolve as coordenadas (linha, coluna) da posição fornecida no tabuleiro.

    Args:
    - posicao: Posição no tabuleiro
    - colunas: Número de colunas do tabuleiro
    """
    posicao -= 1  # Converter para indexação zero-based
    return (posicao // colunas, posicao % colunas) # Devolve um tuplo (linha, coluna)

def distancia_chebyshev(tab, posicao, posicao2):
    """
    Devolve a distância de Chebyshev entre duas posições no tabuleiro.

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição no tabuleiro
    - posicao2: Outra posição no tabuleiro
    """
    # Obter número de colunas e linhas do tabuleiro
    linhas = len(tab)
    colunas = len(tab[0])

    # Converter as posições em coordenadas (linha, coluna)
    lin1, col1 = posicao_para_coordenadas(posicao, colunas)
    lin2, col2 = posicao_para_coordenadas(posicao2, colunas)

    # Calcular a distância de Chebyshev
    return max(abs(lin1 - lin2), abs(col1 - col2))


def obtem_posicoes_adjacentes(tab, posicao):
    """
    Devolve um tuplo formado pelas posições do tabuleiro adjacentes, ordenados de menor a maior.
    Para uma posição ser adjacente a outra, a distância de Chebyshev tem de ser igual a um.

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição no tabuleiro
    """

    # Verificar argumentos
    if not eh_posicao(posicao) or not eh_tabuleiro(tab) or posicao > len(tab) * len(tab[0]):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    # Criar tuplo vazio para armazenar as posições adjacentes
    posicoes_adjacentes = ()
    # Percorrer as posições do tabuleiro
    for i in range(1, len(tab) * len(tab[0]) + 1):
        # Caso a distância de Chebyshev seja igual a 1, adiciona a posição ao tuplo de posições adjacentes
        if distancia_chebyshev(tab, posicao, i) == 1:
            posicoes_adjacentes += (i, )
    # Ordenar de menor para maior o tuplo das posições adjacentes e devolve o tuplo já ordenado
    posicoes_adjacentes = tuple(sorted(posicoes_adjacentes))
    return posicoes_adjacentes


def posicao_central(tab):
    """
    Devolve a posição central do tabuleiro, que é a posição que está no centro da matriz, segundo um cálculo concreto

    Args:
    - tab: Tabuleiro a verificar
    """
    # Obtem o número de linhas e colunas do tabuleiro
    linhas = len(tab)
    colunas = len(tab[0])
    # Calcula a posição central do tabuleiro
    c = (linhas // 2) * colunas + colunas // 2 + 1
    return c


def ordena_posicoes_tabuleiro(tab, tup):
    """
    Devolve um tuplo com as posições em ordem ascendente de acordo com a distância de Chebyshev da posição central do tabuleiro.
    Posições com igual distância à posição central são ordenadas de menor a maior de acordo com a posição que ocupam no tabuleiro.

    Args:
    - tab: Tabuleiro a verificar
    - tup: Tuplo com as posições a ordenar
    """
    #  Verifica se os argumentos são válidos
    if not eh_tabuleiro(tab) or type(tup) != tuple:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    
    # Verifica se todas as posições no tuplo são válidas
    for i in tup:
        if type(i) != int or i < 1 or i > len(tab) * len(tab[0]) or not eh_posicao_valida(tab, i):
            raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    
    # Cria uma lista de tuplos (posição, distância) e obtem a posição central, recorrendo a uma função previamente definida
    posicoes_com_distancia = []
    centro = posicao_central(tab)
    # Preenche a lista com tuplos (posição, distância)
    for pos in tup:
        dist = distancia_chebyshev(tab, centro, pos)
        posicoes_com_distancia.append((pos, dist))
    # Ordena a lista usando bubble sort
    n = len(posicoes_com_distancia)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compara as distâncias
            if posicoes_com_distancia[j][1] > posicoes_com_distancia[j+1][1]:
                posicoes_com_distancia[j], posicoes_com_distancia[j+1] = posicoes_com_distancia[j+1], posicoes_com_distancia[j]
            # Se as distâncias são iguais, compara as posições
            elif posicoes_com_distancia[j][1] == posicoes_com_distancia[j+1][1]:
                if posicoes_com_distancia[j][0] > posicoes_com_distancia[j+1][0]:
                    posicoes_com_distancia[j], posicoes_com_distancia[j+1] = posicoes_com_distancia[j+1], posicoes_com_distancia[j]
    
    # Extrai apenas as posições ordenadas
    return tuple(pos for pos, _ in posicoes_com_distancia)


def marca_posicao(tab, posicao, jog):
    """
    Devolve um novo tabuleiro com uma nova jogada do jogador indicado nessa posição.

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição livre no tabuleiro onde a jogada será feita
    - jog: Jogador que pretende fazer a jogada (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    """
    # Verifica se os argumentos são válidos
    if not eh_posicao(posicao) or not eh_tabuleiro(tab) or jog not in (1, -1) or obtem_valor(tab, posicao) != 0:
        raise ValueError("marca_posicao: argumentos invalidos")
    # Criar variáveis auxiliares
    c = 0
    l = ()
    res = ()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            c += 1
            if c == posicao:
                l += (jog, )
            else:
                l += (tab[i][j], )
        res += (l,)
        l = ()
    return res


def verifica_k_linhas(tab, posicao, jog, k):
    """"
    Verifca se existe pelo menos uma linha, coluna ou diagonal que contenha a posição com k ou mais pedras consecutivas do jogador indicado

    Args:
    - tab: Tabuleiro a verificar
    - posicao: Posição na qual a verificação será feita
    - jog: Jogador que pretende verificar as sequências (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    - k: Número de pedras consecutivas que se pretende verificar
    """

    # Verifica se os argumentos são válidos
    if not eh_posicao(posicao) or not eh_tabuleiro(tab) or not eh_posicao_valida(tab, posicao)  or type(jog) != int or jog not in (1, -1) or type(k) != int or k < 1:
        raise ValueError("verifica_k_linhas: argumentos invalidos")
    
    # Verifica se a posição está ocupada pelo jogador
    if obtem_valor(tab, posicao) != jog:
        return False
    
    # Obter as linhas, colunas e diagonais
    linha = obtem_linha(tab, posicao)
    coluna = obtem_coluna(tab, posicao)
    diagonais = obtem_diagonais(tab, posicao)

    # Função auxiliar para contar sequências
    def conta_sequencia(sequencia):
        contador = 0
        posicao_index = sequencia.index(posicao)
        for i, pos in enumerate(sequencia):
            if obtem_valor(tab, pos) == jog:
                contador += 1
                if contador >= k and posicao_index in range(i-k+1, i+1):
                    return True
            else:
                contador = 0
        return False
    # Verifica linha, coluna e diagonais
    return (conta_sequencia(linha) or 
            conta_sequencia(coluna) or 
            conta_sequencia(diagonais[0]) or 
            conta_sequencia(diagonais[1]))


def eh_fim_jogo(tab, k):
    """
    Verifica se o jogo terminou(True) ou não(False).

    Um jogo considera-se terminado nos seguintes casos:
    - Todas as posições estão ocupadas (não existem mais posições livres)
    - Um dos jogadores tem k pedras consecutivas numa linha, coluna ou diagonal.

    Args:
    - tab: Tabuleiro a verificar
    - k: Número de pedras consecutivas que se pretende verificar
    """

    # Verifica se os argumentos são válidos
    if not eh_tabuleiro(tab) or type(k) != int or k < 1:
        raise ValueError("eh_fim_jogo: argumentos invalidos")
    
    # Verifica se existem posições livres no tabuleiro
    if len(obtem_posicoes_livres(tab)) == 0:
        return True
    # Verifica se o jogo terminou com k pedras consecutivas numa linha, coluna ou diagonal
    for i in range(1, len(tab) * len(tab[0]) + 1):
        if verifica_k_linhas(tab, i, 1, k) or verifica_k_linhas(tab, i, -1, k):
            return True
    # Caso nenhum dos casos tenha sido verificado, retorna False
    return False


def escolhe_posicao_manual(tab):
    """"
    Devolve uma posição introduzida manualmente pelo jogador.
    A função deve apresentar uma mensagem de texto, repetindo a mensagem até o jogador introduzir uma posição livre.

    Args:
    - tab: Tabuleiro a verificar
    """
    # Verifica se os argumentos são válidos
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    # Pede ao jogador para introduzir uma posição livre e enquanto não o fizer continuar a pedir
    while True:
        escolha_jogador = input("Turno do jogador. Escolha uma posicao livre: ")
        if not escolha_jogador.isdigit():
            continue
        escolha_jogador = int(escolha_jogador)
        if eh_posicao(escolha_jogador) and obtem_valor(tab, escolha_jogador) == 0:
            return escolha_jogador


def posicao_auto_facil(tab, jog):
    """"
    Devolve a posição escolhida segundo a 'Estratégia fácil'
    Segundo esta estratégia:
    - Se existir no tabuleiro pelo menos uma posição livre e adjacente a uma pedra própria, jogar numa dessas posições
    - Se não, jogar numa posição livre
    - Caso mais de uma posição cumpra um dos critérios, deve escolher a posição mais próxima da posição do central do tabuleiro

    Args:
    - tab: Tabuleiro a verificar
    - jog: Jogador que pretende escolher a posição (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    """
    # Cria tuplo com as posições ocupadas pelo jogador em tuplo vazio onde vão ser armazenadas as posições adjacentes
    posicoes_ocupadas = obtem_posicoes_jogador(tab, jog)
    posicoes_adjacentes = ()
    #Percorre o tuplo das posições ocupadas e obtem as posições adjacentes a essas posições
    for i in posicoes_ocupadas:
        if obtem_posicoes_adjacentes(tab, i) not in posicoes_adjacentes:
            posicoes_adjacentes += obtem_posicoes_adjacentes(tab, i)
        # Percorre o tuplo das posições adjacentes ordenada por distância ao centro e verifica se existe alguma posição livre
    for j in ordena_posicoes_tabuleiro(tab, posicoes_adjacentes):
        if eh_tabuleiro(tab) and eh_posicao(j) and eh_posicao_valida(tab, j) and eh_posicao_livre(tab, j):
            return j
    
    # Se não existir posições que satisfazem a condição anterior, 
    #   obtém as posições livres e ordena-as pela distância do centro e devolve
    #       a posição livre mais próxima do centro
    posicoes_livres = obtem_posicoes_livres(tab)
    return ordena_posicoes_tabuleiro(tab, posicoes_livres)[0]


def conta_max_consecutivas(tab, jog):
    """
    Devolve o número máximo de pedras consecutivas que o jogador pode chegar a ter na próxima jogada

    Args:
    - tab: Tabuleiro a verificar
    - jog: Jogador que pretende verificar
    """
    # Contador de jogadas consecutivas
    max_consecutivas = 0
    for posicao in range(1, len(tab) * len(tab[0]) + 1):
        if eh_posicao_livre(tab, posicao):
            novo_tab = marca_posicao(tab, posicao, jog)
            for sequencia in [obtem_linha(novo_tab, posicao), 
                obtem_coluna(novo_tab, posicao), 
                obtem_diagonais(novo_tab, posicao)[0], 
                obtem_diagonais(novo_tab, posicao)[1]]:
                consecutivas = 0
                for pos in sequencia:
                    if obtem_valor(novo_tab, pos) == jog:
                        consecutivas += 1
                        max_consecutivas = max(max_consecutivas, consecutivas)
                    else:
                        consecutivas = 0
    return max_consecutivas


def posicao_auto_normal(tab, jog, k):
    """
    Devolve a posição escolhida segundo a 'Estratégia normal'
    Segundo esta estratégia:
    - Determinar o maior valor de L tal que o próprio jogador ou o adversário podem colocar L peças consecutivas na próxima jogada
        - Se existir pelo menos uma posição que permita obter uma linha que contenha essa posição com L pedras consecutivas próprias,
            jogar numa dessas posições
        - Se não, jogar numa posição que impossiblite o adversário de obter L pedras consecutivas numa linha que contenha essa posição
        - Caso mais de uma posição cumpra um dos critérios, deve escolher a posição mais próxima da posição do central do tabuleiro

    Args:
    - tab: Tabuleiro a verificar
    - jog: Jogador que pretende escolher a posição (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    - k: Número de pedras consecutivas que se pretende verificar
    """
    # Obtem um máximo de pedras consecutivas que o jogador ou o adversário pode chegar a ter na próxima jogada
    max_jog = conta_max_consecutivas(tab, jog)
    max_adv = conta_max_consecutivas(tab, -jog)
    # Criar um tuplo para guardar as melhores jogadas para depois serem ordenadas de acordo com a distância do centro
    melhores_jogadas = ()
    # Estratégia ofensiva
    if max_jog >= k:
        for i in obtem_posicoes_livres(tab):
            n_tab = marca_posicao(tab, i, jog)
            if verifica_k_linhas(n_tab, i, jog, k):
                melhores_jogadas += (i,)
        if melhores_jogadas:
            return ordena_posicoes_tabuleiro(tab, melhores_jogadas)[0]
        
    # Estratégia defensiva
    if max_adv >= k:
        for i in obtem_posicoes_livres(tab):
            n_tab = marca_posicao(tab, i, -jog)
            if verifica_k_linhas(n_tab, i, -jog, k):
                melhores_jogadas += (i,)
        if melhores_jogadas:
            return ordena_posicoes_tabuleiro(tab, melhores_jogadas)[0]
    
    # Caso nenhum dos casos tenha sido verificado, aumenta o número de jogadas consecutivas
    if max_jog >= max_adv:
        for i in obtem_posicoes_livres(tab):
            n_tab = marca_posicao(tab, i, jog)
            if conta_max_consecutivas(n_tab, jog) > max_jog:
                melhores_jogadas += (i,)
        if melhores_jogadas != ():
            return ordena_posicoes_tabuleiro(tab, melhores_jogadas)[0]
    else:
        for i in obtem_posicoes_livres(tab):
            n_tab = marca_posicao(tab, i, jog)
            if conta_max_consecutivas(n_tab, -jog) < max_adv:
                melhores_jogadas += (i,)
        if melhores_jogadas != ():
            return ordena_posicoes_tabuleiro(tab, melhores_jogadas)[0]

    # Caso nenhum dos casos tenha sido verificado, devolve a posição livre mais próxima do centro do tabuleiro
    posicoes_livres = obtem_posicoes_livres(tab)
    return ordena_posicoes_tabuleiro(tab, posicoes_livres)[0]


def simula_jogo(tab, jog, posicao_inicial, k):
    """
    Simula um jogo completo começando com a jogada do jogador atual na posição inicial.

    Args:
    - tab: Tabuleiro inicial
    - jog: Jogador que começa a jogar (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    - posicao_inicial: Posição inicial do jogador
    - k: Número de pedras consecutivas que se pretende verificar
    """
    novo_tab = marca_posicao(tab, posicao_inicial, jog)
    jogador_atual = -jog

    while not eh_fim_jogo(novo_tab, k):
        prox_posicao = posicao_auto_normal(novo_tab, jogador_atual, k)
        novo_tab = marca_posicao(novo_tab, prox_posicao, jogador_atual)
        jogador_atual = -jogador_atual

    # Determinar o vencedor
    for i in range(1, len(novo_tab) * len(novo_tab[0]) + 1):
        if verifica_k_linhas(novo_tab, i, jog, k):
            return jog
        if verifica_k_linhas(novo_tab, i, -jog, k):
            return -jog
    return 0  # Empate


def posicao_auto_dificil(tab, jog, k):
    """
    Devolve a posição escolhida segundo a 'Estratégia difícil'
    Segundo esta estratégia:
    - Se existir pelo menos uma posição que permita obter uma linha própria
        com k pedras consecutivas, jogar numa dessas posições.
    - Se não, e se exisir pelo menos uma posição que impossibilite ao adversário de obter uma linha com k pedras consecutivas, 
        jogar numa dessas posições.
    - Se não, para cada posição livrem simular um jogo até ao fim em que o jogador atual joga nessa posição e o resto 
        das jogadas são determinadas assumindo que os dois jogadoresjogam seguindo a 'Estratégia normal'. 
            Registar o resultado de cada simulação e escolher a posição que leva ao melhor resultado possível, isto é:
                - Se existir pelo menos uma posição que permiiria ganhar o jogo, 
                    jogar numa dessas posições.
                - Se não, e se existir peolo menos uma posição qe permiiria empatar o jogo,
                    jogar numa dessas posições.
                - Se não, jogar numa posição livre
        
    Args:
    - tab: Tabuleiro a verificar
    - jog: Jogador que pretende escolher a posição (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    - k: Número de pedras consecutivas que se pretende verificar
    """     
    # Obtem um máximo de pedras consecutivas que o jogador ou o adversário pode chegar a ter na próxima jogada
    max_jog = conta_max_consecutivas(tab, jog)
    max_adv = conta_max_consecutivas(tab, -jog)
    melhores_jogadas = ()
    # Estratégia para ganhar o jogo
    if max_jog >= k:
        for i in obtem_posicoes_livres(tab):
            n_tab = marca_posicao(tab, i, jog)
            if verifica_k_linhas(n_tab, i, jog, k):
                melhores_jogadas += (i,)
        if melhores_jogadas:
            return ordena_posicoes_tabuleiro(tab, melhores_jogadas)[0]
    # Estratégia defensiva para não perder o jogo
    if max_adv >= k:
        for i in obtem_posicoes_livres(tab):
            n_tab = marca_posicao(tab, i, -jog)
            if verifica_k_linhas(n_tab, i, -jog, k):
                melhores_jogadas += (i,)
        if melhores_jogadas:
            return ordena_posicoes_tabuleiro(tab, melhores_jogadas)[0]
        
    # Simulação de jogos
    melhores_posicoes = []
    posicoes_empate = []
    
    for posicao in obtem_posicoes_livres(tab):
        resultado = simula_jogo(tab, jog, posicao, k)
        if resultado == jog:  # Vitória
            melhores_posicoes.append(posicao)
        elif resultado == 0:  # Empate
            posicoes_empate.append(posicao)
    
    # Escolha da melhor posição
    if melhores_posicoes:
        return ordena_posicoes_tabuleiro(tab, tuple(melhores_posicoes))[0]
    elif posicoes_empate:
        return ordena_posicoes_tabuleiro(tab, tuple(posicoes_empate))[0]
    else:
        return ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))[0]


def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    Devolve a posição escolhida automaticamente de acordo com a estratégia selecionada.

    Args:
    - tab: Tabuleiro a verificar
    - jog: Jogador que pretende escolher a posição (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas)
    - k: Número de pedras consecutivas que se pretende verificar
    - lvl: Estratégia a utilizar ('facil', 'normal' ou 'dificil')
    """
    # Verificar se os argumentos são válidos
    if not eh_tabuleiro or type(jog) != int or jog not in (-1, 1) or type(k) != int or k <= 0 or type(lvl) != str or lvl not in ('facil', 'normal', 'dificil'):
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
    
    if lvl == 'facil':
        return posicao_auto_facil(tab, jog)
    elif lvl == 'normal':
        return posicao_auto_normal(tab, jog, k)
    else:
        return posicao_auto_dificil(tab, jog, k)


def jogo_mnk(cfg, jog, lvl):
    """
    Função principal que permite jogar um jogo completo de m, n, k de um jogador contra o computador.
    O jogo começa sempre com o jogador das pedras pretas.
    A função mostra o resultado do jogo (VITORIA, DERROTA ou EMPATE) e devolve um número inteiro identificando o jogador
        vencedor (1 para preto, -1 para branco ou 0 para empate).

    Args:
    - cfg: tup: Configurações do jogo (m, n, k)
    - jog: int: Identifica a cor das pedras do jogador humano (1 para pedras pretas, -1 para pedras brancas)
    - lvl: str: Estratégia a utilizar ('facil', 'normal' ou 'dificil')
    """
    # Verifica se os argumentos são válidos
    if type(cfg) != tuple or len(cfg) != 3 or type(jog) != int or jog not in (-1, 1) or lvl not in ('facil', 'normal', 'dificil'):
        raise ValueError("jogo_mnk: argumentos invalidos")
    for i in cfg:
        if type(i) != int or i <= 0:
            raise ValueError("jogo_mnk: argumentos invalidos")
    # Obtem o número de linhas, colunas do tabuleiro e o valor de k
    m = cfg[0]
    n = cfg[1]
    k = cfg[2]
    #Cria um tabuleiro com as dimensões especificadas e preenche-o com 0, ou seja, posições livres
    tab = tuple(tuple(0 for _ in range(n)) for _ in range(m))
    print("Bem-vindo ao JOGO MNK.")
    # Informa o jogador qual é a cor das suas pedras
    if jog == 1:
        print("O jogador joga com 'X'.")
    else:
        print("O jogador joga com 'O'.")
    # Mostra o tabuleiro inicial em string
    print(tabuleiro_para_str(tab))
    # O jogador inicial é sempre o jogador que joga com as pedras pretas
    jogador_atual = 1
    # Enquanto o jogo não está terminado, o jogo continua
    while not eh_fim_jogo(tab, k):
        if eh_tabuleiro == False or type(k) != int or k <= 0:
            raise ValueError("jogo_mnk: argumentos invalidos")
        # Quando o jogador atual é o humano a escolha da posição é a manual
        if jogador_atual == jog:
            pos = escolhe_posicao_manual(tab)
        # Caso contrário, a escolha da posição é automatica de acordo com a estratégia definida inicialmente
        else:
            print(f"Turno do computador ({lvl}):")
            pos = escolhe_posicao_auto(tab,jogador_atual, k, lvl)
        # Após a escolha da posição, marca-se a posição no tabuleiro, troca-se o jogador atual e mostra-se o novo tabuleiro em string
        tab = marca_posicao(tab, pos, jogador_atual)
        jogador_atual = -jogador_atual
        print(tabuleiro_para_str(tab))
    
    # Quando o jogo terminar, verifica-se qual dos jogadores venceu
    for i in range(1, len(tab) * len(tab[0]) + 1):
        if verifica_k_linhas(tab, i, jog, k):
            print("VITORIA")
            return jog
        if verifica_k_linhas(tab, i, -jog, k):
            print("DERROTA")
            return -jog
    # Caso nenhum dos jogadores tenha vencido, o jogo é considerado empatado
    print("EMPATE")
    return 0