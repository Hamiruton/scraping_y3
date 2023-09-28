import requests, time
from bs4 import BeautifulSoup
from tools import *


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
def assembly(url: str):
  #new_list = url_list[:int(limit)]
  url_list = scraping_key_group(url)
  new_list = url_list
  name_list = []
  for elt in new_list:
    _ = scraping_one_offer(elt)
    name_list.append(_)
  return name_list


def scraping_key_group(url:str) -> list:
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  array_offers = soup.find_all('div', class_='grd-item prefooter-bloc')
  array_links = [elt.find('a')['href'] for elt in array_offers]
  return array_links


def scraping_one_offer(url:str) -> str:
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  name_soc = name_.return_society_name(soup)
  date_parution = date_.return_date(soup)
  list_info = body_.return_body(soup)
  return name_soc, date_parution, list_info


if __name__ == "__main__":
  global_url = "https://business.abidjan.net/annonces-legales/1-avis-de-constitution-de-societe"
  
  result = assembly(global_url)

  print(result)