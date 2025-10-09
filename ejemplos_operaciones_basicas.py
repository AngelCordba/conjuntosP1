"""
Ejemplos de Operaciones Básicas con Conjuntos en Python
Equipo Conjuntos - Universidad Autónoma de Zacatecas
"""

print("🐍 CONJUNTOS EN PYTHON - OPERACIONES BÁSICAS")
print("=" * 50)

# =============================================================================
# 1. CREACIÓN DE CONJUNTOS
# =============================================================================

print("\n1. 🆕 CREACIÓN DE CONJUNTOS")
print("-" * 30)

# Conjunto vacío
conjunto_vacio = set()
print(f"Conjunto vacío: {conjunto_vacio}")

# Conjunto con elementos
numeros = {1, 2, 3, 4, 5}
print(f"Conjunto de números: {numeros}")

# Conjunto a partir de una lista (elimina duplicados)
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_sin_duplicados = set(lista_con_duplicados)
print(f"Lista original: {lista_con_duplicados}")
print(f"Conjunto sin duplicados: {conjunto_sin_duplicados}")

# Conjunto con diferentes tipos de datos
mixto = {1, "python", 3.14, True, (1, 2)}
print(f"Conjunto mixto: {mixto}")

# =============================================================================
# 2. OPERACIONES BÁSICAS - AGREGAR Y ELIMINAR
# =============================================================================

print("\n2. 🔧 OPERACIONES BÁSICAS - AGREGAR Y ELIMINAR")
print("-" * 50)

# add() - Agregar elementos
conjunto = {1, 2, 3}
print(f"Conjunto inicial: {conjunto}")

conjunto.add(4)
print(f"Después de add(4): {conjunto}")

conjunto.add(2)  # No tiene efecto (ya existe)
print(f"Después de add(2) (duplicado): {conjunto}")

# remove() vs discard()
conjunto.remove(3)
print(f"Después de remove(3): {conjunto}")

conjunto.discard(1)
print(f"Después de discard(1): {conjunto}")

# discard() no genera error si el elemento no existe
conjunto.discard(100)
print(f"Después de discard(100) (elemento no existe): {conjunto}")

# remove() generaría error: conjunto.remove(100)  # KeyError

# pop() - elimina y retorna un elemento aleatorio
elemento = conjunto.pop()
print(f"Elemento removido con pop(): {elemento}")
print(f"Conjunto después de pop(): {conjunto}")

# clear() - vaciar el conjunto
conjunto.clear()
print(f"Después de clear(): {conjunto}")

# =============================================================================
# 3. OPERACIONES DE PERTENENCIA
# =============================================================================

print("\n3. 🔍 OPERACIONES DE PERTENENCIA")
print("-" * 30)

vocales = {'a', 'e', 'i', 'o', 'u'}

print(f"Conjunto de vocales: {vocales}")
print(f"'a' en vocales: {'a' in vocales}")
print(f"'z' en vocales: {'z' in vocales}")
print(f"'x' no en vocales: {'x' not in vocales}")

# =============================================================================
# 4. COPY() VS ASIGNACIÓN
# =============================================================================

print("\n4. 📋 COPY() VS ASIGNACIÓN DIRECTA")
print("-" * 40)

original = {1, 2, 3, 4, 5}
print(f"Conjunto original: {original}")

# Asignación directa (referencia)
referencia = original

# Copia real
copia = original.copy()

# Modificamos el original
original.add(6)

print(f"Original después de add(6): {original}")
print(f"Referencia (cambió): {referencia}")
print(f"Copia (no cambió): {copia}")

# =============================================================================
# 5. PROPIEDADES DE LOS CONJUNTOS
# =============================================================================

print("\n5. 📊 PROPIEDADES DE LOS CONJUNTOS")
print("-" * 35)

# No mantienen orden
conjunto_desordenado = {5, 2, 8, 1, 9}
print(f"Conjunto creado: {5, 2, 8, 1, 9}")
print(f"Al imprimir: {conjunto_desordenado}")

# No permiten duplicados
conjunto_duplicados = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Con elementos duplicados: {1, 2, 2, 3, 3, 3}")
print(f"Resultado final: {conjunto_duplicados}")

# Son iterables
print("Iterando sobre el conjunto:")
for elemento in numeros:
    print(f"  - {elemento}")

print("\n" + "=" * 50)
print("🎯 EJEMPLOS BÁSICOS COMPLETADOS EXITOSAMENTE")
