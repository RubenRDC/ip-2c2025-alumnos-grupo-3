
# TP — Visualización de algoritmos de ordenamiento
## Comisión 07 – Grupo 3:
 - Martín Oscar Basualdo
 - Aaron Joaquín Orbegozo
 - Rubén Ruiz Diaz Centurión
 - Federico Denuchi

## Objetivos

- Implementar **Bubble**, **Selection** e **Insertion** cumpliendo el **contrato**  `init(vals)` + `step()` que usa la UI.

- Ver el algoritmo **animado** y **paso a paso** (una operación por llamada a `step`).

- (Opcional) Agregar algoritmos extra y/o **métricas** (comparaciones, swaps, tiempo), y documentar un análisis breve.

  

---

  

## ¿Qué es un algoritmo de ordenamiento?

Un algoritmo de ordenamiento es un procedimiento que re-acomoda una colección según un criterio (números, palabras, objetos por propiedad, etc.).

Existen múltiples estrategias (Bubble, Selection, Insertion, Quick, Merge, Shell, Heap…), cada una con una idea distinta para comparar e intercambiar elementos.

  

---

  

## 📦 Estructura del repositorio

```

/visualizador/

index.html # visualizador web (provisto)

/algorithms/

sort_bubble.py

sort_selection.py

sort_insertion.py

sort_template.py # plantilla para nuevos algoritmos

```

podés agregar: sort_quick.py, sort_merge.py, sort_shell.py, ...

  

>  **Nota:** la extensión “imagen por columnas” ya está implementada.

> Tus algoritmos trabajan sobre una lista de enteros; la UI se encarga de mostrar y mover las columnas.

  

---

  

## ▶️ Cómo ejecutar el visualizador

1. En una terminal, ubicarse en la carpeta `/visualizador`

2. Ejecutar:

```bash

python -m http.server

```

3. Abrir [http://localhost:8000](http://localhost:8000) (recomendado en modo incógnito).

4. Elegir **dataset** y **algoritmo**.

5. Usar los botones: **Mezclar**, **Reproducir**, **Paso**, **Pausa**, **Reset**.

  

El selector de algoritmo carga automáticamente el archivo `algorithms/sort_<valor>.py`.

  

---

  

## 🔗 Contrato de los archivos `sort_<algo>.py`

  

Cada archivo debe exponer **dos funciones globales**:

  

```python

init(vals: list[int]) ->  None

step() ->  dict

```

  

### `init(vals)`

Se ejecuta una vez al comenzar (o tras mezclar).

Debe:

- Guardar copia: `items = list(vals)`

- Guardar `n = len(items)`

- Inicializar los punteros o estado interno (`i`, `j`, `min_idx`, pila, etc.)

  

### `step()`

Se llama muchas veces. Cada llamada realiza **un solo micro-paso** y devuelve un diccionario:

  

```python

{

"a": int, # índice A (0..n-1)

"b": int, # índice B (0..n-1)

"swap": bool, # True si hiciste items[a] <-> items[b]

"done": bool  # True si el algoritmo terminó

}

```

  

**Reglas:**

-  `0 <= a,b < n`

- Si `swap=True`, el intercambio ya debe haberse realizado:

```python

items[a], items[b] = items[b], items[a]

return {"a": a, "b": b, "swap": True, "done": False}

```

- Al finalizar: `return {"done": True}`

- Actualizá correctamente los punteros/estado en cada paso.

  

---

  

## Nuevos algoritmos

- Archivo: `algorithms/sort_<algo>.py`

- Agregar al `<select id="algorithm">` de `index.html` con `value="<algo>"`

- No hace falta modificar `index.html` para **Bubble**, **Selection** e **Insertion**

  

---

  

## Guía de implementación

  

### Bubble Sort

- Estado: `i`, `j`, `n`

- Comparar `items[j]` con `items[j+1]`, hacer swap si corresponde

- Cuando `j+1 == n-i-1`, reiniciar `j=0` y `i+=1`

  

### Selection Sort

- Estado: `i`, `j`, `min_idx`

- Buscar el mínimo en `i..n-1`, swap con `i` al final de la pasada

  

### Insertion Sort

- Estado: `i`, `j`

- Insertar el elemento `i` en la porción ordenada `0..i-1`, intercambiando adyacentes

  

---

  

## ✅ Entregables

-  **Obligatorio:**

- Carpeta `/algorithms/` con **al menos 3** algoritmos (`bubble`, `selection`, `insertion`)

-  **Informe** detallado con decisiones y dificultades

-  **README del equipo** con integrantes y notas de implementación

-  **Opcional:**

- Nuevos algoritmos (`quick`, `merge`, `shell`, etc.)

- Métricas, benchmarks o mejoras visuales

  

---

  

## 📝 Formato de entrega

  

La entrega se divide en **2 partes: código e informe.**

  

### Parte 1: Código

- Todo el desarrollo debe estar en un **repositorio interno del grupo** (fork del repo base del TP).

- Agregar a los **docentes de la comisión** para revisión y seguimiento.

- Los alumnos deben **notificar a los docentes** para pre-entregas o bloqueos.

  

**Sugerencias:**

- Cada integrante debe tener su **propia cuenta de GitHub**.

- Cada integrante debe **commitear su parte del código**, mostrando aportes individuales.

  

### Parte 2: Informe

Debe incluir:

- Una **introducción** general no técnica.

- El **código** de los algoritmos implementadas.

- Una **breve explicación** de cada algoritmo con dificultades y decisiones justificadas.

-  **No** incluir explicaciones de funcionalidades de Python u otros frameworks.

  

El informe debe estar en **PDF** dentro de la carpeta del TP.

  

> 🔥 **Ambas partes (código + informe) son obligatorias para aprobar.**

  

---

  

## 📚 Documentación adicional

- [Documentación oficial de Django](https://docs.djangoproject.com/en/4.2/)

-  **Sección GIT:**

- Introducción a GIT: [clic acá](https://www.youtube.com/watch?v=mzHWafbVRyU).

- Manejo de ramas/branches: [clic acá](https://www.youtube.com/watch?v=BRY9gamL9PE).

- Merge & resolución de conflictos: [clic acá](https://www.youtube.com/watch?v=9YUaf-uxuRM).

  

---

  

## ✅ Checklist antes de entregar

- [ ] Los 3 algoritmos base están implementados y finalizan correctamente

- [ ] `init` resetea el estado

- [ ] `step` realiza un micro-paso

- [ ] Swaps hechos antes de devolver `swap=True`

- [ ] Probado con listas vacías, cortas, ordenadas e inversas

- [ ] Informe y README listos

  

---

  

## Requisitos y entorno

- Python 3.10+

- Navegador moderno (Chrome, Firefox o Edge)