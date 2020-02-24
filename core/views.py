from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Filmes
import pickle


def total_years(request):
    lista_anos = Filmes.objects.values('ano').annotate(qtde=Count('ano'), receita=Sum('receita')).order_by('-ano')
    return render(request, 'core/totalyears.html', {'listaanos': lista_anos})


def revenue_rank(request):
    filterano = request.GET.get('filterano')
    filtertop = request.GET.get('filtertop')

    if type(filterano) is str:
        filterano = int(filterano)

    lista_filmes = Filmes.objects.order_by('-receita')

    if filterano:
        if filterano != 0:
            lista_filmes = lista_filmes.filter(ano=filterano)

    if filtertop:
        if filtertop == 'on':
            lista_filmes = lista_filmes[:10]
        else:
            lista_filmes = lista_filmes[:4000]
    else:
        lista_filmes = lista_filmes[:4000]

    qtdefilmes = lista_filmes.count()
    lista_anos = Filmes.objects.values('ano').distinct().order_by('-ano')
    return render(request, 'core/revenuerank.html', {'listafilmes': lista_filmes, 'listaanos': lista_anos,
                                                     'filteranoatual': filterano, 'filtertopatual': filtertop,
                                                     'qtdefilmes': qtdefilmes})


def importfilmes(request):
    try:
        file = open('moviesdictclean', 'rb')
        dictnovo = pickle.load(file)
        print('ok')
        file.close()
    except FileNotFoundError:
        print('erro')
        dictnovo = {}

    # dictnovo{'2020': [ { }, { }, { } ], '2019': [ { }, { }, { } ] }
    # { } = {'Data_Lanc': x, 'Filme': y ....Genero, Tipo, Receita

    for ano, filmes in dictnovo.items():
        for filme in filmes:
            filmenew = Filmes()
            filmenew.nome = filme['Filme']
            filmenew.ano = filme['Ano']
            filmenew.mes = filme['Mes']
            filmenew.genero = filme['Genero']
            filmenew.tipo = filme['Tipo']
            filmenew.receita = filme['Receita']
            filmenew.save()

    return render(request, 'core/importfilmes.html')
