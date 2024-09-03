ciudades = ["Tena", "Guayaquill", "Quito"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

temperaturas = [
    [
        [25, 27, 28, 30, 22, 26, 24],
        [26, 29, 31, 28, 25, 24, 23],
        [30, 32, 33, 35, 29, 28, 27],
        [20, 21, 22, 23, 24, 25, 26]
    ],
    [
        [22, 24, 26, 25, 23, 21, 20],
        [27, 28, 29, 26, 25, 24, 23],
        [32, 33, 31, 29, 28, 30, 27],
        [19, 20, 22, 24, 23, 21, 22]
    ],
    [
        [21, 22, 23, 24, 20, 19, 18],
        [25, 26, 27, 28, 24, 23, 22],
        [29, 30, 31, 32, 28, 27, 26],
        [18, 19, 20, 21, 22, 23, 24]
    ]
]


for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")
    for j in range(semanas):
        promedio = sum(temperaturas[i][j]) / len(dias_semana)
        print(f"Semana {j+1}: {promedio:.2f}°C")
