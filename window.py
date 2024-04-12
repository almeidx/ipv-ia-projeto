import tkinter as tk
from tkinter import ttk
from distances import distancias_cidades
from algorithms.custo_uniforme import custo_uniforme
from algorithms.profundidade_limitada import profundidade_limitada
from algorithms.sofrega import sofrega
from algorithms.a_star import a_star


def run_algorithm():
    origem = origemSelectBox.get()
    destino = destinoSelectBox.get()
    algoritmo = algoritmoSelectBox.get()

    if algoritmo == "Custo Uniforme":
        result = custo_uniforme(origem, destino)
    elif algoritmo == "Profundidade Limitada":
        result = profundidade_limitada(origem, destino, 10)
    elif algoritmo == "Sôfrega":
        result = sofrega(origem, destino)
    elif algoritmo == "A*":
        result = a_star(origem, destino)

    print(result)

    resultLabel.config(text=f"Distância de {origem} a {destino}: {result[0]} km")

    if result[1] is not None:
        caminho_str = " -> ".join(result[1])
        caminhoLabel.config(text=f"Caminho: {caminho_str}")
    else:
        caminhoLabel.config(text="Não foi possível encontrar um caminho.")


window = tk.Tk()
window.title("Calculadora de Distâncias")
window.geometry("400x300")

distritos = list(distancias_cidades.keys())
distritos.sort()

ttk.Label(window, text="Escolha o distrito de origem:").pack(pady=2)
origemSelectBox = ttk.Combobox(window, values=distritos)
origemSelectBox.pack(pady=5)

ttk.Label(window, text="Escolha o distrito de destino:").pack(pady=2)
destinoSelectBox = ttk.Combobox(window, values=distritos)
destinoSelectBox.pack(pady=5)

ttk.Label(window, text="Escolha o algoritmo de procura:").pack(pady=2)
algoritmoSelectBox = ttk.Combobox(
    window, values=["Custo Uniforme", "Profundidade Limitada", "Sôfrega", "A*"]
)
algoritmoSelectBox.pack(pady=5)

submit = ttk.Button(window, text="Calcular", command=lambda: run_algorithm())
submit.pack(pady=5)

resultLabel = ttk.Label(window, text="")
resultLabel.pack(pady=5)

caminhoLabel = ttk.Label(window, text="")
caminhoLabel.pack(pady=5)

window.mainloop()
