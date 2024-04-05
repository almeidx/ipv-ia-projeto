from distances import distancias_cidades, distancias_faro


def a_star(origem):
    fila = [(0, origem)]  # (custo acumulado + heurística, cidade)
    custo_acumulado = {cidade: float("inf") for cidade in distancias_cidades}
    custo_acumulado[origem] = 0
    caminho = {}

    while fila:
        custo_atual, cidade_atual = fila.pop(0)

        if cidade_atual == "Faro":
            caminho_completo = ["Faro"]
            while cidade_atual != origem:
                cidade_atual = caminho[cidade_atual]
                caminho_completo.append(cidade_atual)
            return custo_acumulado["Faro"], caminho_completo[::-1]

        for cidade_vizinha, custo in distancias_cidades[cidade_atual].items():
            novo_custo = custo_acumulado[cidade_atual] + custo
            if novo_custo < custo_acumulado[cidade_vizinha]:
                custo_acumulado[cidade_vizinha] = novo_custo
                prioridade = novo_custo + distancias_faro[cidade_vizinha]
                fila.append((prioridade, cidade_vizinha))
                caminho[cidade_vizinha] = cidade_atual

        fila.sort()

    return float("inf"), None
