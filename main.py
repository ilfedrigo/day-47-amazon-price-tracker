import requests
from bs4 import BeautifulSoup

PRODUCT_LINK = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(PRODUCT_LINK, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"})
product = response.text

soup = BeautifulSoup(product, "html.parser")

preco = soup.find(class_="a-offscreen", name="span")

preco_final = float(preco.text.replace('$', ''))


print(preco_final)