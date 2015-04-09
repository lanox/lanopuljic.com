#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lano'
SITENAME = '#! Shit Lano Says'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/lanox'),
          ('twitter', '#'),
          ('bitbucket', 'https://bitbucket.org/lanox'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set Plugin Path and  Active Plugins
PLUGIN_PATHS = ['content/plugins/']
PLUGINS = ['gravatar']
#ASSET_SOURCE_PATHS = ['static/css/']

# GOOGLE FONTS
GOOGLE_FONTS = [
"Lato:400,700",
"Source Code Pro",
]

# DISPLAY COVER IMAGE 
COVER_IMG_URL = 'theme/images/logo1.jpg'

# THEME
THEME = 'theme/lanox/'

DISQUS_SITENAME = "lanopuljic"

# Set menu buttons on side bar
MENUITEMS = [('Archive', 'archives.html'), ('About', '/pages/about.html'), ('Work', '/pages/work.html'),]

# Custome FOOTER Text
FOOTER_TEXT = ' builds things by banging on a keyboard.'

#TAGLINE - Used for the page titles and some meta tags.
TAGLINE = 'Life is binary, zeros and ones.'

#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")


ARTICLE_URL = '{date:%Y}/{date:%B}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

# Displays page number on main page.
DEFAULT_PAGINATION = False