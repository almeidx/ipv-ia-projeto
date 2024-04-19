import tkinter as tk
from tkinter import ttk
import tkintermapview as mv
from distances import distancias_cidades, coordenadas_distritos
from algorithms.custo_uniforme import custo_uniforme
from algorithms.profundidade_limitada import profundidade_limitada
from algorithms.sofrega import sofrega
from algorithms.a_star import a_star


def run_algorithm(map_widget: mv.TkinterMapView):
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

    map_widget.delete_all_marker()
    map_widget.delete_all_path()

    if result[1] is not None:
        caminho_str = " -> ".join(result[1])
        caminhoLabel.config(text=f"Caminho: {caminho_str}")

        first = result[1][0]
        last = result[1][-1]

        lat1, lon1 = coordenadas_distritos[first]
        lat2, lon2 = coordenadas_distritos[last]

        map_widget.set_marker(lat1, lon1, text=first)
        map_widget.set_marker(lat2, lon2, text=last)

        # path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.57, 13.4), (52.55, 13.35)])

        for i in range(len(result[1]) - 1):
            distrito1 = result[1][i]
            distrito2 = result[1][i + 1]

            lat1, lon1 = coordenadas_distritos[distrito1]
            lat2, lon2 = coordenadas_distritos[distrito2]

            map_widget.set_path([(lat1, lon1), (lat2, lon2)])
    else:
        caminhoLabel.config(text="Não foi possível encontrar um caminho.")


window = tk.Tk()
window.title("Calculadora de Distâncias")
window.geometry("800x600")

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

map_widget = mv.TkinterMapView(window, width=320, height=320, corner_radius=0)
map_widget.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

map_widget.set_position(40.2028, -8.4139)
map_widget.set_zoom(6.5)

submit = ttk.Button(window, text="Calcular", command=lambda: run_algorithm(map_widget))
submit.pack(pady=5)

resultLabel = ttk.Label(window, text="")
resultLabel.pack(pady=5)

caminhoLabel = ttk.Label(window, text="")
caminhoLabel.pack(pady=5)

window.mainloop()
