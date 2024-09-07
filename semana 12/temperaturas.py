# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 25}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 17}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 23}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print("el promedio sera ",suma)

while True:
    print("selecciona una ciudad:")
    print("1. ciudad 1")
    print("2. ciudad 2")
    print("3. ciudad 3")
    print("4. salir ")

    opcion= input("ingrese la opcion deseada")
    if opcion == "1":
        ciudad = temperaturas(0)
        print(ciudad)
    else:

        print("no se encuentra la opcion deseada")
        continue