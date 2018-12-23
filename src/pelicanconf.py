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
BIO = u'Escritor independente, aprendiz de aeronáutica linguística, e um eterno autodidata de tudo e mais alguma coisa.'
DESCRIPTION = u'Página oficial de Victor Domingos - escritor e poeta português, autor de livros de narrativa e poesia, em edição impressa e e-book.'

PATH = 'content'
STATIC_PATHS = ['images', 'biblioteca']
PAGE_PATHS = ['paginas']
ARTICLE_PATHS = ['artigos']
DEFAULT_PAGINATION = 9
DEFAULT_ORPHANS = 2

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'pt'
LOCALE = "pt_PT"

HIDE_AUTHORS = True
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 0  # Do not generate summary automatically (to allow optional "read more" link" on index page)
PAGE_ORDER_BY = 'reversed-basename'
WITH_FUTURE_DATES = False

CATEGORIES_SAVE_AS = 'blog/categorias.html'
CATEGORY_URL = 'blog/categoria/{slug}.html'
CATEGORY_SAVE_AS = 'blog/categoria/{slug}.html'

TAGS_SAVE_AS = 'blog/tags.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'

ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'

PAGE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{category}/{slug}.html'

AUTHORS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

ARCHIVES_SAVE_AS = 'blog/arquivo.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/arquivo/{date:%Y}.html'
MONTH_ARCHIVE_SAVE_AS = ''

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

DEFAULT_DATE_FORMAT = '%-d-%-m-%Y'

FEED_ALL_RSS = 'index_files/feed.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}_rss.xml'
TAG_FEED_RSS = ''

# global metadata to all the contents
DEFAULT_METADATA = {'author': 'Victor Domingos'}
SLUGIFY_SOURCE = 'basename'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/hyde"
SITESUBTITLE = ''

SIDEBAR_LINKS = (
				 #('Bio', 'info/biografia.html'),
				 #('Livros', 'info/livros.html'),
				 #('Contacto', 'info/contactos.html'),
				 ('file-o', 'index.html'),
				 ('user', 'info/biografia.html'),
				 ('book', 'info/livros.html'),
				 ('comments-o', 'info/contactos.html'),
				 ('safari', 'etcetera/sitemap.html'),
                )



#DISPLAY_DATE_ON_ARTICLE_LIST = False
#SITEIMAGE_FOLDER = 'images/avatars/x150'  # Images to be used randomly in the header


'''
SITEIMAGES = [ Path(*Path(img).parts[1:])
               for img in glob('{}/{}/*.png'.format(PATH,SITEIMAGE_FOLDER))]

SITEIMAGE_SIZE = 'width=100% height=100%'
SITEIMAGE = '/images/avatars/x150/avatar1.png' # Default Image that appears in the header
'''

PROFILE_IMAGE = 'autor/autor_victor-domingos_O_280.jpg'


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
