from bs4 import BeautifulSoup

def return_society_name(soup:BeautifulSoup) -> str:
  name = soup.find('h1')
  return name.text.strip()


def return_date(soup:BeautifulSoup) -> str:
  _date = soup.find("div", class_="clearBoth margTop10 margBottom20 fwBold alDtails")
  re_date = _date.text.split()[4:]
  date = " ".join(re_date)
  return date


def return_body(soup:BeautifulSoup) -> dict:
  list_info = {}
  div = soup.select('div.txt p')
  div = [elt.text for elt in div]
  for element in div:
    if 'capital' in element.lower():
      list_info['capital'] = element
    elif 'objet' in element.lower():
      list_info['objet'] = element
  
  return list_info