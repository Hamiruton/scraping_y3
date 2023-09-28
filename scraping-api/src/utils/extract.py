import openpyxl
import uuid
import os, shutil

dir_parent = os.getcwd()
dst_filepath = os.path.join(dir_parent, 'extraction-data')
columns_sheet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def save_to_excel(list_data):
  wb = openpyxl.Workbook()
  sheet = wb.active
  
  keys = list(list_data[0].keys())
  len_keys = len(keys)
  col_to_use = columns_sheet[:len_keys]

  for i in range(len_keys):
    sheet[col_to_use[i] + '1'] = keys[i]

  for itr_row,elt in enumerate(list_data):
    new_itr = str(itr_row + 2)
    for itr_col,value in enumerate(col_to_use):
      sheet[value+new_itr] = elt[keys[itr_col]]

  name_file = "data-" + str(uuid.uuid4()) + ".xlsx"
  wb.save(name_file)

  # Move file to extraction-data directory
  filepath = os.path.join(dir_parent, name_file)
  shutil.move(filepath, dst_filepath)
  print("Fichier créé")
  
  return name_file