import unittest
from silniki import przekrec, zamieszaj, sprawdz
from testy_narzedzia import silnikB, silnikC, sound, manipulator
from unittest.mock import MagicMock
import random


class TestPrzekrec(unittest.TestCase):
    def test_silnika_B(self):
        self.assertEqual(przekrec(silnikB, "B", 2, 230, -50, 3), 3)
        self.assertEqual(przekrec(silnikB, "B", 3, 230, -50, 2), 1)
        self.assertEqual(przekrec(silnikB, "B", 2, 230, -50, 1), 2)
        self.assertEqual(przekrec(silnikB, "B", 4, -230, 50, 3), 3)
        self.assertEqual(przekrec(silnikB, "B", 1, -230, 50, 2), 1)
        self.assertEqual(przekrec(silnikB, "B", 3, -230, 50, 1), 2)

    def test_silnika_C(self):
        self.assertEqual(przekrec(silnikC, "C", 2, 230, -50, 3), 2)
        self.assertEqual(przekrec(silnikC, "C", 3, 230, -50, 2), 3)
        self.assertEqual(przekrec(silnikC, "C", 2, 230, -50, 1), 1)
        self.assertEqual(przekrec(silnikC, "C", 4, -230, 50, 3), 2)
        self.assertEqual(przekrec(silnikC, "C", 1, -230, 50, 2), 3)
        self.assertEqual(przekrec(silnikC, "C", 3, -230, 50, 1), 1)


class TestZamieszaj(unittest.TestCase):
    def test_zamieszaj_pojedyncze(self):
        random.randint = MagicMock(side_effect=[1, 1])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)
        random.randint = MagicMock(side_effect=[1, 2])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)
        random.randint = MagicMock(side_effect=[1, 3])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 3)
        random.randint = MagicMock(side_effect=[1, 4])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 3)

    def test_zamieszaj_2obroty(self):
        random.randint = MagicMock(side_effect=[2, 1, 4])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)
        random.randint = MagicMock(side_effect=[2, 2, 3])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)
        random.randint = MagicMock(side_effect=[2, 1, 3])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)
        random.randint = MagicMock(side_effect=[2, 4, 3])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 2)

    def test_zamieszaj_5obrotow(self):
        random.randint = MagicMock(side_effect=[5, 2, 4, 1, 3, 2])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 3)
        random.randint = MagicMock(side_effect=[5, 1, 2, 4, 3, 2])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)
        random.randint = MagicMock(side_effect=[5, 1, 3, 4, 2, 4])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 3)
        random.randint = MagicMock(side_effect=[5, 4, 3, 3, 3, 2])
        self.assertEqual(zamieszaj(silnikB, silnikC, 2), 1)


class TestSprawdz(unittest.TestCase):
    def test_sprawdz_true(self):
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 2, 2),
                         (True, 2))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 1, 1),
                         (True, 2))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 3, 3),
                         (True, 2))

    def test_sprawdz_false(self):
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 1, 2),
                         (False, 1))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 1, 3),
                         (False, 3))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 2, 1),
                         (False, 1))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 2, 3),
                         (False, 3))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 3, 1),
                         (False, 1))
        self.assertEqual(sprawdz(sound, manipulator, silnikB, silnikC, 3, 2),
                         (False, 3))


if __name__ == '__main__':
    unittest.main()
