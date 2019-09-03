import feedparser
from utils import get_day_correlation

def get_rss():
    rss_url = "https://api.audioteca.rac1.cat/rss/la-competencia"
    return feedparser.parse(rss_url)

def get_last_podcast():
    rss = get_rss()
    return rss['entries'][0]['link']

def get_podcast(day):
    rss_formatted_day = get_day_correlation(day) 
    rss = get_rss()
    for i in range(len(rss['entries'])):
        if rss_formatted_day in rss['entries'][i]['published']:
            return rss['entries'][i]['link']
    return -1

def get_available_days():
    available_days = [
        'lunes',
        'martes',
        'miercoles',
        'jueves',
        'viernes',
    ]
    return available_days
