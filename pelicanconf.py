#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jacob Ritchie'
SITENAME = u'Jacob\'s Larder'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'
LOCALE= u"en_GB"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

'''
Disabled by mg theme - may re-enable later 

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''

SOCIAL = (('twitter', 'https://twitter.com/JWKRitchie'),
          ('github', 'https://github.com/jritch'),
          ('envelope', 'mailto:jacob.w.k.ritchie@gmail.com'),)


#Parameters inherited from the mg-theme
ALTNAME=SITENAME
SITESUBTITLE="Dried and pickled musings"
DESCRIPTION="A blog about whatever makes it out of the hole."

#DEFAULT_PAGINATION = True

THEME = "agit"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
