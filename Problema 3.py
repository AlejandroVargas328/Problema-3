# ================================================
# PROBLEMA 4 - Videoteca Digital
# Fundamentos de Programación - UNAD
# ================================================

def contar_titulos_populares_recientes(videoteca, calificacion_min, anio_min):
    """
    Cuenta la cantidad de títulos que cumplen:
    - Calificación >= calificacion_min
    - Año de lanzamiento >= anio_min
    """
    conteo = 0
    for titulo in videoteca:
        if titulo[2] >= calificacion_min and titulo[1] >= anio_min:
            conteo += 1
    return conteo


# ====================== DATOS INICIALES ======================
videoteca = [
    ["Dune: Part Two", 2024, 8.6, "Ciencia Ficción"],
    ["Oppenheimer", 2023, 8.5, "Drama Histórico"],
    ["The Batman", 2022, 7.8, "Acción"],
    ["Everything Everywhere All at Once", 2022, 7.8, "Comedia"],
    ["Spider-Man: Across the Spider-Verse", 2023, 8.6, "Animación"],
    ["The Holdovers", 2023, 7.9, "Comedia Dramática"],
    ["Poor Things", 2023, 7.9, "Ciencia Ficción"],
    ["Barbie", 2023, 6.8, "Comedia"],
    ["Killers of the Flower Moon", 2023, 7.6, "Drama"],
    ["The Killer", 2023, 6.7, "Acción"]
]

# ====================== PROGRAMA PRINCIPAL ======================
print("=" * 60)
print("VIDEOTECA DIGITAL - Análisis de Material Popular y Reciente")
print("=" * 60)

# Solicitar datos al usuario
print("\nIngrese los criterios de búsqueda:")
cal_min = float(input("Calificación mínima (ej: 7.5): "))
anio_min = int(input("Año mínimo de lanzamiento (ej: 2023): "))

# Llamada a la función
resultado = contar_titulos_populares_recientes(videoteca, cal_min, anio_min)

# Mostrar resultados
print("\n" + "=" * 60)
print("RESULTADO DEL ANÁLISIS")
print("=" * 60)
print(f"Calificación mínima: {cal_min}")
print(f"Año mínimo: {anio_min}")
print(f"\nCantidad de títulos populares y recientes: **{resultado}**")

# Mostrar cuáles cumplen (opcional pero recomendado)
print("\nTítulos que cumplen los criterios:")
cumplen = 0
for titulo in videoteca:
    if titulo[2] >= cal_min and titulo[1] >= anio_min:
        print(f"• {titulo[0]} ({titulo[1]}) - Calificación: {titulo[2]}")
        cumplen += 1

if cumplen == 0:
    print("No se encontraron títulos que cumplan los criterios.")
