import requests, asyncio, aiohttp, time
from bs4 import BeautifulSoup
from tools import *
from collections import defaultdict


def exec_time(func):
  async def wrapper(*args, **kwargs):
    start_time = time.time()
    result = await func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution de {func.__name__}: {execution_time:.6f} secondes")
    return result
  return wrapper


def scrape_group(url:str, limit:int, total_url:list=[], url_page:int=1) -> list:
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  array_offers = soup.find_all('div', class_='grd-item prefooter-bloc', limit=limit)
  array_links = [elt.find('a')['href'] for elt in array_offers]

  total_url_links = total_url + array_links

  if len(array_links) == limit:
    return total_url_links
  else:
    new_rul_page = url_page + 1
    base_url = url.split('?')[0]
    new_url = base_url + "?page=" + str(new_rul_page)
    print(f"{new_rul_page} ==> {new_url}")
    new_limit = limit - len(array_links)
    return scrape_group(new_url, new_limit, total_url=total_url_links, url_page=new_rul_page)


async def fetch_page(session, url):
  async with session.get(url) as response:
    return await response.text()


def def_val():
  return "Non disponible"

async def scrape_link(url:str) -> str:
  final_data = defaultdict(def_val)
  async with aiohttp.ClientSession() as session:
    page = await fetch_page(session, url)
    soup = BeautifulSoup(page, "html.parser")
    name_.return_society_name(soup, final_data)
    date_.return_date(soup, final_data)
    body_.return_body(soup, final_data)
    return final_data


@exec_time
async def main(global_url:str, limit=10):

  links = scrape_group(global_url, limit=limit)

  tasks = [scrape_link(link) for link in links]

  results = await asyncio.gather(*tasks)
  results = [dico for dico in results if dico]

  #print(results)

  extract.save_to_excel(results)


if __name__ == "__main__":
  global_url = input("Insere l'url global : ")
  limit = input("Insère une limite d'extraction : ")
  asyncio.run(main(global_url, limit=int(limit)))