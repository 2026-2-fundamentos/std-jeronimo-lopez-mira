def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """
    
    import csv
    import gzip
    from collections import defaultdict

    min_max_values = defaultdict(lambda: [float('inf'), float('-inf')])

    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            if len(row) < 5:
                continue

            metrics = row[4]
            for pair in metrics.split(","):
                if ":" in pair:
                    key, value_str = pair.split(":")
                    try:
                        value = int(value_str)
                        min_max_values[key][0] = min(min_max_values[key][0], value)
                        min_max_values[key][1] = max(min_max_values[key][1], value)
                    except ValueError:
                        continue

    return [(key, min_val, max_val) for key, (min_val, max_val) in sorted(min_max_values.items())]
