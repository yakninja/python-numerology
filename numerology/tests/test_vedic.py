import datetime
import unittest

from numerology import vedic


class PsychicNumber(unittest.TestCase):

    known_values = (
        (1, 1, 1), (10, 1, 1), (15, 1, 6), (29, 1, 2), (32, 1, None), (-1, 1, None), (0, 1, None),
        (1, 2, 1), (10, 2, 1), (15, 2, 6), (29, 2, 11), (32, 2, None), (-1, 2, None), (0, 2, None),
        (9, None, 9), (10, None, 1), (15, None, 6), (29, None, 11), (32, 2, None), (-1, 2, None), (0, 2, None),
    )

    def test_known_values(self):
        for n, d, pn in self.known_values:
            self.assertEqual(pn, vedic.psychic_number(n, d))


class DestinyNumber(unittest.TestCase):

    known_values = (
        ('1965-05-15', 1, 5), (datetime.date(1965, 5, 15), 1, 5),
        ('1980-02-30', 1, None), ('foobar', 1, None),
        ('1967-05-15', 2, 34), (datetime.date(1967, 5, 15), 2, 34),
        ('1980-02-30', None, None), ('foobar', None, None),
    )

    def test_known_values(self):
        for n, d, dn in self.known_values:
            self.assertEqual(dn, vedic.destiny_number(n, d))


class NameNumberEnglish(unittest.TestCase):

    known_values = (
        ('Numerology', 1, 7), ('Bharati Krishna Tirtha', 1, 7), ('Dharma', 1, 2),
        ('Bharati Krishna Tirtha', 2, 61), ('Name', 2, 15), ('Karma', 2, 10),
    )

    def test_known_values(self):
        for n, d, nn in self.known_values:
            self.assertEqual(nn, vedic.name_number(n, vedic.ENGLISH, d))


class NameNumberCyrillic(unittest.TestCase):

    known_values = (
        ('Нумерология', 1, 4), ('Имя', 1, 6), ('Карма', 1, 4),
        ('Нумерология', 2, 49), ('Имя', 2, 15), ('Карма', 2, 13),
    )

    def test_known_values(self):
        for n, d, nn in self.known_values:
            self.assertEqual(nn, vedic.name_number(n, vedic.CYRILLIC, d))


class NameNumberSanskrit(unittest.TestCase):

    known_values = (
        ('स्वामी भारती कृष्ण तीर्थ', 1, 1),
        ('स्वामी भारती कृष्ण तीर्थ', 2, 55),
        ('गोपीभाग्यमधुव्रातशृङ्गिशोदधिसन्धिग । कलजीवितखाताव गलहालारसंधर ॥', 3, 163),
    )

    def test_known_values(self):
        for n, d, nn in self.known_values:
            self.assertEqual(nn, vedic.name_number(n, vedic.SANSKRIT, d))


if __name__ == '__main__':
    unittest.main()