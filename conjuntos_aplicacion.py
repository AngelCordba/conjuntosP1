import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import numpy as np

class MenuConjuntos:
    def __init__(self):
        self.conjunto1 = {1, 2, 3, 4, 5}
        self.conjunto2 = {3, 4, 5, 6, 7}
        self.conjunto3 = {5, 6, 7, 8, 9}
        self.conjuntos_personalizados = {}
    
    def mostrar_conjuntos(self):
        print(f"\nConjunto 1: {self.conjunto1}")
        print(f"Conjunto 2: {self.conjunto2}")
        print(f"Conjunto 3: {self.conjunto3}")
        if self.conjuntos_personalizados:
            print("\nConjuntos Personalizados:")
            for nombre, conjunto in self.conjuntos_personalizados.items():
                print(f"  {nombre}: {conjunto}")
    
    def seleccionar_conjunto(self, incluir_personalizados=False):
        while True:
            print("\nSeleccione un conjunto:")
            print("1. Conjunto 1")
            print("2. Conjunto 2")
            print("3. Conjunto 3")
            
            if incluir_personalizados and self.conjuntos_personalizados:
                print("Conjuntos personalizados:")
                for i, (nombre, _) in enumerate(self.conjuntos_personalizados.items(), 4):
                    print(f"{i}. {nombre}")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                return self.conjunto1
            elif opcion == '2':
                return self.conjunto2
            elif opcion == '3':
                return self.conjunto3
            elif incluir_personalizados and self.conjuntos_personalizados:
                try:
                    idx = int(opcion) - 4
                    if 0 <= idx < len(self.conjuntos_personalizados):
                        nombres = list(self.conjuntos_personalizados.keys())
                        return self.conjuntos_personalizados[nombres[idx]]
                except (ValueError, IndexError):
                    pass
            
            print("Opción inválida. Intente nuevamente.")
    
    def crear_conjunto_personalizado(self):
        print("\n--- CREAR CONJUNTO PERSONALIZADO ---")
        nombre = input("Ingrese el nombre del nuevo conjunto: ")
        
        if nombre in self.conjuntos_personalizados:
            print("¡Ya existe un conjunto con ese nombre!")
            return
        
        print("Ingrese los elementos separados por comas.")
        print("Puede ingresar cualquier tipo de dato: números, texto, etc.")
        print("Ejemplo: 1, hola, True, 3.14, mundo")
        
        elementos = input("Elementos: ")
        elementos_lista = [self._convertir_elemento(x.strip()) for x in elementos.split(',')]
        
        nuevo_conjunto = set()
        for elemento in elementos_lista:
            if elemento != "":
                nuevo_conjunto.add(elemento)
        
        self.conjuntos_personalizados[nombre] = nuevo_conjunto
        print(f"Conjunto '{nombre}' creado: {nuevo_conjunto}")
    
    def _convertir_elemento(self, elemento):
        """Convierte el elemento al tipo de dato apropiado"""
        if elemento == "":
            return elemento
        
        # Intentar convertir a entero
        try:
            return int(elemento)
        except ValueError:
            pass
        
        # Intentar convertir a float
        try:
            return float(elemento)
        except ValueError:
            pass
        
        # Intentar convertir a booleano
        if elemento.lower() == 'true':
            return True
        elif elemento.lower() == 'false':
            return False
        
        # Devolver como string
        return elemento
    
    def modificar_conjunto_personalizado(self):
        if not self.conjuntos_personalizados:
            print("No hay conjuntos personalizados para modificar")
            return
        
        print("\nConjuntos personalizados disponibles:")
        for i, nombre in enumerate(self.conjuntos_personalizados.keys(), 1):
            print(f"{i}. {nombre}")
        
        try:
            opcion = int(input("Seleccione el conjunto a modificar: ")) - 1
            nombres = list(self.conjuntos_personalizados.keys())
            if 0 <= opcion < len(nombres):
                nombre = nombres[opcion]
                self.operaciones_conjunto_personalizado(nombre)
            else:
                print("Opción inválida")
        except ValueError:
            print("Ingrese un número válido")
    
    def operaciones_conjunto_personalizado(self, nombre_conjunto):
        conjunto = self.conjuntos_personalizados[nombre_conjunto]
        
        while True:
            print(f"\n--- OPERACIONES SOBRE CONJUNTO '{nombre_conjunto}' ---")
            print(f"Conjunto actual: {conjunto}")
            print("1. Agregar elemento")
            print("2. Remover elemento")
            print("3. Limpiar conjunto")
            print("4. Realizar operación con otro conjunto")
            print("5. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                elemento = input("Elemento a agregar: ")
                elemento_convertido = self._convertir_elemento(elemento)
                conjunto.add(elemento_convertido)
                print(f"Elemento '{elemento_convertido}' agregado")
            
            elif opcion == '2':
                elemento = input("Elemento a remover: ")
                elemento_convertido = self._convertir_elemento(elemento)
                if elemento_convertido in conjunto:
                    conjunto.remove(elemento_convertido)
                    print(f"Elemento '{elemento_convertido}' removido")
                else:
                    print("El elemento no existe en el conjunto")
            
            elif opcion == '3':
                conjunto.clear()
                print("Conjunto limpiado")
            
            elif opcion == '4':
                self.operaciones_entre_conjuntos(conjunto, nombre_conjunto)
            
            elif opcion == '5':
                break
            
            else:
                print("Opción inválida")
    
    def operaciones_entre_conjuntos(self, conjunto_base, nombre_base):
        print(f"\nOperaciones entre '{nombre_base}' y otro conjunto:")
        otro_conjunto = self.seleccionar_conjunto(True)
        
        print(f"\nConjunto base: {conjunto_base}")
        print(f"Otro conjunto: {otro_conjunto}")
        
        print("\nOperaciones disponibles:")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Diferencia simétrica")
        print("5. Verificar subconjunto")
        print("6. Verificar superconjunto")
        
        opcion = input("Seleccione una operación: ")
        
        if opcion == '1':
            resultado = conjunto_base.union(otro_conjunto)
            print(f"Unión: {resultado}")
        elif opcion == '2':
            resultado = conjunto_base.intersection(otro_conjunto)
            print(f"Intersección: {resultado}")
        elif opcion == '3':
            resultado = conjunto_base.difference(otro_conjunto)
            print(f"Diferencia: {resultado}")
        elif opcion == '4':
            resultado = conjunto_base.symmetric_difference(otro_conjunto)
            print(f"Diferencia simétrica: {resultado}")
        elif opcion == '5':
            resultado = conjunto_base.issubset(otro_conjunto)
            print(f"¿Es subconjunto? {resultado}")
        elif opcion == '6':
            resultado = conjunto_base.issuperset(otro_conjunto)
            print(f"¿Es superconjunto? {resultado}")
        else:
            print("Opción inválida")

    # OPERACIONES BÁSICAS
    def add(self):
        print("\n--- OPERACIÓN ADD ---")
        conjunto = self.seleccionar_conjunto(True)
        elemento = input("Ingrese el elemento a agregar: ")
        elemento_convertido = self._convertir_elemento(elemento)
        conjunto.add(elemento_convertido)
        print(f"Elemento '{elemento_convertido}' agregado exitosamente")
    
    def clear(self):
        print("\n--- OPERACIÓN CLEAR ---")
        conjunto = self.seleccionar_conjunto(True)
        conjunto.clear()
        print("Conjunto limpiado exitosamente")
    
    def copy(self):
        print("\n--- OPERACIÓN COPY ---")
        conjunto = self.seleccionar_conjunto(True)
        copia = conjunto.copy()
        print(f"Copia del conjunto: {copia}")
        return copia
    
    def diferente(self):
        print("\n--- OPERACIÓN DIFERENCIA ---")
        print("Seleccione el conjunto base:")
        conjunto_a = self.seleccionar_conjunto(True)
        print("Seleccione el conjunto a restar:")
        conjunto_b = self.seleccionar_conjunto(True)
        diferencia = conjunto_a.difference(conjunto_b)
        print(f"Diferencia: {diferencia}")
        return diferencia
    
    def discard(self):
        print("\n--- OPERACIÓN DISCARD ---")
        conjunto = self.seleccionar_conjunto(True)
        elemento = input("Ingrese el elemento a descartar: ")
        elemento_convertido = self._convertir_elemento(elemento)
        conjunto.discard(elemento_convertido)
        print(f"Elemento '{elemento_convertido}' descartado (si existía)")
    
    def interseccion(self):
        print("\n--- OPERACIÓN INTERSECCIÓN ---")
        print("Seleccione el primer conjunto:")
        conjunto_a = self.seleccionar_conjunto(True)
        print("Seleccione el segundo conjunto:")
        conjunto_b = self.seleccionar_conjunto(True)
        interseccion = conjunto_a.intersection(conjunto_b)
        print(f"Intersección: {interseccion}")
        return interseccion
    
    def isdisjoint(self):
        print("\n--- OPERACIÓN ISDISJOINT ---")
        print("Seleccione el primer conjunto:")
        conjunto_a = self.seleccionar_conjunto(True)
        print("Seleccione el segundo conjunto:")
        conjunto_b = self.seleccionar_conjunto(True)
        resultado = conjunto_a.isdisjoint(conjunto_b)
        print(f"¿Son disjuntos? {resultado}")
        return resultado
    
    def issubset(self):
        print("\n--- OPERACIÓN ISSUBSET ---")
        print("Seleccione el subconjunto:")
        subconjunto = self.seleccionar_conjunto(True)
        print("Seleccione el conjunto principal:")
        conjunto_principal = self.seleccionar_conjunto(True)
        resultado = subconjunto.issubset(conjunto_principal)
        print(f"¿Es subconjunto? {resultado}")
        return resultado
    
    def issuperset(self):
        print("\n--- OPERACIÓN ISSUPERSET ---")
        print("Seleccione el superconjunto:")
        superconjunto = self.seleccionar_conjunto(True)
        print("Seleccione el subconjunto:")
        subconjunto = self.seleccionar_conjunto(True)
        resultado = superconjunto.issuperset(subconjunto)
        print(f"¿Es superconjunto? {resultado}")
        return resultado
    
    def pop(self):
        print("\n--- OPERACIÓN POP ---")
        conjunto = self.seleccionar_conjunto(True)
        if conjunto:
            elemento = conjunto.pop()
            print(f"Elemento removido: {elemento}")
        else:
            print("El conjunto está vacío")
    
    def remove(self):
        print("\n--- OPERACIÓN REMOVE ---")
        conjunto = self.seleccionar_conjunto(True)
        elemento = input("Ingrese el elemento a remover: ")
        elemento_convertido = self._convertir_elemento(elemento)
        
        # EJEMPLO DE IF
        if elemento_convertido in conjunto:
            conjunto.remove(elemento_convertido)
            print(f"Elemento '{elemento_convertido}' removido exitosamente")
        else:
            print(f"El elemento '{elemento_convertido}' no existe en el conjunto")
    
    def union(self):
        print("\n--- OPERACIÓN UNION ---")
        print("Seleccione el primer conjunto:")
        conjunto_a = self.seleccionar_conjunto(True)
        print("Seleccione el segundo conjunto:")
        conjunto_b = self.seleccionar_conjunto(True)
        union = conjunto_a.union(conjunto_b)
        print(f"Unión: {union}")
        return union
    
    def update(self):
        print("\n--- OPERACIÓN UPDATE ---")
        conjunto = self.seleccionar_conjunto(True)
        print("Seleccione el conjunto con el que actualizar:")
        conjunto_actualizacion = self.seleccionar_conjunto(True)
        conjunto.update(conjunto_actualizacion)
        print("Conjunto actualizado exitosamente")

    # SUBSECCIONES DE ESTRUCTURAS DE CONTROL
    def ejemplo_while(self):
        print("\n" + "="*50)
        print("EJEMPLO WHILE - Vaciar conjunto con pop()")
        print("="*50)
        
        conjunto_ejemplo = self.conjunto1.copy()
        print(f"Conjunto original: {conjunto_ejemplo}")
        print("Removiendo elementos con pop() hasta vaciar:")
        
        contador = 1
        while conjunto_ejemplo:
            elemento = conjunto_ejemplo.pop()
            print(f"Paso {contador}: Elemento removido: {elemento}, Restante: {conjunto_ejemplo}")
            contador += 1
        
        print("\n¡Conjunto completamente vaciado!")
        print(f"Conjunto final: {conjunto_ejemplo}")
    
    def ejemplo_for(self):
        print("\n" + "="*50)
        print("EJEMPLO FOR - Recorrer y analizar conjuntos")
        print("="*50)
        
        todos_conjuntos = {
            "Conjunto 1": self.conjunto1,
            "Conjunto 2": self.conjunto2, 
            "Conjunto 3": self.conjunto3,
            **self.conjuntos_personalizados
        }
        
        print("Recorriendo todos los conjuntos:")
        for nombre, conjunto in todos_conjuntos.items():
            print(f"\n{nombre}: {conjunto}")
            
            if conjunto:
                try:
                    elementos_ordenados = sorted(conjunto)
                    print(f"  Elementos ordenados: {elementos_ordenados}")
                except TypeError:
                    print("  (No se pueden ordenar - tipos de datos mixtos)")
                
                print(f"  Cantidad de elementos: {len(conjunto)}")
                
                # Solo calcular max y min si todos los elementos son comparables
                try:
                    if conjunto:
                        print(f"  Elemento mayor: {max(conjunto)}")
                        print(f"  Elemento menor: {min(conjunto)}")
                except TypeError:
                    print("  (No se pueden calcular max/min - tipos no comparables)")
            else:
                print("  (Conjunto vacío)")
    
    def ejemplo_if(self):
        print("\n" + "="*50)
        print("EJEMPLO IF - Análisis de relaciones entre conjuntos")
        print("="*50)
        
        # Crear algunos conjuntos de ejemplo para las pruebas
        A = {1, 2, 3, 4, 5}
        B = {3, 4, 5, 6, 7}
        C = {5, 6, 7, 8, 9}
        D = {1, 2}
        
        print("Conjuntos de ejemplo:")
        print(f"A = {A}")
        print(f"B = {B}") 
        print(f"C = {C}")
        print(f"D = {D}")
        
        print("\nAnálisis con estructuras IF:")
        
        # Verificar intersecciones
        if A & B:
            print("✓ A y B tienen elementos en común")
            elementos_comunes = A & B
            print(f"  Elementos comunes: {elementos_comunes}")
        else:
            print("✗ A y B no tienen elementos en común")
        
        # Verificar subconjuntos
        if D.issubset(A):
            print("✓ D es subconjunto de A")
        else:
            print("✗ D no es subconjunto de A")
        
        # Verificar disjuntos
        if A.isdisjoint(C):
            print("✗ A y C son disjuntos (no comparten elementos)")
        else:
            print("✓ A y C comparten algunos elementos")
            print(f"  Elementos compartidos: {A & C}")
        
        # Análisis múltiple con elif
        relacion_AB = ""
        if A == B:
            relacion_AB = "iguales"
        elif A.issubset(B):
            relacion_AB = "A es subconjunto de B"
        elif B.issubset(A):
            relacion_AB = "B es subconjunto de A"
        elif A & B:
            relacion_AB = "parcialmente superpuestos"
        else:
            relacion_AB = "completamente diferentes"
        
        print(f"\nRelación entre A y B: {relacion_AB}")
    
    def mostrar_diagrama_venn(self):
        print("\n" + "="*50)
        print("DIAGRAMAS DE VENN CON MATPLOTLIB")
        print("="*50)
        
        print("Seleccione 2 o 3 conjuntos para el diagrama:")
        conjuntos_seleccionados = []
        nombres_seleccionados = []
        
        # Mostrar todos los conjuntos disponibles
        todos_conjuntos = {
            "Conjunto 1": self.conjunto1,
            "Conjunto 2": self.conjunto2,
            "Conjunto 3": self.conjunto3,
            **self.conjuntos_personalizados
        }
        
        print("\nConjuntos disponibles:")
        for i, (nombre, conjunto) in enumerate(todos_conjuntos.items(), 1):
            print(f"{i}. {nombre}: {conjunto}")
        
        try:
            num_conjuntos = int(input("\n¿Cuántos conjuntos desea usar? (2 o 3): "))
            if num_conjuntos not in [2, 3]:
                print("Solo se permiten 2 o 3 conjuntos")
                return
        except ValueError:
            print("Ingrese un número válido")
            return
        
        for i in range(num_conjuntos):
            try:
                opcion = int(input(f"Seleccione el conjunto {i+1}: "))
                nombres = list(todos_conjuntos.keys())
                if 1 <= opcion <= len(nombres):
                    nombre = nombres[opcion-1]
                    conjuntos_seleccionados.append(todos_conjuntos[nombre])
                    nombres_seleccionados.append(nombre)
                else:
                    print("Opción inválida")
                    return
            except ValueError:
                print("Ingrese un número válido")
                return
        
        self._generar_diagrama_venn_matplotlib(conjuntos_seleccionados, nombres_seleccionados)
    
    def _generar_diagrama_venn_matplotlib(self, conjuntos, nombres):
        """Genera diagramas de Venn usando matplotlib-venn"""
        try:
            plt.figure(figsize=(10, 8))
            
            if len(conjuntos) == 2:
                # Diagrama para 2 conjuntos
                venn_diagram = venn2([conjuntos[0], conjuntos[1]], set_labels=nombres)
                
                # Personalizar colores
                venn_diagram.get_patch_by_id('10').set_facecolor('lightblue')
                venn_diagram.get_patch_by_id('01').set_facecolor('lightgreen')
                venn_diagram.get_patch_by_id('11').set_facecolor('lightyellow')
                
                # Añadir título
                plt.title(f"Diagrama de Venn: {nombres[0]} vs {nombres[1]}", fontsize=14, fontweight='bold')
                
                # Mostrar información detallada
                solo_A = conjuntos[0] - conjuntos[1]
                solo_B = conjuntos[1] - conjuntos[0]
                interseccion_AB = conjuntos[0] & conjuntos[1]
                
                print(f"\nElementos solo en {nombres[0]}: {solo_A}")
                print(f"Elementos solo en {nombres[1]}: {solo_B}")
                print(f"Elementos en ambos: {interseccion_AB}")
                
            elif len(conjuntos) == 3:
                # Diagrama para 3 conjuntos
                venn_diagram = venn3([conjuntos[0], conjuntos[1], conjuntos[2]], set_labels=nombres)
                
                # Personalizar colores
                venn_diagram.get_patch_by_id('100').set_facecolor('lightblue')
                venn_diagram.get_patch_by_id('010').set_facecolor('lightgreen')
                venn_diagram.get_patch_by_id('001').set_facecolor('lightcoral')
                venn_diagram.get_patch_by_id('110').set_facecolor('lightyellow')
                venn_diagram.get_patch_by_id('101').set_facecolor('lightcyan')
                venn_diagram.get_patch_by_id('011').set_facecolor('lightpink')
                venn_diagram.get_patch_by_id('111').set_facecolor('white')
                
                # Añadir título
                plt.title(f"Diagrama de Venn: {nombres[0]}, {nombres[1]}, {nombres[2]}", 
                         fontsize=14, fontweight='bold')
                
                # Mostrar información detallada
                solo_A = conjuntos[0] - conjuntos[1] - conjuntos[2]
                solo_B = conjuntos[1] - conjuntos[0] - conjuntos[2]
                solo_C = conjuntos[2] - conjuntos[0] - conjuntos[1]
                AB = (conjuntos[0] & conjuntos[1]) - conjuntos[2]
                AC = (conjuntos[0] & conjuntos[2]) - conjuntos[1]
                BC = (conjuntos[1] & conjuntos[2]) - conjuntos[0]
                ABC = conjuntos[0] & conjuntos[1] & conjuntos[2]
                
                print(f"\nElementos solo en {nombres[0]}: {solo_A}")
                print(f"Elementos solo en {nombres[1]}: {solo_B}")
                print(f"Elementos solo en {nombres[2]}: {solo_C}")
                print(f"Elementos en {nombres[0]} y {nombres[1]} (no en {nombres[2]}): {AB}")
                print(f"Elementos en {nombres[0]} y {nombres[2]} (no en {nombres[1]}): {AC}")
                print(f"Elementos en {nombres[1]} y {nombres[2]} (no en {nombres[0]}): {BC}")
                print(f"Elementos en los tres conjuntos: {ABC}")
            
            # Configuraciones adicionales del gráfico
            plt.grid(False)
            plt.axis('on')
            
            # Mostrar el gráfico
            print("\nGenerando diagrama de Venn...")
            plt.tight_layout()
            plt.show()
            
            # Guardar el diagrama como imagen
            guardar = input("\n¿Desea guardar el diagrama como imagen? (s/n): ").lower()
            if guardar == 's':
                nombre_archivo = input("Nombre del archivo (sin extensión): ")
                plt.savefig(f"{nombre_archivo}.png", dpi=300, bbox_inches='tight')
                print(f"Diagrama guardado como {nombre_archivo}.png")
            
        except ImportError:
            print("Error: La librería matplotlib-venn no está instalada.")
            print("Instálela con: pip install matplotlib-venn")
            self._dibujar_diagrama_venn_textual(conjuntos, nombres)
        except Exception as e:
            print(f"Error al generar el diagrama: {e}")
            print("Mostrando representación textual...")
            self._dibujar_diagrama_venn_textual(conjuntos, nombres)
    
    def _dibujar_diagrama_venn_textual(self, conjuntos, nombres):
        """Representación textual alternativa si matplotlib no está disponible"""
        print("\n" + "="*50)
        print("DIAGRAMA DE VENN - REPRESENTACIÓN TEXTUAL")
        print("="*50)
        
        if len(conjuntos) == 2:
            A, B = conjuntos
            nombre_A, nombre_B = nombres
            
            solo_A = A - B
            solo_B = B - A
            interseccion_AB = A & B
            
            print(f"\n{nombre_A}: {A}")
            print(f"{nombre_B}: {B}")
            print(f"\nElementos solo en {nombre_A}: {solo_A}")
            print(f"Elementos solo en {nombre_B}: {solo_B}")
            print(f"Elementos en ambos: {interseccion_AB}")
            
        elif len(conjuntos) == 3:
            A, B, C = conjuntos
            nombre_A, nombre_B, nombre_C = nombres
            
            solo_A = A - B - C
            solo_B = B - A - C
            solo_C = C - A - B
            AB = (A & B) - C
            AC = (A & C) - B
            BC = (B & C) - A
            ABC = A & B & C
            
            print(f"\n{nombre_A}: {A}")
            print(f"{nombre_B}: {B}")
            print(f"{nombre_C}: {C}")
            
            print(f"\nElementos solo en {nombre_A}: {solo_A}")
            print(f"Elementos solo en {nombre_B}: {solo_B}")
            print(f"Elementos solo en {nombre_C}: {solo_C}")
            print(f"Elementos en {nombre_A} y {nombre_B} (no en {nombre_C}): {AB}")
            print(f"Elementos en {nombre_A} y {nombre_C} (no en {nombre_B}): {AC}")
            print(f"Elementos en {nombre_B} y {nombre_C} (no en {nombre_A}): {BC}")
            print(f"Elementos en los tres conjuntos: {ABC}")
    
    def menu_estructuras_control(self):
        while True:
            print("\n" + "="*50)
            print("SUBMENÚ - ESTRUCTURAS DE CONTROL")
            print("="*50)
            print("1. Ejemplo con WHILE")
            print("2. Ejemplo con FOR") 
            print("3. Ejemplo con IF")
            print("4. Crear conjunto personalizado")
            print("5. Modificar conjunto personalizado")
            print("6. Mostrar diagrama de Venn (Matplotlib)")
            print("7. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == '1':
                self.ejemplo_while()
            elif opcion == '2':
                self.ejemplo_for()
            elif opcion == '3':
                self.ejemplo_if()
            elif opcion == '4':
                self.crear_conjunto_personalizado()
            elif opcion == '5':
                self.modificar_conjunto_personalizado()
            elif opcion == '6':
                self.mostrar_diagrama_venn()
            elif opcion == '7':
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    # MENÚ PRINCIPAL
    def mostrar_menu_principal(self):
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL - OPERACIONES CON CONJUNTOS")
        print("="*50)
        print("1. add() - Agregar elemento")
        print("2. clear() - Limpiar conjunto")
        print("3. copy() - Copiar conjunto")
        print("4. difference() - Diferencia entre conjuntos")
        print("5. discard() - Descartar elemento")
        print("6. intersection() - Intersección")
        print("7. isdisjoint() - Verificar si son disjuntos")
        print("8. issubset() - Verificar subconjunto")
        print("9. issuperset() - Verificar superconjunto")
        print("10. pop() - Remover y retornar elemento")
        print("11. remove() - Remover elemento específico")
        print("12. union() - Unión de conjuntos")
        print("13. update() - Actualizar conjunto")
        print("14. Mostrar conjuntos actuales")
        print("15. Estructuras de control y conjuntos personalizados")
        print("16. Salir")
    
    def ejecutar(self):
        print("PROGRAMA AVANZADO DE OPERACIONES CON CONJUNTOS")
        print("Con matplotlib para diagramas de Venn")
        print("Conjuntos iniciales:")
        self.mostrar_conjuntos()
        
        while True:
            self.mostrar_menu_principal()
            opcion = input("\nSeleccione una opción (1-16): ")
            
            if opcion == '1':
                self.add()
            elif opcion == '2':
                self.clear()
            elif opcion == '3':
                self.copy()
            elif opcion == '4':
                self.diferente()
            elif opcion == '5':
                self.discard()
            elif opcion == '6':
                self.interseccion()
            elif opcion == '7':
                self.isdisjoint()
            elif opcion == '8':
                self.issubset()
            elif opcion == '9':
                self.issuperset()
            elif opcion == '10':
                self.pop()
            elif opcion == '11':
                self.remove()
            elif opcion == '12':
                self.union()
            elif opcion == '13':
                self.update()
            elif opcion == '14':
                self.mostrar_conjuntos()
            elif opcion == '15':
                self.menu_estructuras_control()
            elif opcion == '16':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
            
            # Mostrar estado actual después de cada operación
            if opcion not in ['14', '15', '16']:
                self.mostrar_conjuntos()

# Ejecutar el programa
if __name__ == "__main__":
    try:
        programa = MenuConjuntos()
        programa.ejecutar()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")