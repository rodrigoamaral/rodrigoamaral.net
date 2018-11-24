#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rodrigo Amaral'
SITENAME = u'Rodrigo Amaral'
SITEURL = 'http://rodrigoamaral.net'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Recife'

DEFAULT_LANG = u'pt-br'

# Theme
# THEME = 'pelican-octopress-theme'
THEME = 'hauntr'
DIRECT_TEMPLATES = (('index', 'archives', '404'))
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DEFAULT_CATEGORY = 'Blog'

# Menu

MENUITEMS = [('Sobre', '/sobre'),
             ('Blog', '/category/blog/'),
             ('Projetos', '#'),
             ('Palestras', '/palestras/')]
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['assets']

# Google Analytics
GOOGLE_ANALYTICS = 'UA-1400375-1'
