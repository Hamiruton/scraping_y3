from bs4 import BeautifulSoup

def return_body(soup:BeautifulSoup, data:dict) -> None:
  div = soup.select('div.txt p')
  div = [elt.text for elt in div]
  for element in div:
    if 'capital' in element.lower():
      #list_info['capital'] = element
      data['capital'] = element
    if 'objet' in element.lower():
      #list_info['objet'] = element
      data['objet'] = element