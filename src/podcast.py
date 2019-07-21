import feedparser
from utils import get_day_correlation

RSS_URL = "https://api.audioteca.rac1.cat/rss/la-competencia"

RSS_PODCASTS = feedparser.parse(RSS_URL)

def get_last_podcast():
    return RSS_PODCASTS['entries'][0]['link']

def get_podcast(day):
    rss_formatted_day = get_day_correlation(day) 
    for i in range(len(RSS_PODCASTS['entries'])):
        if rss_formatted_day in RSS_PODCASTS['entries'][i]['published']:
            return RSS_PODCASTS['entries'][i]['link']
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

