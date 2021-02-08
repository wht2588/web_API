import unittest


class Test01(unittest.TestCase):

    def test01(self):
        print("test01 id=", id(self))

    def test02(self):
        print("test02 id=", id(self))
