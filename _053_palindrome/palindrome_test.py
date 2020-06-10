from unittest import TestCase
from _053_palindrome.palindrome import palindrome


class PalindromeTest(TestCase):
    def test1(self):
        self.assertEqual(0, palindrome('a?a'))

    def test2(self):
        self.assertEqual(1, palindrome('ab?'))

    def test3(self):
        self.assertEqual(4, palindrome('???'))

    def test4(self):
        a = ''
        for i in range(100):
            if i % 5 == 0:
                a = a + '?'
            else:
                a = a + 'a'
        raised = False
        try:
            result = palindrome(a)
            print(result)
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')
