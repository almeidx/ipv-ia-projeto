# Procura Cega:
# - Custo Uniforme
# - Profundidade Limitada

# Heuristica:
# - A* = Sôfrega + Custo Uniforme
# - Sôfrega

from algorithms.custo_uniforme import custo_uniforme
from algorithms.profundidade_limitada import profundidade_limitada
from algorithms.sofrega import sofrega
from algorithms.a_star import a_star
from distances import distancias_cidades


def main():
    option = -1

    while option < 1 or option > 5:
        print("Escolha o algoritmo de procura:")
        print("1 - Custo Uniforme")
        print("2 - Profundidade Limitada")
        print("3 - Sôfrega")
        print("4 - A*")
        print("5 - Sair")
        option = int(input("Escolha: "))

    clear()

    if option == 1:
        print("Algoritmo de procura Cega - Custo Uniforme")

        origem = validar_distrito(input("Origem: "))
        destino = validar_distrito(input("Destino: "))

        result = custo_uniforme(origem, destino)

        print(f"Distância de {origem} a {destino}: {str(result[0])}km")
        print_caminho(result[1])
    elif option == 2:
        print("Algoritmo de procura Cega - Profundidade Limitada")

        origem = validar_distrito(input("Origem: "))
        destino = validar_distrito(input("Destino: "))
        limite = int(input("Limite: "))

        result = profundidade_limitada(origem, destino, limite)

        if result[1] is None:
            print(
                f"Não foi possível encontrar um caminho de {origem} a {destino} com limite de {str(limite)}."
            )
            exit(0)

        print(
            f"Distância de {origem} a {destino} com limite de {str(limite)}: {str(result[0])}km"
        )
        print_caminho(result[1])
    elif option == 3:
        print("Algoritmo de procura Heurística - Sôfrega")
        print("Destino é Faro")

        origem = validar_distrito(input("Origem: "))

        result = sofrega(origem)
        print(f"Distância de {origem} a Faro: {str(result)}km")
    elif option == 4:
        print("Algoritmo de procura Heurística - A*")

        origem = validar_distrito(input("Origem: "))

        result = a_star(origem)
        print(f"Distância de {origem} a Faro: {str(result[0])}km")
        print_caminho(result[1])
    else:
        exit(0)


def clear():
    print("\033[H\033[J")


def print_caminho(caminho):
    print("Caminho: ", end="")
    for index, cidade in enumerate(caminho):
        if index == len(caminho) - 1:
            print(cidade)
        else:
            print(cidade, end=" -> ")


def validar_distrito(county):
    if county not in distancias_cidades:
        print(f"O distrito {county} não existe.")
        exit(0)

    return county


if __name__ == "__main__":
    main()
