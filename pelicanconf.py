#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import imp

jinjaext = imp.load_source('jinjaext', './jinjaext.py')

AUTHOR = u''
SITENAME = u"Cafe Gác Hoa"
SITEURL = ''
SITETAGLINE = ''

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/quangquach'),
          ('Twitter', 'http://twitter.com/quangquach'),
          ('Facebook', 'http://facebook.com/quangquach55'),)

DEFAULT_PAGINATION = 10

THEME = 'gachoa-theme'
#THEME = '../pelican-themes/lannisport'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
TYPOGRIFY = True

ARTICLE_URL = '/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'
TAGS_SAVE_AS = 'tag/index.html'
CATEGORIES_SAVE_AS = 'category/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

PLUGINS = ["assets",]

#JINJA_EXTENSIONS = [jinjaext.esitmate_time, ]
JINJA_FILTERS = {
'estimate_time': jinjaext.estimate_time ,
}

STATIC_PATHS = [
    'extra/CNAME',
    'images',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
