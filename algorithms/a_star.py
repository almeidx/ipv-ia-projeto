from distances import distancias_entre_distritos, distancias_faro
from coordenadas import calcular_distancia_coordenadas


def a_star(origem, destino):
    fila = [(0, origem)]  # (custo acumulado + heurística, cidade)
    custo_acumulado = {cidade: float("inf") for cidade in distancias_entre_distritos}
    custo_acumulado[origem] = 0
    caminho = {}

    while fila:
        custo_atual, cidade_atual = fila.pop(0)

        if cidade_atual == destino:
            caminho_completo = [destino]
            while cidade_atual != origem:
                cidade_atual = caminho[cidade_atual]
                caminho_completo.append(cidade_atual)
            return custo_acumulado[destino], caminho_completo[::-1]

        for cidade_vizinha, custo in distancias_entre_distritos[cidade_atual].items():
            novo_custo = custo_acumulado[cidade_atual] + custo
            if novo_custo < custo_acumulado[cidade_vizinha]:
                custo_acumulado[cidade_vizinha] = novo_custo
                prioridade = novo_custo + calcular_distancia_coordenadas(
                    cidade_vizinha, destino
                )
                fila.append((prioridade, cidade_vizinha))
                caminho[cidade_vizinha] = cidade_atual

        fila.sort()

    return float("inf"), None
