#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thingspeak

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
]

project = "thingspeak"
source_suffix = ".rst"
master_doc = "index"
copyright = "2016, Mikołaj Chwalisz"
author = "Mikołaj Chwalisz"

version = thingspeak.__version__
release = thingspeak.__version__

language = None

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
todo_include_todos = True

templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "alabaster"
html_theme_options = {
    "logo_name": True,
    "description": "Python binding for ThingSpeak API",
    "github_user": "mchwalisz",
    "github_repo": "thingspeak",
    "github_banner": True,
    "github_button": True,
    "extra_nav_links": {
        "ThingSpeak.com": "https://thingspeak.com/",
        "Say Thanks!": "https://saythanks.io/to/mchwalisz",
    },
    "analytics_id": "UA-47922208-4",
}
html_sidebars = {
    "**": ["about.html", "navigation.html", "relations.html", "searchbox.html"]
}
htmlhelp_basename = "thingspeakdoc"

latex_elements = {}
latex_documents = [
    (
        master_doc,
        "thingspeak.tex",
        "thingspeak Documentation",
        "Mikołaj Chwalisz",
        "manual",
    )
]
texinfo_documents = [
    (
        master_doc,
        "thingspeak",
        "thingspeak Documentation",
        author,
        "thingspeak",
        "One line description of project.",
        "Miscellaneous",
    )
]

man_pages = [(master_doc, "thingspeak", "thingspeak Documentation", [author], 1)]

intersphinx_mapping = {"https://docs.python.org/": None}
