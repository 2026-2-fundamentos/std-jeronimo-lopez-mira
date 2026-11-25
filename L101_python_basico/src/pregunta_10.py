def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo del formato de la respuesta:

        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """

    import csv
    import gzip
    from pathlib import Path

    result = []
    data_path = Path(__file__).resolve().parent.parent / "data" / "data.csv.gz"

    with gzip.open(data_path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            if len(row) < 5:
                continue

            letter = row[0]
            codes_count = len(row[3].split(",")) if row[3] else 0
            metrics_count = len(row[4].split(",")) if row[4] else 0

            result.append((letter, codes_count, metrics_count))

    return result