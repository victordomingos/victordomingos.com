# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from glob import glob
import platform

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


DELETE_OUTPUT_DIRECTORY = True


AUTHOR = u'Victor Domingos'
SITENAME = u'Victor Domingos'
SITEURL = u'https://victordomingos.com/testingvd'
BIO = u'Página oficial do autor'
DESCRIPTION = u'Página oficial de Victor Domingos - escritor e poeta português, autor de livros de narrativa e poesia, em edição impressa e e-book.'

PATH = 'content'
STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 2

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'pt'
LOCALE = "pt_PT"

HIDE_AUTHORS = True
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 150
PAGE_ORDER_BY = 'reversed-basename'
WITH_FUTURE_DATES = False

AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories.html'
CATEGORY_URL = 'index_files/{slug}.php'
CATEGORY_SAVE_AS = 'index_files/{slug}.php'
TAGS_SAVE_AS = ''

ARTICLE_URL = 'index_files/{slug}.php'
ARTICLE_SAVE_AS = 'index_files/{slug}.php'


PAGE_URL = '{category}/{slug}'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

YEAR_ARCHIVE_SAVE_AS = 'index_files/archive-{date:%Y}.php'
MONTH_ARCHIVE_SAVE_AS = ''

TAG_URL = ''
TAG_SAVE_AS = ''

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

DEFAULT_DATE_FORMAT = '%d %B %Y'

FEED_ALL_RSS = 'index_files/feed.xml'
CATEGORY_FEED_RSS = 'index_files/{slug}_rss.xml'
TAG_FEED_RSS = 'index_files/{slug}_rss.xml'

# global metadata to all the contents
DEFAULT_METADATA = {'author': 'Victor Domingos'}
SLUGIFY_SOURCE = 'basename'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/hyde"
SITESUBTITLE = 'Aprendiz de poeta e tantas coisas mais'

DISPLAY_DATE_ON_ARTICLE_LIST = False
SITEIMAGE_FOLDER = 'images/avatars/x150'  # Images to be used randomly in the header


SITEIMAGES = [ Path(*Path(img).parts[1:])
               for img in glob('{}/{}/*.png'.format(PATH,SITEIMAGE_FOLDER))]

SITEIMAGE_SIZE = 'width=100% height=100%'
SITEIMAGE = '/images/avatars/x150/avatar1.png' # Default Image that appears in the header


# Social widget
ICONS = (('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
         ('twitter', 'https://twitter.com/victordomingos'),
         ('linkedin', 'https://linkedin.com/in/victordomingos'),
         ('github', 'https://github.com/victordomingos'),
         ('stack-overflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)


PLUGIN_PATHS = ['plugins/']
PLUGINS = [
           'autostatic',
           'advthumbnailer',
           'related_posts',
           'neighbors',
           #'deadlinks',
          ]

DEADLINK_VALIDATION = True
DEADLINK_OPTS = {
        'archive': True,
        'classes': [],
        'labels': False,
        'timeout_duration_ms': 1000,
        'timeout_is_error': False,
    }

RELATED_POSTS_MAX = 3

"""
if CURRENT_PLATFORM != "iOS":
    # for instance if you have some plugin configurations not compatible with Pythonista
    pass
"""

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight',
                                           'linenums': True,
                                          },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'pyembed.markdown': {},
        # 'markdown.extensions.tables':{},
        },
    'output_format': 'html5',
    }

PYGMENTS_STYLE = "autumn"