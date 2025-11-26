# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
valoresIniciales = []
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def startValues():
    global items, n, valoresIniciales
    items = list(valoresIniciales)
    n = len(items)

def init(vals):
    global valoresIniciales
    valoresIniciales = vals
    startValues()
    # TODO: inicializar punteros/estado

def step():
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    return {"done": True}

