from algorithms.custo_uniforme import custo_uniforme
from algorithms.profundidade_limitada import profundidade_limitada
from algorithms.sofrega import sofrega
from algorithms.a_star import a_star
from distances import distancias_entre_distritos


def main():
    option = -1

    while option < 1 or option > 5:
        print("Escolha o algoritmo de procura:")
        print("1 - Custo Uniforme")
        print("2 - Profundidade Limitada")
        print("3 - Sôfrega")
        print("4 - A*")
        print("5 - Sair")

        try:
            option = int(input("Escolha: "))
        except ValueError:
            option = -1

    clear_terminal()

    if option == 1:
        print("Algoritmo de procura Cega - Custo Uniforme")

        origem = validar_distrito(input("Origem: "))
        destino = validar_distrito(input("Destino: "))

        result = custo_uniforme(origem, destino)

        print(f"Distância de {origem} a {destino}: {fmt_distance(result[0])}")
        print_caminho(result[1])
    elif option == 2:
        print("Algoritmo de procura Cega - Profundidade Limitada")

        origem = validar_distrito(input("Origem: "))
        destino = validar_distrito(input("Destino: "))
        profundidade = int(input("Limite: "))

        result = profundidade_limitada(origem, destino, profundidade)

        if result[1] is None:
            print(
                f"Não foi possível encontrar um caminho de {origem} a {destino} com limite de {str(profundidade)}."
            )
            exit(0)

        print(
            f"Distância de {origem} a {destino} com limite de {str(profundidade)}: {fmt_distance(result[0])}"
        )
        print_caminho(result[1])
    elif option == 3:
        print("Algoritmo de procura Heurística - Sôfrega")

        origem = validar_distrito(input("Origem: "))
        destino = validar_distrito(input("Destino: "))

        result = sofrega(origem, destino)
        print(f"Distância de {origem} a {destino}: {fmt_distance(result[0])}")
        print_caminho(result[1])
    elif option == 4:
        print("Algoritmo de procura Heurística - A*")

        origem = validar_distrito(input("Origem: "))
        destino = validar_distrito(input("Destino: "))

        result = a_star(origem, destino)
        print(f"Distância de {origem} a {destino}: {fmt_distance(result[0])}")
        print_caminho(result[1])
    else:
        exit(0)


def clear_terminal():
    print("\033[H\033[J")


def print_caminho(caminho):
    print("Caminho: ", end="")
    for index, cidade in enumerate(caminho):
        if index == len(caminho) - 1:
            print(cidade)
        else:
            print(cidade, end=" -> ")


def fmt_distance(dist):
    return f"{dist:.2f} km"


def validar_distrito(county):
    if county not in distancias_entre_distritos:
        print(f"O distrito {county} não existe.")
        exit(0)

    return county


if __name__ == "__main__":
    main()
