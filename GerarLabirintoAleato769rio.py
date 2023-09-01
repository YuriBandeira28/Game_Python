# Função para gerar labirintos nxn
def gerar_labirinto(largura, altura):
    # Inicializa o labirinto com paredes
    labirinto = [[1] * largura for _ in range(altura)]
    # Inicializa a matriz de visitados
    visitados = [[False] * largura for _ in range(altura)]
    # Escolhe uma célula inicial aleatória com coordenadas ímpares
    x, y = random.randint(0, (largura - 3) // 2) * 2 + 1, random.randint(0, (altura - 3) // 2) * 2 + 1
    
    # Função recursiva para realizar a busca em profundidade
    def dfs(x, y):
        # Marca a célula atual como visitada
        visitados[y][x] = True
        labirinto[y][x] = 0
        # Embaralha as direções para tornar o labirinto mais aleatório
        direcoes = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(direcoes)
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 < nx < largura - 1 and 0 < ny < altura - 1 and not visitados[ny][nx]:
                labirinto[(y + ny) // 2][(x + nx) // 2] = 0
                dfs(nx, ny)
    dfs(x, y)
    return labirinto
