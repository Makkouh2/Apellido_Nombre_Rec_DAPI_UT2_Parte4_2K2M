def create_email(nombre, apellido):
    """Función que me crea un email dependiendo del nombre y apellido
    - Parámetros:
        nombre: nombre del nombre
        apellido: apellido del alumno
    - Salida:
        Devuelve el email creado a partir del nombre y apellido
    """
    correo = nombre[0].lower() + apellido[:5].lower() + "@educacion.navarra.es"
    return correo

def calculate_grade(practica01, practica02, practica03, examen, recuperacion, actitud):
    """Función que me calcula la nota final de cada alumno
    - Parámetros:
        - Practica01: Nota float
        - Practica02: Nota float
        - Practica03: Nota float
        - Examen: Nota float
        - Recuperación: Nota float
        - Actitud: Nota float
    - Salida:
        - Nota final: nota del alumno
        - Aprobado: booleano true o false
    """
    notafinal = ((practica01 + practica02 + practica03) / 3) * 0.3 + max(examen, recuperacion) * 0.6 + actitud * 0.1
    aprobado = notafinal >= 5
    return notafinal, aprobado

import csv

def process_class(archivo_csv):
    """La función lee el archivo csv que contiene los datos de los alumnos
        -Parametros:
            archivo_csv: variable del archivo csv que tiene los datos.
        -Salida:
            Los datos nuevos se guadan en otro archivo csv llamado grades.csv"""
    alumnos = []

    with open(archivo_csv, newline="", encoding="utf-8") as file:
        x = csv.reader(file)
        next(x)  

        for linea in x:
            nombre = linea[0]
            apellido = linea[1]
            practica01 = float(linea[2].replace(',', '.'))
            practica02 = float(linea[3].replace(',', '.'))
            practica03 = float(linea[4].replace(',', '.'))
            examen = float(linea[5].replace(',', '.'))
            recuperacion = float(linea[6].replace(',', '.'))
            actitud = float(linea[7].replace(',', '.'))

            correo = create_email(nombre, apellido)
            nota_final, aprobado = calculate_grade(practica01, practica02, practica03, examen, recuperacion, actitud)
            nota_final_str = f"{nota_final:.2f}".replace('.', ',')

            datos_a_guardar = {
                'Nombre': nombre,
                'Apellido': apellido,
                'Email': correo,
                'Nota': nota_final_str,
                'Aprobado': aprobado
            }
            alumnos.append(datos_a_guardar)

    with open('grades.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nombre', 'Apellido', 'Email', 'Nota', 'Aprobado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for alumno in alumnos:
            writer.writerow(alumno)

process_class("class.csv")
