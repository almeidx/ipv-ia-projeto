from distances import distancias_entre_distritos


def profundidade_limitada(origem, destino, limite):
    def dfs(cidade, caminho, profundidade, distancia):
        if cidade == destino:
            return distancia, caminho + [cidade]

        if profundidade == 0:
            return None, None

        for proxima_cidade in distancias_entre_distritos[cidade]:
            if proxima_cidade not in caminho:
                nova_distancia = (
                    distancia + distancias_entre_distritos[cidade][proxima_cidade]
                )
                resultado, distancia_resultado = dfs(
                    proxima_cidade, caminho + [cidade], profundidade - 1, nova_distancia
                )

                if resultado is not None:
                    return resultado, distancia_resultado

        return None, None

    resultado, caminho = dfs(origem, [], limite, 0)
    if resultado is None:
        return float("inf"), None

    return resultado, caminho
