import unittest
from SimpleHTMLBuilder import SimpleHTMLBuilder


class TestHTMLBuilder(unittest.TestCase):
    def test_init(self):
        builder = SimpleHTMLBuilder('test string')

        self.assertEqual(builder.element_string, 'test string\n')

    def test_write(self):
        builder = SimpleHTMLBuilder()

        builder.write('test string')

        self.assertEqual(builder.element_string, 'test string\n')

    def test_element(self):
        builder = SimpleHTMLBuilder()

        with builder.element('a'):
            pass

        self.assertEqual(builder.element_string, '<a>\n</a>\n')

    def test_element_tags(self):
        builder = SimpleHTMLBuilder()

        with builder.element('a', href='https://www.example.com'):
            pass

        self.assertEqual(builder.element_string, '<a href="https://www.example.com">\n</a>\n')

    def test_element_class(self):
        builder = SimpleHTMLBuilder()

        with builder.element('div', _class='test-class'):
            pass

        self.assertEqual(builder.element_string, '<div class="test-class">\n</div>\n')
