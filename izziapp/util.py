remove_characters = [',', '/', ':', '.']


def date_format(item):
    for i in remove_characters:
        item = item.replace(i, '-')
    return item