import unittest
from HTMLBuilder import HTMLBuilder


class TestHTMLBuilder(unittest.TestCase):
    def test_init(self):
        builder = HTMLBuilder('test string')

        self.assertEqual(builder.element_string, 'test string\n')

    def test_write(self):
        builder = HTMLBuilder()

        builder.write('test string')

        self.assertEqual(builder.element_string, 'test string\n')

    def test_element(self):
        builder = HTMLBuilder()

        with builder.element('a'):
            pass

        self.assertEqual(builder.element_string, '<a>\n</a>\n')

    def test_element_tags(self):
        builder = HTMLBuilder()

        with builder.element('a', href='https://www.example.com'):
            pass

        self.assertEqual(builder.element_string, '<a href="https://www.example.com">\n</a>\n')

    def test_element_class(self):
        builder = HTMLBuilder()

        with builder.element('div', _class='test-class'):
            pass

        self.assertEqual(builder.element_string, '<div class="test-class">\n</div>\n')
