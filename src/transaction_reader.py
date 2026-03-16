import csv

def csv_read_to_dict(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            return list(reader)
    except Exception:
        return []






#a = csv_read_to_dict('../data/transactions.csv')
#print(a)
