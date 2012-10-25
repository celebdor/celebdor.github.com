#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Antoni Segura Puimedon"
SITENAME = u"People's front of Python"
SITEURL = 'http://blog.antoni.me'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

DEFAULT_PAGINATION = 10
MARKUP = ('md')
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),)

