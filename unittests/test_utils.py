from unittest import TestCase

from wrench.utils import (dynamic_load, camelcase_to_underscore, 
    rows_to_columns, parse_link, pprint)

# =============================================================================

class TestUtils(TestCase):
    def test_dynamic_load(self):
        import os
        fn = dynamic_load('os.path.abspath')
        self.assertEqual(os.path.abspath, fn)

    def test_camelcase(self):
        pairs = [
            ('one', 'one'),
            ('one_two', 'oneTwo'),
            ('one_two', 'OneTwo'),
        ]

        for pair in pairs:
            self.assertEqual(pair[0], camelcase_to_underscore(pair[1]))

    def test_rows_to_cols(self):
        matrix = [ 
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]

        expected = [ 
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
        ]

        self.assertEqual(expected, rows_to_columns(matrix))

    def test_parse_link(self):
        url, text = parse_link('')
        self.assertEqual('', url)
        self.assertEqual('', text)

        url, text = parse_link('before <a href="/foo/bar.html">Stuff</a> after')
        self.assertEqual('/foo/bar.html', url)
        self.assertEqual('Stuff', text)

    def test_pprint(self):
        d = {
            'foo':'bar',
            'thing':3,
        }

        expected = """{\n    "foo": "bar",\n    "thing": 3\n}\n"""

        from wrench.contexts import capture_stdout
        with capture_stdout() as output:
            pprint(d)

        self.assertEqual(expected, output.getvalue())
