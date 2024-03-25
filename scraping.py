from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=1024,720')

navegador = webdriver.Chrome(options=options)

navegador.get('https://g1.globo.com/')

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

dados_url = []

news_name = site.find('div', attrs={'id': 'bstn-fd-launcher'})

news_name_1 = news_name.find('a', attrs={'cmp-ltrk-idx': '1'})

news_name_2 = news_name.find('a', attrs={'cmp-ltrk-idx': '2'})

news_name_3 = news_name.find('a', attrs={'cmp-ltrk-idx': '3'})

news_name_4 = news_name.find('a', attrs={'cmp-ltrk-idx': '4'})

news_name_5 = news_name.find('a', attrs={'cmp-ltrk-idx': '5'})

url_noticia_1 = news_name_1['data-mrf-link']

url_noticia_2 = news_name_2['data-mrf-link']

url_noticia_3 = news_name_3['data-mrf-link']

url_noticia_4 = news_name_4['data-mrf-link']

url_noticia_5 = news_name_5['data-mrf-link']

url = [url_noticia_1, url_noticia_2, url_noticia_3, url_noticia_4, url_noticia_5]

dados_url.append([url_noticia_1, url_noticia_2, url_noticia_3, url_noticia_4, url_noticia_5])

dados = pd.DataFrame(dados_url)

dados.to_json('newsUrl.json', index=False)

dados.to_csv('newsUrl.csv', index=False)