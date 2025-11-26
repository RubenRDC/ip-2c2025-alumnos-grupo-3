# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

valores = []        # array real de números que llega desde la UI
cantidad = 0        # cantidad de elementos

# pila de trabajo: (izq, der, fase) con fase en {"dividir", "mezclar"}
pila = []

# estado de mezcla in-place
en_mezcla = False
izq = der = medio = 0
puntero_izq = puntero_der = 0

# estado de rotación (para mover elementos del subarray derecho al izquierdo)
rotando = False
indice_rotacion = 0   # índice actual del swap adyacente que se está ejecutando


def init(vals):
    global valores, cantidad, pila, en_mezcla
    global izq, der, medio, puntero_izq, puntero_der, rotando, indice_rotacion

    valores = list(vals)
    cantidad = len(valores)

    pila = []
    if cantidad > 1:
        pila.append((0, cantidad - 1, "dividir"))

    en_mezcla = False
    izq = der = medio = 0
    puntero_izq = puntero_der = 0
    rotando = False
    indice_rotacion = 0


def step():
    """
    Realiza UN solo micro-paso del MergeSort in-place:
    - swap=True → realizó un intercambio entre dos índices
    - swap=False → solo comparó / avanzó punteros
    - done=True → algoritmo completado
    """
    global valores, cantidad, pila, en_mezcla
    global izq, der, medio, puntero_izq, puntero_der, rotando, indice_rotacion

    # No queda trabajo → terminado
    if not pila and not en_mezcla and not rotando:
        return {"a": 0, "b": 0, "swap": False, "done": True}

    ###############################################################
    # 1) FASE DE ROTACIÓN (mover valor del subarray derecho al izquierdo)
    ###############################################################
    if rotando:
        # swap adyacente entre indice_rotacion y indice_rotacion - 1
        a = indice_rotacion - 1
        b = indice_rotacion

        # intercambio real en la lista
        valores[a], valores[b] = valores[b], valores[a]
        indice_rotacion -= 1

        # si ya movimos el elemento hasta puntero_izq → terminar rotación
        if indice_rotacion == puntero_izq:
            rotando = False
            # avanzar puntero izquierdo y actualizar topes del merge
            puntero_izq += 1
            medio += 1
            puntero_der += 1

        return {"a": a, "b": b, "swap": True, "done": False}

    ###############################################################
    # 2) FASE DE MEZCLA (merge in-place)
    ###############################################################
    if en_mezcla:

        # Si alguno de los dos subarrays se agotó → terminar mezcla
        if puntero_izq > medio or puntero_der > der:
            en_mezcla = False
            return {"a": izq, "b": der, "swap": False, "done": False}

        # Si el valor del subarray izquierdo es menor → avanzar puntero izquierdo
        if valores[puntero_izq] <= valores[puntero_der]:
            a = puntero_izq
            b = puntero_der
            puntero_izq += 1
            # solo highlight
            return {"a": a, "b": b, "swap": False, "done": False}

        else:
            # El elemento del subarray derecho debe insertarse en la izquierda
            índice_a_mover = puntero_der
            indice_rotacion = índice_a_mover  # comenzamos la rotación
            rotando = True

            # esto solo marca visualmente, el swap real se hace en el próximo paso
            return {"a": puntero_izq, "b": puntero_der, "swap": False, "done": False}

    ###############################################################
    # 3) FASE DE DIVISIÓN Y PREPARACIÓN DE LA MEZCLA
    ###############################################################
    if pila:
        izq, der, fase = pila.pop()

        # Intervalo trivial
        if izq >= der:
            return {"a": izq, "b": der, "swap": False, "done": False}

        if fase == "dividir":
            medio = (izq + der) // 2

            # agregar tareas en orden LIFO
            pila.append((izq, der, "mezclar"))
            pila.append((medio + 1, der, "dividir"))
            pila.append((izq, medio, "dividir"))

            return {"a": izq, "b": der, "swap": False, "done": False}

        if fase == "mezclar":
            medio = (izq + der) // 2

            # inicializar punteros para mezcla
            puntero_izq = izq
            puntero_der = medio + 1
            en_mezcla = True

            return {"a": izq, "b": der, "swap": False, "done": False}

    ###############################################################
    # Caso de seguridad
    ###############################################################
    return {"a": 0, "b": 0, "swap": False, "done": True}