from distances import distancias_entre_distritos
from coordenadas import calcular_distancia_coordenadas


def sofrega(origem, destino):
    if origem == destino:
        return 0, [destino]

    dist = 0
    cidade_atual = origem
    caminho = [origem]

    while True:
        filhos = distancias_entre_distritos[cidade_atual]
        cidade_mais_proxima = min(
            filhos, key=lambda x: calcular_distancia_coordenadas(x, destino)
        )

        dist += distancias_entre_distritos[cidade_atual][cidade_mais_proxima]
        cidade_atual = cidade_mais_proxima

        caminho.append(cidade_atual)

        if cidade_atual == destino:
            break

    return dist, caminho
