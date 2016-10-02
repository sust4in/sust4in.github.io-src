#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ogulcan Gurcaglar'

SITENAME = "Ogulcan Gurcaglar"
SITEURL = 'http://localhost:8000'
SITENAME = "Ogulcan Gurcaglar's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'Read and :wq'
SITEDESCRIPTION = ''
SITELOGO = '//s.gravatar.com/avatar/d1199e94d0b102565a1b4ab0cf79e3ee?s=80'

FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

PATH = 'content'

TIMEZONE = 'Europe/Istanbul'

THEME = 'Flex'

LOAD_CONTENT_CACHE = False
DISPLAY_CATEGORIES_ON_MENU = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']


DATE_FORMATS = {
    'en': '%B %d, %Y',
}


MAIN_MENU = True


DEFAULT_LANG = 'tr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://www.github.com/sust4in'),
          ('linkedin', 'https://tr.linkedin.com/in/o%C4%9Fulcan-g%C3%BCr%C3%A7a%C4%9Flar-5793a7aa'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}


DISQUS_SITENAME = "ogurcaglarblog"
ADD_THIS_ID = 'ra-57f1150fb3bb5070'
GOOGLE_ANALYTICS = "UA-85018984-1"
GOOGLE_TAG_MANAGER = "GTM-MK4575"

STATUSCAKE = {
    'trackid': 'Nu34dBMqV5',
    'days': 7,
    'rumid': 6852,
    'design': 6,
}

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {
    	'path': 'static/custom.css'
    	}
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True
