import pandas as pd

data = {
    "pandas:": ["Pata", "Tablero", "Puerta", "Estante","Panel Lateral"],
    "Centimetros": [40, 120, 60, 30, 100]
}

df = pd.DataFrame(data)

df.to_excel("mueble_medidas.xlsx", index=False)