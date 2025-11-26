# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"
valoresIniciales = []

def startValues():
    global items, n, i, j, min_idx, fase, valoresIniciales
    items = list(valoresIniciales)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def init(vals):
    global valoresIniciales
    valoresIniciales = vals
    startValues()

def step():
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".

    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.

    global items, n, i, j, min_idx, fase

    # Si i+1 es igual a la lista, ya está todo ordenado
    if(i+1==n):
        return {"done":True}
    
    # ------------------ FASE "BUSCAR" ------------------
    if(fase == "buscar"):

        # Si encontramos un valor más chico, actualizamos min_idx
        if(items[j]<items[min_idx]):

            min_idx = j
            return {"a": min_idx, "b": j, "swap": False, "done": False}

        # Si no es menor, solo avanzamos j
        j=j+1

        # Si j llegó al final, pasamos a fase "swap"
        if(j>=n):
            fase="swap"
        return {"a": min_idx, "b": j, "swap": False, "done":False}
    
    # ------------------ FASE "SWAP" ------------------
    if(fase=="swap"):

        minAux = min_idx # guardamos el índice del mínimo encontrado
        iAux = i # guardamos la posición donde debe colocarse

        # Si el mínimo encontrado NO está en la posición correcta, hacemos el intercambio
        if(items[minAux]!=items[iAux]):
            itemsAux = items[i]         # guardamos temporalmente items[i]
            items[min_idx] = items[i]   # movemos el valor actual a la posición del mínimo
            items[i] = itemsAux         # colocamos el mínimo en su lugar
            min_idx = i                 # el mínimo ahora quedó en la posición i
            return {"a": iAux, "b": minAux, "swap": True, "done": False}
        
        # Si no hubo swap (el mínimo ya estaba donde debía):
        i = i+1         # avanzamos a la siguiente posición a ordenar
        j = i+1         # el nuevo recorrido empieza desde i+1
        min_idx = i     # asumimos que el nuevo mínimo arranca en i
        fase = "buscar" # volvemos a buscar
        return {"done":False}




