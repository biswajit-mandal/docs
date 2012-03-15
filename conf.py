# -*- coding: utf-8 -*-
#
# MongoDB documentation build configuration file, created by
# sphinx-quickstart on Mon Oct  3 09:58:40 2011.
#
# This file is execfile()d with the current directory set to its containing dir.

# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".ext")))
from mongodb_docs_meta import VersionMeta

# -- General configuration ----------------------------------------------------

needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', "sphinx.ext.extlinks", 'mongodb_domain', "additional_directives", "aggregation_domain"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'MongoDB'
copyright = u'2011-2012, 10gen, Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0.2'
release = version

current_git_commit = VersionMeta.commit
current_git_branch = VersionMeta.branch

rst_epilog = ".. |branch| replace:: ``" + current_git_branch + "``" + """
.. |commit| replace:: ``""" + current_git_commit + "``" + """
.. |copy| unicode:: U+000A9
.. |hardlink| replace:: http://docs.mongodb.org/""" + current_git_branch

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

extlinks = {
    'issue': ('https://jira.mongodb.org/browse/%s', '' ),
    'wiki': ('http://www.mongodb.org/display/DOCS/%s', ''),
    'api': ('http://api.mongodb.org/%s', ''),
    'source': ('http://github.com/mongodb/mongo/blob/master/%s', ''),
    'docsgithub' : ( 'http://github.com/mongodb/docs/blob/' + current_git_branch + '/%s', ''),
    'hardlink' : ( 'http://docs.mongodb.org/' + current_git_branch + '/%s', '')
    }

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes...
html_theme = 'mongodb'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + ' Manual'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "source/.static/logo-mongodb.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['source/.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

html_use_smartypants = True
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

manual_edition_path = 'http://docs.mongodb.org/' + current_git_branch + '/MongoDB-Manual-' + current_git_branch

html_theme_options = { 'branch': current_git_branch,
                       'commit': current_git_commit,
                       'pdfpath':  manual_edition_path + '.pdf',
                       'epubpath':  manual_edition_path + '.epub'
                       }

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'MongoDBdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
  # (source start file, target name, title, author, documentclass [howto/manual]).
    ('contents', 'MongoDB.tex', u'MongoDB Documentation', u'MongoDB Documentation Project', 'manual'),
]

latex_elements = { 'preamble': '\DeclareUnicodeCharacter{FF04}{\$} \DeclareUnicodeCharacter{FF0E}{.}',
                   'pointsize': '10pt',
                   'papersize': 'letterpaper'
                   }

latex_use_parts = True
latex_show_pagerefs = True
latex_show_urls = False
latex_domain_indices = True

# The name of an image file (relative to this directory) to place at the top of the title page.
#latex_logo = None

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# -- Options for manual page output --------------------------------------------

man_pages = [
  # (source start file, name, description, authors, manual section).
    ('contents', 'mongodb', u'MongoDB Manual', [u'MongoDB Documentation Project'], 1),
    ('reference/bsondump', 'bsondump', u'MongoDB BSON utility', [u'MongoDB Documentation Project'], 1),
    ('reference/mongo', 'mongo', u'MongoDB Shell', [u'MongoDB Documentation Project'], 1),
    ('reference/mongod', 'mongod', u'MongoDB Server', [u'MongoDB Documentation Project'], 1),
    ('reference/mongos', 'mongos', u'MongoDB Shard Utility', [u'MongoDB Documentation Project'], 1),
    ('reference/mongodump', 'mongodump', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongoexport', 'mongoexport', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongofiles', 'mongofiles', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongoimport', 'mongoimport', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongooplog', 'mongooplog', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongorestore', 'mongorestore', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongostat', 'mongostat', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongosniff', 'mongosniff', u'MongoDB', [u'MongoDB Documentation Project'], 1),
    ('reference/mongotop', 'mongotop', u'MongoDB', [u'MongoDB Documentation Project'], 1),
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'MongoDB'
epub_author = u'MongoDB Documentation Project'
epub_publisher = u'MongoDB Documentation Project'
epub_copyright = u'2011, 10gen Inc.'
epub_theme = 'epub_mongodb'
epub_tocdup = True
epub_tocdepth = 3
epub_language = 'en'
epub_scheme = 'url'
epub_identifier = 'http://docs.mongodb.org/' + current_git_branch
epub_exclude_files = []

# HTML files that should be inserted before/after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []
#epub_post_files = []
