from math import sin, cos, sqrt, atan2, radians
from distances import distancias_faro


def calcular_distancia_coordenadas(origem, destino):
    if destino == "Faro" or origem == "Faro":
        if destino == "Faro":
            return distancias_faro[origem]
        else:
            return distancias_faro[destino]

    lat1, lon1 = coordenadas_distritos[origem]
    lat2, lon2 = coordenadas_distritos[destino]

    # Raio médio da Terra em km
    raio_terra = 6371.0

    lat1_rad, lon1_rad, lat2_rad, lon2_rad = (
        radians(lat1),
        radians(lon1),
        radians(lat2),
        radians(lon2),
    )

    d_lon = lon2_rad - lon1_rad
    d_lat = lat2_rad - lat1_rad

    # Fórmula de Haversine
    a = sin(d_lat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = raio_terra * c

    return distancia


coordenadas_distritos = {
    "Aveiro": (40.6333, -8.65),
    "Beja": (38.0333, -7.8833),
    "Braga": (41.5503, -8.42),
    "Bragança": (41.8067, -6.7589),
    "Castelo Branco": (39.8167, -7.5),
    "Coimbra": (40.2028, -8.4139),
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
