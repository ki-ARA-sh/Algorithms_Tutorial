from unittest import TestCase
from unittest.mock import patch
import code


class MyTest(TestCase):
    @patch('code.input', create=True)
    def test_answer_yes(self, mocked_input):
        mocked_input.side_effect = ['4 4', '1 2 1', '2 3 0', '3 4 0', '2 4 0']
        result = code.main()
        print(result)
        self.assertEqual(result, '2 3 2 1')


    @patch('code.input', create=True)
    def test_answer_no(self, mocked_input):
        mocked_input.side_effect = ['4 3', '2 2 0', '2 3 1', '1 4 0']
        result = code.main()
        print(result)
        self.assertEqual(code.main(), '-1')
