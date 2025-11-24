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
    global items, n, i, j # TODO:
    a=j
    b=j+1
    done=False
    if items[a]>items[b]:
        aux=items[a]
        items[a]=items[b]
        items[b]=aux
        swap=True
    else:
        swap=False
    i=i+1
    j=j+1
    if i+1==n:
        n=n-1
        i=0
        j=0
    if n==1:

        done=True      
    return {"a": a,"b": b,"swap": swap, "done": done}   
