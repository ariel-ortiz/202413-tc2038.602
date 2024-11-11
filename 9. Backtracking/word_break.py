elements = {
    'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na',
    'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti',
    'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge',
    'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb', 'mo',
    'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te',
    'i', 'xe', 'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm',
    'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu', 'hf',
    'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 'tl', 'pb',
    'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th', 'pa', 'u',
    'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no',
    'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn',
    'nh', 'fl', 'mc', 'lv', 'ts', 'og'
}


def find(s: str, words: set[str], answer: list[str] = []) -> list[str] | None:
    if s == '':
        return answer
    index: int = 0
    word: str = ''
    while index < len(s):
        word += s[index]
        if word in words:
            new_answer: list[str] | None = \
                find(s[index + 1:], words, answer + [word])
            if new_answer is not None:
                return new_answer
        index += 1
    return None


def periodic_table_words(s: str) -> str | None:
    result: list[str] = []
    word: str
    for word in s.split():
        r: list[str] | None = find(word, elements)
        if r is not None:
            result.append('-'.join([x.capitalize() for x in r]))
        else:
            return None
    return '  '.join(result)


if __name__ == '__main__':
    words: set[str] = {
        'the', 'a', 'an', 'boy', 'girl',
        'dog', 'ran', 'ate', 'homework',
        'table', 'them', 'my', 'kissed'
    }
    # print(find('theboy', words))
    # print(find('thedogatemyhomework', words))
    # print(len(elements))
    print(periodic_table_words('chocolate'))
    print(periodic_table_words('promotion'))
    print(periodic_table_words('white chocolate sucks'))
    print(periodic_table_words('this fat boy thinks you watch black hats'))
    print(periodic_table_words('yes i think you scare python babies in argentina'))
    print(periodic_table_words('un taco bebe'))
