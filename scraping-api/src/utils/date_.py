from bs4 import BeautifulSoup

def return_date(soup:BeautifulSoup, data:dict) -> None:
  try:
    _date = soup.find("div", class_="clearBoth margTop10 margBottom20 fwBold alDtails")
    re_date = _date.text.split()[4:]
    date = " ".join(re_date)
    data['date'] = date
  except:
    return None