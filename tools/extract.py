import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
columns_sheet = ["A","B","C","D","E"]

def save_to_excel(list_data):
  keys = list(list_data[0].keys())
  len_keys = len(keys)
  col_to_use = columns_sheet[:len_keys]

  for i in range(len_keys):
    sheet[col_to_use[i] + '1'] = keys[i]

  for itr_row,elt in enumerate(list_data):
    new_itr = str(itr_row + 2)
    for itr_col,value in enumerate(col_to_use):
      sheet[value+new_itr] = elt[keys[itr_col]]

  wb.save("scrap_data.xlsx")
  print("Fichier créé")