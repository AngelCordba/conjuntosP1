# Creación de conjuntos
estudiantes_matematicas = {"Ana", "Juan", "Diana", "Eva"}
estudiantes_fisica = {"Juan", "Diana", "Fran", "Gabo"}

# Intersección (estudiantes en ambos cursos)
ambos_cursos = estudiantes_matematicas & estudiantes_fisica
print(f"Estudian ambos: {ambos_cursos}")

# Diferencia (solo matemáticas)
solo_matematicas = estudiantes_matematicas - estudiantes_fisica
print(f"Solo matemáticas: {solo_matematicas}")
