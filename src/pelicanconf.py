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
BIO = u'Escritor&nbsp;independente. Curioso. Aprendiz&nbsp;de&nbsp;tudo.'
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
SITESUBTITLE = 'Página oficial de Victor Domingos'

SIDEBAR_LINKS = (
				 ('Notícias', 'index.html'),
				 ('Biografia', 'info/biografia.html'),
				 ('Livros', 'info/livros.html'),
				 ('Contactar', 'info/contactos.php'),
                )


PROFILE_IMAGE = 'autor/autor_victor-domingos_O_172.jpg'
PROFILE_IMAGE76 = 'autor/autor_victor-domingos_O_76.jpg'
PROFILE_IMAGE86 = 'autor/autor_victor-domingos_O_86.jpg'
PROFILE_IMAGE120 = 'autor/autor_victor-domingos_O_120.jpg'
PROFILE_IMAGE136 = 'autor/autor_victor-domingos_O_136.jpg'
PROFILE_IMAGE138 = 'autor/autor_victor-domingos_O_138.jpg'
PROFILE_IMAGE152 = 'autor/autor_victor-domingos_O_152.jpg'
PROFILE_IMAGE172 = 'autor/autor_victor-domingos_O_172.jpg'
PROFILE_IMAGE204 = 'autor/autor_victor-domingos_O_204.jpg'

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
