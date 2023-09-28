import PyPDF2, time


def exec_time(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution de {func.__name__}: {execution_time:.6f} secondes")
    return result
  return wrapper

@exec_time
def extract_text_from_pdf(pdf_file_path):
  with open(pdf_file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    text = ''
    
    #page = pdf_reader.pages[6]
    text = page.extract_text()

    for page_num in range(num_pages):
      page = pdf_reader.pages[page_num]
      text += page.extract_text()

  return text


@exec_time
def extract_acc_text(pdf_file_path, text_to_find):
  with open(pdf_file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    i = 0
    for page_num in range(num_pages):
      page = pdf_reader.pages[page_num]
      i += 1
      print(i)
      ext_page = page.extract_text()
      if text_to_find[0] in ext_page.lower() and text_to_find[1] in ext_page.lower():
        break

  return ext_page

if __name__ == "__main__":
  pdf_file_path = "journal_hier.pdf"
  pdf_text = extract_acc_text(pdf_file_path, text_to_find=['appel', 'offres'])
  print(pdf_text)