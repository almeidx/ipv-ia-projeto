distancias_faro = {
    "Aveiro": 366,
    "Beja": 99,
    "Braga": 454,
    "Bragança": 487,
    "Castelo Branco": 280,
    "Coimbra": 319,
    "Évora": 157,
    "Faro": 0,
    "Guarda": 352,
    "Leiria": 278,
    "Lisboa": 195,
    "Portalegre": 228,
    "Porto": 418,
    "Santarém": 231,
    "Setúbal": 168,
    "Viana do Castelo": 473,
    "Vila Real": 429,
    "Viseu": 363,
}

coordenadas_distritos = {
    "Aveiro": (40.6333, -8.65),
    "Beja": (38.0333, -7.8833),
    "Braga": (41.5503, -8.42),
    "Bragança": (41.8067, -6.7589),
    "Castelo Branco": (39.8167, -7.5),
    "Coimbra": (40.2028, -8.4139),
    "Faro": (37.0167, -7.9333),
    "Évora": (38.5667, -7.9),
    "Guarda": (40.5333, -7.3333),
    "Leiria": (39.75, -8.8),
    "Lisboa": (38.7253, -9.15),
    "Portalegre": (39.3167, -7.4167),
    "Porto": (41.1621, -8.622),
    "Santarém": (39.2339, -8.6861),
    "Setúbal": (38.5243, -8.8926),
    "Viana do Castelo": (41.7, -8.8333),
    "Vila Real": (41.2958, -7.7461),
    "Viseu": (40.6667, -7.9167),
}

distancias_cidades = {
    "Aveiro": {"Porto": 68, "Viseu": 95, "Coimbra": 68, "Leiria": 115},
    "Beja": {"Évora": 78, "Faro": 152, "Setúbal": 142},
    "Braga": {"Viana do Castelo": 48, "Vila Real": 106, "Porto": 53},
    "Bragança": {"Vila Real": 137, "Guarda": 202},
    "Castelo Branco": {"Coimbra": 159, "Guarda": 106, "Portalegre": 80, "Évora": 203},
    "Coimbra": {"Viseu": 96, "Leiria": 67},
    "Évora": {"Lisboa": 150, "Santarém": 117, "Portalegre": 131, "Setúbal": 103},
    "Faro": {"Setúbal": 249, "Lisboa": 299},
    "Guarda": {"Vila Real": 157, "Viseu": 85},
    "Leiria": {"Lisboa": 129, "Santarém": 70},
    "Lisboa": {"Santarém": 78, "Setúbal": 50},
    "Porto": {"Viana do Castelo": 71, "Vila Real": 116, "Viseu": 133},
    "Vila Real": {"Viseu": 110},
}


# Inverter as distâncias para serem bidirecionais
for cidade, distancias in list(distancias_cidades.items()):
    for inner_cidade, inner_distancia in list(distancias.items()):
        if inner_cidade not in distancias_cidades:
            distancias_cidades[inner_cidade] = {}

        distancias_cidades[inner_cidade][cidade] = inner_distancia
