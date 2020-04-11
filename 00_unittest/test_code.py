from unittest import TestCase
from unittest.mock import patch
import code


class MyTest(TestCase):
    @patch('code.input', create=True)
    def test_answer_yes(self, mocked_input):
        mocked_input.side_effect = ['2', 'kiarash 20', 'bita 20']
        self.assertEqual(code.main(), {'kiarash': 20, 'bita': 20})

    # @patch('code.input', return_value='no')
    # def test_answer_no(self, input):
    #     self.assertEqual(code.main("test input?"), 'no')