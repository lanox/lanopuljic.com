#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Pelican settings ------------------------------------------------------------

# Basic
AUTHOR = 'Lano'
SITENAME = '#! Shit Lano Says'
SITEURL = 'http://lanopuljic.com'
# SITEURL = 'http://localhost:8000'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = 'http://lanopuljic.com/images/linkedin_logo.png'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
THEME = 'theme/lanox/'
TIMEZONE = 'Australia/Sydney'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URLs
ARTICLE_URL = '{date:%Y}/{date:%b}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{slug}.html'
PAGE_URL = '{date:%Y}/{date:%b}/{slug}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%b}/pages/{slug}.html'

# Delete the output directory, before generating new files
DELETE_OUTPUT_DIRECTORY = True

# Theme settings --------------------------------------------------------------

# Social widget
SOCIAL = (('github', 'http://github.com/lanox'),
          ('twitter', 'http://github.com/lanox'),
          ('linkedin', 'https://br.linkedin.com/in/lanopuljic/en'),)

# GOOGLE FONTS
GOOGLE_FONTS = [
    "Lato:400,700",
    "Source Code Pro",
    "Nunito:300",
]

# DISPLAY COVER IMAGE
COVER_IMG_URL = '/images/logo.jpg'

# FAVICON
FAVICON = SITEURL + '/images/favicon.png'

STATIC_PATHS = ['images']

# DISQUS Comments
DISQUS_SITENAME = "lanopuljic"

# Set menu buttons on side bar
MENU_ITEMS = [('Home', '/'),
              ('About', '/pages/about.html'), ('Work', '/pages/work.html'),
              ('Archives', '/archives.html'), ]

# Custome FOOTER Text
FOOTER_TEXT = ' builds things by banging on a keyboard.'

# TAGLINE - Used for the page titles and some meta tags.
TAGLINE = 'Life is binary, zeros and ones.'

# GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")
GOOGLE_ANALYTICS = 'UA-51180854-1'

# SHARE BUTTONS
ADD_THIS_ID = 'ra-55c72deca9344b40'

# Displays page number on main page.
DEFAULT_PAGINATION = False
