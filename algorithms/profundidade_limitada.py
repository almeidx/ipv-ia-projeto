from distances import distancias_cidades


def profundidade_limitada(origem, destino, limite):
    def dfs(cidade, caminho, profundidade, distancia):
        if cidade == destino:
            return distancia, caminho + [cidade]

        if profundidade == 0:
            return 0, None

        for proxima_cidade in distancias_cidades[cidade]:
            if proxima_cidade not in caminho:
                nova_distancia = distancia + distancias_cidades[cidade][proxima_cidade]
                resultado, distancia_resultado = dfs(
                    proxima_cidade, caminho + [cidade], profundidade - 1, nova_distancia
                )

                if resultado is not None:
                    return resultado, distancia_resultado

        return 0, None

    return dfs(origem, [], limite, 0)
