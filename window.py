import tkinter as tk
from tkinter import ttk
import tkintermapview as mv
from distances import distancias_entre_distritos, coordenadas_distritos
from algorithms.custo_uniforme import custo_uniforme
from algorithms.profundidade_limitada import profundidade_limitada
from algorithms.sofrega import sofrega
from algorithms.a_star import a_star


def run_algorithm(map_widget: mv.TkinterMapView):
    origem = origem_select.get()
    destino = destino_select.get()
    algoritmo = algoritmo_select.get()

    if origem == "" or destino == "" or algoritmo == "":
        return

    if algoritmo == "Custo Uniforme":
        result = custo_uniforme(origem, destino)
    elif algoritmo == "Profundidade Limitada":
        profundidade = profundidade_input.get() or "10"
        result = profundidade_limitada(origem, destino, int(profundidade))
    elif algoritmo == "Sôfrega":
        result = sofrega(origem, destino)
    elif algoritmo == "A*":
        result = a_star(origem, destino)

    print(result)

    result_label.config(text=f"Distância de {origem} a {destino}: {result[0]} km")

    map_widget.delete_all_marker()
    map_widget.delete_all_path()

    if result[1] is not None:
        caminho_str = " -> ".join(result[1])
        caminho_label.config(text=f"Caminho: {caminho_str}")

        first = result[1][0]
        last = result[1][-1]

        lat1, lon1 = coordenadas_distritos[first]
        lat2, lon2 = coordenadas_distritos[last]

        map_widget.set_marker(lat1, lon1, text=first)
        map_widget.set_marker(lat2, lon2, text=last)

        for i in range(len(result[1]) - 1):
            distrito1 = result[1][i]
            distrito2 = result[1][i + 1]

            lat1, lon1 = coordenadas_distritos[distrito1]
            lat2, lon2 = coordenadas_distritos[distrito2]

            map_widget.set_path([(lat1, lon1), (lat2, lon2)])
    else:
        caminho_label.config(text="Não foi possível encontrar um caminho.")


window = tk.Tk()
window.title("Calculadora de Distâncias")
window.geometry("800x700")

distritos = list(distancias_entre_distritos.keys())

ttk.Label(window, text="Escolha o distrito de origem:").pack(pady=2)
origem_select = ttk.Combobox(window, values=distritos)
origem_select.pack(pady=5)

ttk.Label(window, text="Escolha o distrito de destino:").pack(pady=2)
destino_select = ttk.Combobox(window, values=distritos)
destino_select.pack(pady=5)

ttk.Label(window, text="Escolha o algoritmo de procura:").pack(pady=2)
algoritmo_select = ttk.Combobox(
    window, values=["Custo Uniforme", "Profundidade Limitada", "Sôfrega", "A*"]
)
algoritmo_select.pack(pady=5)

profundidade_frame = tk.Frame(window, pady=2)
profundidade_frame.pack_forget()

ttk.Label(profundidade_frame, text="Profundidade Máxima:").pack(side=tk.LEFT)

profundidade_input = ttk.Entry(profundidade_frame)
profundidade_input.pack(side=tk.LEFT)

map_widget = mv.TkinterMapView(window, width=320, height=320, corner_radius=0)
map_widget.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

# map_widget.set_tile_server(
#     "https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga"
# )

map_widget.fit_bounding_box((42.2164901, -10.0195117), (36.9051659, -6.7675586))

submit = ttk.Button(window, text="Calcular", command=lambda: run_algorithm(map_widget))
submit.pack(pady=5)

result_label = ttk.Label(window, text="")
result_label.pack(pady=5)

caminho_label = ttk.Label(window, text="")
caminho_label.pack(pady=5)


def toggle_profundidade_frame(_):
    if algoritmo_select.get() == "Profundidade Limitada":
        profundidade_frame.pack()
    else:
        profundidade_frame.pack_forget()


algoritmo_select.bind("<<ComboboxSelected>>", toggle_profundidade_frame)

window.mainloop()
