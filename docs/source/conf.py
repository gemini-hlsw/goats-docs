# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GOATS'
copyright = '2023, Association of Universities for Research in Astronomy'
author = 'Monika Soraisam'
#release = '23.10.0'
version = '23.10.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'

html_theme = "sphinx_rtd_theme"
#html_static_path = ['_static']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
html_logo = "images/GOATS_logo.png"


# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Figure numbering 
numfig = True

# Substitutions and replacements
rst_epilog = """
.. role:: raw-html(raw)
   :format: html

.. |TOMToolkit| replace:: :raw-html:`<a href="https://tom-toolkit.readthedocs.io/en/stable/">TOM Toolkit</a>`
.. |ANTARES| replace:: :raw-html:`<a href="https://antares.noirlab.edu/">ANTARES</a>`
.. |DRAGONS| replace:: :raw-html:`<a href="https://dragons.readthedocs.io/en/stable/">DRAGONS</a>`
.. |GOA| replace:: :raw-html:`<a href="https://archive.gemini.edu/">Gemini Observatory Archive</a>`
.. |Dlab| replace:: :raw-html:`<a href="https://datalab.noirlab.edu/">Astro Data Lab</a>`

"""
