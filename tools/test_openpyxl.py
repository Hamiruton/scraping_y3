import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
columns_sheet = ["A","B","C","D","E"]

data = [
  {"nom": "Alice", "age": 25, "ville": "New York"},
  {"nom": "Bob", "age": 30, "ville": "San Francisco"},
  {"nom": "Carol", "age": 22, "ville": "Los Angeles"}
]

keys = list(data[0].keys())
len_keys = len(keys)
col_to_use = columns_sheet[:len_keys]

for i in range(len_keys):
  sheet[col_to_use[i] + '1'] = keys[i]

for i,elt in enumerate(data):
  val = str(i + 2)
  for nb,j in enumerate(col_to_use):
    sheet[j+val] = elt[keys[nb]]

  """
  sheet['A' + val] = elt['nom']
  sheet['B' + val] = elt['age']
  sheet['C' + val] = elt['ville']
  """

wb.save("test_file.xlsx")