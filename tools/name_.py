from bs4 import BeautifulSoup

def return_society_name(soup:BeautifulSoup, data:dict) -> None:
  try:
    name = soup.find('h1')
    data['name'] = name.text.strip()
  except:
    return None