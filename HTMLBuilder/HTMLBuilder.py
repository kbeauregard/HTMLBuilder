from contextlib import contextmanager

INDENT = '  '


class HTMLBuilder:
    element_string = ''
    indent_level = 0
    
    def __init__(self, inital_html=None):
        self.element_string = inital_html + '\n' if inital_html else ''
    
    def __str__(self):
        return self.element_string
    
    def __repr__(self):
        return 'HTMLBuilder(%s)' % self.element_string
    
    @property
    def indent(self):
        return INDENT * self.indent_level
    
    @contextmanager
    def element(self, element, close=True, **kwargs):
        try:
            self.element_string += self._create_open_tag(element, **kwargs)
            if close:
                self.indent_level += 1
            yield self
        finally:
            if close:
                self.indent_level += -1
                self.element_string += self.indent + '</%s>\n' % element

    def _create_open_tag(self, element, **kwargs):
        if kwargs.get('_class'):
            kwargs['class'] = kwargs.pop('_class')
        variables = ' '.join(['="'.join(pair) + '"' for pair in kwargs.items()])
        variables = ' ' + variables if variables else variables
        return self.indent + '<%s%s>\n' % (element, variables)
            
    def write(self, string):
        self.element_string += self.indent + string + '\n'
        return self
