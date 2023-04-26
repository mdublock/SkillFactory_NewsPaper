from django import template

register = template.Library()


@register.filter
def censor(value):
    if not isinstance(value, str):
        raise TypeError('Input value must be a string')

    censored_words = ['редиска', 'сосиска', 'кабачок']  # список слов, которые нужно заменить
    for word in censored_words:
        if word in value.lower():
            censored_word = word[0] + '*' * (len(word) - 1)
            value = value.replace(word, censored_word)
    return value