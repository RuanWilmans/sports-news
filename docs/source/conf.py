# -- Project info -------------------------------------------------------------
project = "Sports News"
author = "Ruan Wilmans"

# -- Path + Django setup ------------------------------------------------------
import os, sys, django
root_doc = "index"                        # Sphinx 8
sys.path.insert(0, os.path.abspath('../..'))  # from docs/source -> project root
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# -- Extensions / Theme -------------------------------------------------------
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
html_theme = "sphinx_rtd_theme"
