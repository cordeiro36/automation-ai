from secret import API_KEY
import requests
import json
import scraping
import pandas as pd

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
#https://api.openai.com/v1/models
id_modelo = "gpt-3.5-turbo"

noticias = scraping.url

contador = 0

for noticia in noticias:

    contador += 1

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": f"{noticia}"}]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)

    resposta = requisicao.json()

    mensagem = resposta["choices"][0]["message"]["content"]

    dados = pd.DataFrame([mensagem])

    dados.to_json(f'noticia{contador}.json', index=False)

    dados.to_csv(f'noticia{contador}.csv', index=False)

