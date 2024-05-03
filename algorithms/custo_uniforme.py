from distances import distancias_entre_distritos


def custo_uniforme(origem, destino):
    fila = [(0, origem, [])]  # (custo acumulado, cidade atual, caminho até agora)
    visitados = set()

    while fila:
        fila.sort()  # Ordenar a fila pela prioridade (custo acumulado)
        custo, cidade, caminho = fila.pop(0)

        if cidade == destino:
            return custo, caminho + [cidade]

        if cidade in visitados:
            continue

        visitados.add(cidade)

        for proxima_cidade, custo_caminho in distancias_entre_distritos[cidade].items():
            if proxima_cidade not in visitados:
                fila.append((custo + custo_caminho, proxima_cidade, caminho + [cidade]))

    return float("inf"), None
