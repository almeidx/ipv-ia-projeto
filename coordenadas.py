from math import sin, cos, sqrt, atan2, radians
from distances import distancias_faro, coordenadas_distritos


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
