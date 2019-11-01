# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

extensions = [
    'sphinx_copybutton'
]
templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}
master_doc = 'index'
project = u'docss'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'docs'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False

latex_documents = [
  ('index', 'docs.tex', u'Documentation',
   u'', 'manual'),
]

def setup(app):
    app.add_stylesheet('custom.css')

