#!/usr/bin/env python3

'''
Given formatted input, will write out a properly formatted html file

Unit tests using PyTest:
    py.test test_html_render.py

Running tests using ipython:
    run run_html_render.py
    Creates -> test_html_output<step #>.html
'''

class Element:
    # Class names should normally use the CapWords convention
    # Class attributes are shared by all instances
    tag = 'html'    # Element doesn't really have a tag
    ind = ''

    # The __init__ method gets called when memory for the object is allocated

    def __init__(self, content=None):
        # Instance attributes unique to each instance
        self.content = []
        if content:
            self.content.append(content)
                
    # Other Methods

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(str(content))

    def render(self, out_file, ind = ''):
        out_file.write(self.ind + '<{}>\n'.format(self.tag))
        for content in self.content:
            if hasattr(content, 'render'):
                content.render(out_file, '')
            else:
                out_file.write(self.ind + '    ' + content + '\n')
        out_file.write(self.ind + '</{}>\n'.format(self.tag))

class OneLineTag(Element):

    def render(self, out_file, ind = ''):
        out_file.write(self.ind + '<{}>'.format(self.tag))
        for content in self.content:
            if hasattr(content, 'render'):
                content.render(out_file, "")
            else:
                out_file.write(self.ind + '   ' + content)
        out_file.write(self.ind + '</{}>\n'.format(self.tag))

class Head(Element):
    tag = 'head'
    ind = ''

class Html(Element):
    tag = 'html'
    ind = ''

class Body(Element):
    tag = 'body'
    ind = '    '

class P(Element):
    tag = 'p'
    ind = '        '

class Title(OneLineTag):
    tag = 'title'
    ind = '    '