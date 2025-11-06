import csv

def get_raw(num_ligne):
    assert type(num_ligne) == int, "The type of num_ligne must be int"
    i = 0
    with open('data.csv', newline='', encoding='CP1252') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Essaie ',' si nécessaire
        for line in reader:
            if i == num_ligne:
                return line
            i += 1
    return None

print(type(get_raw(12))) 

def get_cell(x, y):
    row = get_raw(y)
    if row is not None and 0 <= x < len(row):
        return row[x]
    else:
        return None


print(get_cell(8, 4))
