import requests
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def coletorSlugs(url):
    slugs = []
    numPagina = 1
    # Garante que a URL base termine com '/' para a paginação funcionar
    if not url.endswith('/'):
        url += '/'

    while True:
        urlPaginada = url + 'page/' + str(numPagina)
        try:
            response = requests.get(urlPaginada, headers=headers, timeout=10)
            response.raise_for_status() # Lança um erro para status codes ruins (4xx ou 5xx)
        except requests.RequestException:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        filmes = soup.findAll('li', class_='poster-container')
        if not filmes:
            break

        slugs.extend(filme.find('div', class_='film-poster')['data-film-slug']
                    for filme in filmes if filme.find('div', class_='film-poster'))
        numPagina += 1
    return slugs

def coletorDados(slugFilme):
    try:
        urlFilme = f'https://letterboxd.com/film/{slugFilme}/'

        # Tenta pegar os dados JSON primeiro
        paginaJSON_url = f'https://letterboxd.com/film/{slugFilme}/json/'
        paginaJSON = requests.get(paginaJSON_url, headers=headers, timeout=10)
        paginaJSON.raise_for_status()
        conteudoJSON = json.loads(paginaJSON.text)

        # Coleta dados da página principal do filme
        paginaFilme = requests.get(urlFilme, headers=headers, timeout=10)
        paginaFilme.raise_for_status()
        conteudoPaginaFilme = BeautifulSoup(paginaFilme.content, 'html.parser')

        conteudoPaginaFilmeJSON_tag = conteudoPaginaFilme.find('script', type='application/ld+json')
        conteudoPaginaFilmeJSON = json.loads(conteudoPaginaFilmeJSON_tag.string.split('/* <![CDATA[ */')[-1].split('/* ]]> */')[0].strip())

        # Monta o dicionário com os dados extraídos
        dados_filme = {
            'nomeFilme': conteudoJSON.get("name"),
            'anoFilme': conteudoJSON.get("releaseYear"),
            'diretorFilme': conteudoJSON.get("directors")[0]["name"] if conteudoJSON.get("directors") else None,
            'duracaoFilme': conteudoJSON.get("runTime"),
            'sinopseFilme': conteudoPaginaFilme.find('div', class_='truncate').find('p').text.strip() if conteudoPaginaFilme.find('div', class_='truncate') else '',
            'notaFilme': conteudoPaginaFilmeJSON.get('aggregateRating', {}).get('ratingValue'),
            'avaliacoesFilme': conteudoPaginaFilmeJSON.get('aggregateRating', {}).get('ratingCount'),
            'urlFilme': urlFilme
        }

        return dados_filme
    except (requests.RequestException, KeyError, IndexError, json.JSONDecodeError):
        # Retorna None se houver qualquer erro durante a coleta de um filme específico
        return None

def iniciar_extracao(url):
    """
    Função principal do scraper. Recebe uma URL e retorna uma lista de dicionários de filmes.
    """
    slugs = coletorSlugs(url)
    filmes_coletados = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        # O .map executa a função para cada item na lista de slugs
        resultados = executor.map(coletorDados, slugs)

    for resultado in resultados:
        if resultado: # Adiciona à lista apenas se não for None (ou seja, se não houve erro)
            filmes_coletados.append(resultado)

    return filmes_coletados