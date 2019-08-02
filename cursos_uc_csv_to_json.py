import pandas as pd
import sys

data = {}
cursos = set()


def to_int(x):
    if isinstance(x, int):
        return x
    return int(x.split(",")[0])


dataset = pd.read_csv("Registro.csv", ";", encoding='utf-8').drop_duplicates()

del dataset["Cupos ocupados"]

dataset["Cupos disponibles"] = dataset["Cupos disponibles"].apply(to_int)
dataset["Cupos ofrecido"] = dataset["Cupos ofrecido"].apply(to_int)

group_dataset = dataset.groupby(
    ["Curso", "Sigla - sección", "Hora de consulta", "Tipo de vacante"]).sum().reset_index()
print(group_dataset.head())
group_dataset_2 = dataset.groupby(
    ["Curso", "Sigla - sección", "Hora de consulta"]).sum().reset_index()
print(group_dataset_2.head())

for line in group_dataset.itertuples():

    _, curso, sigle_section, time, type_vacant, ofrecidas, cupos_disponibles = line
    if ofrecidas == 0:
        continue

    if sigle_section not in data:
        data[sigle_section] = {
            "total_available": [],
            "type_available": {},
            "nombre": curso,
            "section": sigle_section.split("-")[1]
        }

    if type_vacant not in data[sigle_section]["type_available"]:
        data[sigle_section]["type_available"][type_vacant] = []
    
    data[sigle_section]["type_available"][type_vacant].append({"time": str(time).split(".")[0], "count": cupos_disponibles})

for line in group_dataset_2.itertuples():

    _, curso, sigle_section, time, ofrecidas, cupos_disponibles = line
    if sigle_section[:4] != "IIC{}".format(sys.argv[1]) or ofrecidas == 0:
        continue

    data[sigle_section]["total_available"].append({"time": str(time).split(".")[0], "count": cupos_disponibles})

import json

with open("cursos.json".format(sys.argv[1]), "w", encoding="UTF-8") as file2:
    json.dump(data, file2, indent=4, ensure_ascii=False)
