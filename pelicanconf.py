#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jan Papousek'
SITENAME = '...'
SITEURL = ''
SITELOGO = 'images/papousek.jpeg'

THEME = 'notmyidea'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('adaptive learning group', 'http://www.fi.muni.cz/adaptivelearning/'),
    ('google scholar', 'https://scholar.google.cz/citations?user=ozn2O8gAAAAJ')
)

# Social widget
SOCIAL = (('github', 'https://github.com/papousek'),
          ('twitter', 'https://twitter.com/jan_papousek'),
          ('linkedin', 'https://www.linkedin.com/in/janpapousek/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
