# sort_quick.py — QuickSort paso a paso (Lomuto), compatible con el visualizador
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

###############################################################
# QuickSort paso a paso (Lomuto)
# Compatible con el visualizador (usa sólo swaps)
# Variables en español + comentarios detallados
###############################################################

# Lista real de números (enteros) que llega desde JS
valores = []
cantidad = 0

# Pila con intervalos (izq, der) pendientes de ordenar
pila = []

# Estado del particionado actual
en_particion = False            # ¿estamos particionando un intervalo?
izq = der = 0                   # límites del intervalo actual
indice_pivote = 0               # índice donde está el pivote
valor_pivote = None             # valor del pivote (para comparar)
pos_menores = 0                 # puntero 'i' del esquema de Lomuto
explorador = 0                  # puntero 'j' del esquema de Lomuto
valoresIniciales = []

###############################################################
# init(vals): inicializa todos los estados antes de ordenar
###############################################################

def startValues():
    global valores, cantidad, pila, valoresIniciales
    global en_particion, izq, der, indice_pivote, valor_pivote
    global pos_menores, explorador

    # Copiamos los valores desde la UI
    valores = list(valoresIniciales)
    cantidad = len(valores)

    # Si hay más de 1 elemento, agregamos el intervalo total
    pila = []
    if cantidad > 1:
        pila.append((0, cantidad - 1))

    # Reset del estado de partición
    en_particion = False
    izq = der = indice_pivote = pos_menores = explorador = 0
    valor_pivote = None

def init(vals):
    global valoresIniciales
    valoresIniciales = vals
    startValues()

###############################################################
# step(): ejecuta un micro-paso del algoritmo
###############################################################
def step():
    global valores, pila, cantidad
    global en_particion, izq, der, indice_pivote, valor_pivote
    global pos_menores, explorador

    ###########################################################
    # 1) Caso base: nada por hacer → terminado
    ###########################################################
    if not pila and not en_particion:
        return {"a": 0, "b": 0, "swap": False, "done": True}

    ###########################################################
    # 2) Si estamos particionando un intervalo (Lomuto)
    ###########################################################
    if en_particion:

        #######################################################
        # FASE 1: recorrer con 'explorador' desde izq hasta der-1
        #######################################################
        if explorador < der:

            # Mostrar comparación entre explorador y pivote
            a = explorador
            b = indice_pivote

            # Caso: valor menor que el pivote → hacer swap(i, j)
            if valores[explorador] < valor_pivote:

                # Intercambiar valores[pos_menores] ↔ valores[explorador]
                valores[pos_menores], valores[explorador] = (
                    valores[explorador],
                    valores[pos_menores],
                )

                # Guardamos índices intercambiados para la UI
                intercambiado_a = pos_menores
                intercambiado_b = explorador

                # Avanzar frontera de elementos menores
                pos_menores += 1

                # Avanzar explorador
                explorador += 1

                # Devolver operación de swap
                return {"a": intercambiado_a, "b": intercambiado_b, "swap": True, "done": False}

            else:
                # Caso: valor >= pivote → solo highlight
                explorador += 1
                return {"a": a, "b": b, "swap": False, "done": False}

        ###########################################################
        # FASE 2: colocar el pivote en su posición final
        ###########################################################
        if indice_pivote != pos_menores:

            # Swap pivote ↔ valor en pos_menores
            valores[pos_menores], valores[indice_pivote] = (
                valores[indice_pivote],
                valores[pos_menores],
            )

            intercambiado_a = pos_menores
            intercambiado_b = indice_pivote

            # El pivote termina aquí
            posicion_pivote_final = pos_menores

            # Termina la partición
            en_particion = False

            # Agregar intervalos derecho e izquierdo (LIFO)
            if posicion_pivote_final + 1 < der:
                pila.append((posicion_pivote_final + 1, der))

            if izq < posicion_pivote_final - 1:
                pila.append((izq, posicion_pivote_final - 1))

            return {"a": intercambiado_a, "b": intercambiado_b, "swap": True, "done": False}

        else:
            # El pivote ya estaba donde corresponde
            posicion_pivote_final = pos_menores
            en_particion = False

            # Agregar subintervalos
            if posicion_pivote_final + 1 < der:
                pila.append((posicion_pivote_final + 1, der))

            if izq < posicion_pivote_final - 1:
                pila.append((izq, posicion_pivote_final - 1))

            # Highlight final del intervalo
            return {"a": izq, "b": der, "swap": False, "done": False}

    ###########################################################
    # 3) Si no estamos particionando → empezar una nueva partición
    ###########################################################
    if pila:
        izq, der = pila.pop()

        # Intervalo trivial
        if izq >= der:
            return {"a": izq, "b": der, "swap": False, "done": False}

        # Elegimos pivote como el último elemento
        indice_pivote = der
        valor_pivote = valores[indice_pivote]

        # Inicializamos punteros Lomuto
        pos_menores = izq
        explorador = izq

        # Activamos la partición
        en_particion = True

        return {"a": izq, "b": der, "swap": False, "done": False}

    ###########################################################
    # Esto casi nunca se ejecuta
    ###########################################################
    return {"a": 0, "b": 0, "swap": False, "done": True}
