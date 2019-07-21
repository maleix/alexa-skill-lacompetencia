import unicodedata

"""
Since we are working with spanish utterances,
it is useful to remove accent marks
"""
def get_normalized_day(day):
    normalized_day = ''.join((c for c in unicodedata.normalize('NFD',day)
                                if unicodedata.category(c) != 'Mn'))
    return normalized_day.lower()

def get_day_correlation(day):
    day_correlation = {
        'lunes': 'Mon',
        'martes': 'Tue',
        'miercoles': 'Wed',
        'jueves': 'Thu',
        'viernes': 'Fri',
    }
    if day in day_correlation:
        return day_correlation[day]
    else:
        return 'Day not available'
