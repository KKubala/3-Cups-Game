import unittest
from wybor import wybierz, tak_nie
from testy_narzedzia import *
from unittest.mock import MagicMock
import random


class TestWybierz(unittest.TestCase):
    def test_Wybierz_cup_1(self):
        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[False])
        podczerwien.bottom_left = MagicMock(side_effect=[False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 1)

        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[True])
        podczerwien.bottom_left = MagicMock(side_effect=[False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 2)

        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[False])
        podczerwien.bottom_left = MagicMock(side_effect=[True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 1)

    def test_Wybierz_cup_2(self):
        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 3)

        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 2)

        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[True, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 1)

    def test_Wybierz_cup_5(self):
        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True, True,
                                                      True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False, False,
                                                         False, False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 3)

        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[False, False, False,
                                                      False, False])
        podczerwien.bottom_left = MagicMock(side_effect=[True, True, True,
                                                         True, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 1)

        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, False, True,
                                                      False, True])
        podczerwien.bottom_left = MagicMock(side_effect=[True, False, False,
                                                         False, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 3), 2)

    def test_Wybierz_level_1(self):
        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[False])
        podczerwien.bottom_left = MagicMock(side_effect=[False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 1)

        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[True])
        podczerwien.bottom_left = MagicMock(side_effect=[False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 2)

        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[False])
        podczerwien.bottom_left = MagicMock(side_effect=[True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 1)

    def test_Wybierz_level_2(self):
        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 3)

        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 2)

        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[True, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 1)

    def test_Wybierz_cup_5(self):
        ts.ustaw_odpowiedzi([False, False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True, True,
                                                      True, True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False, False,
                                                         False, False, False])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 4)

        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[False, False, False,
                                                      False, False])
        podczerwien.bottom_left = MagicMock(side_effect=[True, True, True,
                                                         True, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 1)

        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, False, True,
                                                      False, True])
        podczerwien.bottom_left = MagicMock(side_effect=[True, False, False,
                                                         False, True])
        self.assertEqual(wybierz("font", ekran, ts, podczerwien, 4), 2)


class TestTak_Nie(unittest.TestCase):
    def test_tak_nie_1(self):
        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[False])
        podczerwien.bottom_left = MagicMock(side_effect=[False])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Want Guess?"),
                         True)

    def test_tak_nie_1(self):
        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[True])
        podczerwien.bottom_left = MagicMock(side_effect=[True])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         False)

    def test_tak_nie_1(self):
        ts.ustaw_odpowiedzi([False, True])
        podczerwien.top_left = MagicMock(side_effect=[True])
        podczerwien.bottom_left = MagicMock(side_effect=[False])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         False)

    def test_tak_nie_2(self):
        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, False])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False])
        self.assertEqual(tak_nie("f",  ekran, ts, podczerwien, "Play again?"),
                         False)

    def test_tak_nie_2(self):
        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, True])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         True)

    def test_tak_nie_2(self):
        ts.ustaw_odpowiedzi([False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[False, False])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         True)

    def test_tak_nie_5(self):
        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[True, False, True,
                                                      True, False])
        podczerwien.bottom_left = MagicMock(side_effect=[True, False, False,
                                                         True, True])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         True)

    def test_tak_nie_5(self):
        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[False, False, True,
                                                      False, True])
        podczerwien.bottom_left = MagicMock(side_effect=[False, True, True,
                                                         True, True])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         True)

    def test_tak_nie_5(self):
        ts.ustaw_odpowiedzi([False, False, False, False, False, True])
        podczerwien.top_left = MagicMock(side_effect=[False, False, False,
                                                      True, False])
        podczerwien.bottom_left = MagicMock(side_effect=[False, False, False,
                                                         False, False])
        self.assertEqual(tak_nie("f", ekran, ts, podczerwien, "Play again?"),
                         False)


if __name__ == '__main__':
    unittest.main()
