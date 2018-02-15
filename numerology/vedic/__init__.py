import datetime

import numerology.utils

ENGLISH = 'english'
CYRILLIC = 'cyrillic'
SANSKRIT = 'sanskrit'


NAME_MAP = {
    ENGLISH: {
        'AIJQY': 1,
        'BCKR': 2,
        'GLS': 3,
        'DMT': 4,
        'NE': 5,
        'UVWX': 6,
        'OZ': 7,
        'FHP': 8,
    },
    CYRILLIC: {
        'АКУЬ': 1,
        'БЛФЮ': 2,
        'ВМХЯ': 3,
        'ГНЦЁ': 4,
        'ДОЧ': 5,
        'ЕПШЭ': 6,
        'ЖРЩ': 7,
        'ЗСЪ': 8,
        'ИЙТЫ': 9,
    },
    SANSKRIT: {
        'क ट प य': 1,  # ka, ta, pa, ya
        'ख ठ फ र': 2,  # kha, tha, pha, ra
        'ग ड ब ल': 3,  # ga, da, ba, la
        'घ ढ भ व': 4,  # gha, dha, bha, va
        'ङ ण म श': 5,  # gna, na, ma, sa
        'च त ष': 6,  # ca, ta, sa
        'छ थ स': 7,  # cha, tha, sa
        'ज द ह': 8,  # ja, da, ha
        'झ ध': 9,  # jha, dha
        'क्ष': 0,  # ka
    },
}


def psychic_number(n, digits=1):
    """
    The psychic number in Vedic Numerology tells the way you look at yourself. It defines your basic characteristics.
    It reveals what you want to be or about the talents with which you have come to this earth.

    To obtain your psychic number you will have to find the single whole number of the date of your birth.
    Only the date is considered and you have to make it in a single one if it is two digit number.
    If your date of birth is 15th of any month your psychic number is 1+5=6

    :param n: date of birth (day only)
    :param digits: max number of digits you need in result
    :return: psychic number, if date is valid, None otherwise
    """
    if n <= 0 or n > 31:
        return None

    return numerology.utils.sum_digits(n, digits)


def destiny_number(date, digits=1):
    """
    This number in Vedic Numerology will reveal what the world think of you. It is the characteristics that other
    people find within you. The destiny number is obtained by adding the date, month and year of your birth
    and then converting that into a single digit whole number.

    The destiny number for a person takes birth in 15th May 1965 is 1+5+5+1+9+6+5=32=>3+2=5

    :param date: date of birth, either date object or yyyy-mm-dd formatted string
    :param digits: max number of digits you need in result
    :return: destiny number, if date is valid, None otherwise
    """
    if isinstance(date, str):
        try:
            d = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return None
    else:
        if not isinstance(date, datetime.date):
            return None
        else:
            d = date

    return numerology.utils.sum_digits(int(d.strftime("%Y%m%d")), digits)


def name_number(name, charset=ENGLISH, digits=1):
    """
    This number is arrived at by adding the numerological value of each letter in a name and reducing the total
    into a single compound number. As you can see below, each letter in the alphabet has been assigned a value
    between 1 and 8 based upon Vedic mathematics and the pattern of numbers present in the Vedic Square.
    Number 9 is not considered in such calculations because adding 9 to any other number does not alter its value
    (for example, 9 + 1 = 10 = 1, 9 + 2 = 11 = 2).

    :param name:
    :param charset: charset to use: ENGLISH, CYRILLIC, DEVANAGARI
    :param digits: max number of digits you need in result
    :return:
    """
    r = 0
    if charset not in NAME_MAP:
        return None
    for c in name.upper().replace(' ', ''):
        for k in NAME_MAP[charset].keys():
            if c in k:
                r += NAME_MAP[charset][k]

    if numerology.utils.count_digits(r) > digits:
        return numerology.utils.sum_digits(r, digits)

    return r

