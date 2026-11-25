def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """
    import csv
    import gzip
    from collections import Counter
    from pathlib import Path

    counts = Counter()
    data_path = Path(__file__).resolve().parent.parent / "data" / "data.csv.gz"

    with gzip.open(data_path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            if len(row) < 3:
                continue

            date = row[2]
            if len(date) >= 7 and date[4] == "-":
                counts[date[5:7]] += 1

    return [(month, counts[month]) for month in sorted(counts)]
