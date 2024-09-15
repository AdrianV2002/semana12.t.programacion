def calcular_promedio_temperaturas(temperaturas, ciudades, dias_semana):
    semanas = len(temperaturas[0])
    for i, ciudad in enumerate(ciudades):
        print(f"\nPromedios de temperatura para {ciudad}:")
        for j in range(semanas):
            promedio = sum(temperaturas[i][j]) / len(dias_semana)
            print(f"Semana {j+1}: {promedio:.2f}°C")


ciudades = ["Tena", "Guayaquil", "Quito", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

temperaturas = [
    # Ciudad de Tena con 4 Semanas
    [
        [25, 27, 28, 30, 22, 26, 24],
        [26, 29, 31, 28, 25, 24, 23],
        [30, 32, 33, 35, 29, 28, 27],
        [20, 21, 22, 23, 24, 25, 26]
    ],
    # Ciudad de Guayaquil con 4 Semanas
    [
        [22, 24, 26, 25, 23, 21, 20],
        [27, 28, 29, 26, 25, 24, 23],
        [32, 33, 31, 29, 28, 30, 27],
        [19, 20, 22, 24, 23, 21, 22]
    ],
    # Ciudad de Quito con 4 Semanas
    [
        [21, 22, 23, 24, 20, 19, 18],
        [25, 26, 27, 28, 24, 23, 22],
        [29, 30, 31, 32, 28, 27, 26],
        [18, 19, 20, 21, 22, 23, 24]
    ],
    # Ciudad de Cuenca con 4 Semanas
    [
        [18, 20, 18, 19, 20, 19, 18],
        [21, 21, 22, 24, 24, 23, 22],
        [20, 10, 15, 17, 18, 20, 21],
        [18, 19, 20, 21, 22, 23, 20]
    ]
]

calcular_promedio_temperaturas(temperaturas, ciudades, dias_semana)