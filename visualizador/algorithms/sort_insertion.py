# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    # TODO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.

    global items, n, i, j

    # Si ya procesamos todos los elementos, el algoritmo termina
    if i >= n:
        return {"done": True}
    if j == None:
        j = i

    # Mientras estemos dentro de la lista y el elemento anterior sea mayor,
    # hacemos un único swap y lo reportamos
    while j > 0 and items[j-1] > items[j]:
        aux = items[j-1]
        items[j-1] = items[j]
        items[j] = aux
        
        j=j-1 # seguimos desplazándonos hacia la izquierda

        # devolvemos qué posiciones se swapearon
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # Si ya no hay desplazamientos para hacer, avanzamos al siguiente elemento
    i=i+1
    j=None    

    # Aún no se termino, pero no hubo swap en este paso
    return {"done": False}
