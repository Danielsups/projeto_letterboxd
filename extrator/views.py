from django.shortcuts import render, redirect
from .models import Filme
from . import scraper
from django.db import connection

def extracao_view(request):
    if request.method == 'POST':
        Filme.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'extrator_filme'")
        
        url = request.POST.get('letterboxd_url')
        if url:
            filmes_data = scraper.iniciar_extracao(url)
            for dados_filme in filmes_data:
                Filme.objects.create(
                    nomeFilme=dados_filme.get('nomeFilme'),
                    anoFilme=dados_filme.get('anoFilme'),
                    sinopseFilme=dados_filme.get('sinopseFilme'),
                    duracaoFilme=dados_filme.get('duracaoFilme'),
                    diretorFilme=dados_filme.get('diretorFilme'),
                    notaFilme=dados_filme.get('notaFilme'),
                    avaliacoesFilme=dados_filme.get('avaliacoesFilme'),
                    urlFilme=dados_filme.get('urlFilme')
                )
        return redirect('extracao_view')

    # Pega o parâmetro 'ordenar_por' da URL. Se não existir, o padrão é 'id'.
    ordenacao = request.GET.get('ordenar_por', 'id')

    # Mapeia as opções do formulário para os campos do modelo do Django.
    # O sinal de menos (-) antes do nome do campo indica ordem decrescente.
    mapa_ordenacao = {
        'melhor_avaliado': '-notaFilme',
        'pior_avaliado': 'notaFilme',
        'alfabetica_az': 'nomeFilme',
        'alfabetica_za': '-nomeFilme',
        'mais_recente': '-anoFilme',
        'mais_antigo': 'anoFilme',
        'id': 'id' # Padrão
    }

    # Busca o campo correspondente no mapa. Se a opção for inválida, usa o padrão 'id'.
    campo_para_ordenar = mapa_ordenacao.get(ordenacao, 'id')
    
    # Busca todos os filmes e aplica a ordenação.
    filmes = Filme.objects.all().order_by(campo_para_ordenar)

    context = {
        'filmes': filmes,
        'ordenacao_atual': ordenacao # Passa a ordenação atual para o template
    }
    return render(request, 'extrator/extracao.html', context)

def limpar_banco_view(request):
    """
    Esta view apaga todos os objetos Filme do banco de dados.
    """
    if request.method == 'POST':
        Filme.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'extrator_filme'")
            
    # Redireciona de volta para a página principal
    return redirect('extracao_view')