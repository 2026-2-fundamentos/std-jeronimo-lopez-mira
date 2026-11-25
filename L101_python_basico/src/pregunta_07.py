def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """

    import csv
    import gzip
    from collections import defaultdict

    value_to_letters = defaultdict(list)

    with gzip.open("data/data.csv.gz", "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            if len(row) < 2:
                continue

            letter = row[0]
            try:
                value = int(row[1])
                value_to_letters[value].append(letter)
            except ValueError:
                continue

    return [(value, letters) for value, letters in sorted(value_to_letters.items())]