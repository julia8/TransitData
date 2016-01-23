from unittest import TestCase
from transitData import hello

class TestHello(TestCase):
    def test_giveMeNumber(self):
        self.assertEqual(hello.giveMeNumber(), 5)
