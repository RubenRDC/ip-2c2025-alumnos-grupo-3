# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0


def step():
    # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.

    global items, n, i, j

    a=i     # índice del primer elemento a comparar
    b=j+1   # índice del segundo elemento a comparar
    

    # Si el elemento actual es mayor que el siguiente, hacemos el swap
    if(items[a]>items[b]):
        aux = items[a]
        items[a]=items[b]
        items[b]=aux
        return {"a": a, "b": b, "swap": True, "done": False}
    
    # Avanzamos los punteros para la siguiente comparación
    i=i+1
    j=j+1
    
    # Si llegamos al final del rango que todavía falta ordenar:
    if i+1==n:
        n=n-1 # reducimos n porque la burbuja más grande ya quedó al final
        i=0
        j=0

    # Si queda un solo elemento por ordenar, ya está todo ordenado. Asi que terminamos
    if n<=1:
        return {"done": True}

    return {"a": a, "b": b, "swap": False, "done": False}
