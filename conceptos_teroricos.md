# 📚 Conceptos Teóricos - Conjuntos en Python

## 🎯 Definición Matemática

Un **conjunto** es una colección de objetos distintos, considerados como un objeto en sí mismo. Los objetos se llaman **elementos** o **miembros** del conjunto.

### Notación Matemática
- $A = \{1, 2, 3, 4\}$ - Conjunto por extensión
- $B = \{x \mid x \text{ es un número par}\}$ - Conjunto por comprensión
- $x \in A$ - x pertenece a A
- $x \notin A$ - x no pertenece a A

## 🔧 Implementación en Python

### Características de los Conjuntos en Python
- **Elementos únicos**: No se permiten duplicados
- **No ordenados**: Los elementos no mantienen un orden específico
- **Mutables**: Se pueden agregar y eliminar elementos
- **Elementos hasheables**: Los elementos deben ser inmutables

### Creación de Conjuntos
```python
# Conjunto vacío
vacío = set()

# Conjunto con elementos
numeros = {1, 2, 3, 4, 5}

# Desde una lista (elimina duplicados)
lista = [1, 2, 2, 3, 4, 4, 4]
conjunto = set(lista)  # {1, 2, 3, 4}
