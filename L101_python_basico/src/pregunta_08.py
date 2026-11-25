def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """

    import csv
    import gzip
    from collections import defaultdict

    value_to_letters = defaultdict(set)

    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            if len(row) < 2:
                continue

            letter = row[0]
            try:
                value = int(row[1])
                value_to_letters[value].add(letter)
            except ValueError:
                continue

    return [(value, sorted(letters)) for value, letters in sorted(value_to_letters.items())]
