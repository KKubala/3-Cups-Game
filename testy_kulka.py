import unittest
from kulka import monit_kulki


class TestKulka(unittest.TestCase):
    def test_monit_kulkiB1(self):
        self.assertEqual(monit_kulki("B", 1), 2)

    def test_monit_kulkiB2(self):
        self.assertEqual(monit_kulki("B", 2), 1)

    def test_monit_kulkiB3(self):
        self.assertEqual(monit_kulki("B", 3), 3)

    def test_monit_kulkiC1(self):
        self.assertEqual(monit_kulki("C", 1), 1)

    def test_monit_kulkiC2(self):
        self.assertEqual(monit_kulki("C", 2), 3)

    def test_monit_kulkiC3(self):
        self.assertEqual(monit_kulki("C", 3), 2)


if __name__ == '__main__':
    unittest.main()
