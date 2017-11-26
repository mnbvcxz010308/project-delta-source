#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vipin G S'
SITEURL = 'https://vipings.com'
SITENAME = 'Essential DataScince'
SITETITLE = AUTHOR
SITESUBTITLE  = 'I\'m Vipin, from Kerala, India. Working as Software Engineer. I love Open Source and programming'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = SITEURL + '/images/profile.jpg'
#SITELOGO = 'https://pbs.twimg.com/profile_images/914885371095166976/yI0_Cn3O_400x400.jpg'
FAVICON = 'https://imgur.com/O6hIfF5'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
PATH = 'content'
STATIC_PATHS = ['images',]
TIMEZONE = 'Asia/Kolkata'
ROBOTS = 'index, follow'
GITHUB_CORNER_URL = 'https://github.com/vipings/vipings.github.io'
#STATUSCAKE = { 'trackid': 'BGwxi3zrk1', 'days': 7, 'design': 6, 'rumid': 6852 }
#GUAGES = '59f446e07218b5138403f40b'
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2017
ADD_THIS_ID = 'ra-59f43d72a564b093'
#EXTRA_PATH_METADATA = {
#    'extra/custom.css': {'path': 'static/custom.css'},
#}
#CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('about', 'http://getpelican.com/'),
         ('contact', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('email', 'gs.vipin@yahoo.in'),
          ('linkedin', 'https://www.linkedin.com/in/gsvipin/'),
	  ('github','https://github.com/vipings/' ),
	  ('twitter', 'https://twitter.com/vipingsnair/'),)

DEFAULT_PAGINATION = 10




# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup','sitemap', 'post_stats',]

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

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
print("Reached Here")
JINJA_ENVIRONMENT = {'extensions': ['']}
print("Reached Here2")
THEME = 'Theme/Flex'
GOOGLE_ANALYTICS = 'UA-108813279-1'
GOOGLE_TAG_MANAGER = 'GTM-WKDTT5P'
#GZIP_CACHE_OVERWRITE = True
GOOGLE_OPTIMIZE = 'GTM-NT4C39P'
