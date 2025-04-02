def calculo(tiempo):
    match tiempo:
        case t if t < 200:
            return "Rapido"
        case t if 200 <= t <= 500:
            return "Normal"
        case _:
            return "Lento"

def sonAnagramas(p, p2):
    return sorted(p.lower()) == sorted(p2.lower())

def obtenerpuntos(ranking):
    return ranking[1]["puntos"]

def OrdenarRondaDescendente(ranking):
    return dict(sorted(ranking.items(), key=obtenerpuntos, reverse=True))

def calcularMaxpuntos(ranking):
    return max(ranking, key=lambda jugador: ranking[jugador]["puntos"])

def cargarRanking(rondas, ranking):
    for i, ronda in enumerate(rondas):
        for jugador, datos in ronda.items():
            ranking[jugador]["kills"] += datos["kills"]
            ranking[jugador]["assists"] += datos["assists"]
            ranking[jugador]["deaths"] += datos["deaths"]
            ranking[jugador]["puntos"] += (datos["kills"] * 3) + (datos["assists"] * 1) + (int(datos["deaths"] * -1))
        
        mvp_ronda = calcularMaxpuntos(ranking)
        ranking[mvp_ronda]["mvps"] += 1
        ranking = OrdenarRondaDescendente(ranking)
        print(f"Ronda {i+1} : {ranking} \n")
    
    return ranking