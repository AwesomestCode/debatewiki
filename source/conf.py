# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Portions of the debatewiki code were borrowed from Game Manual 0.

project = 'debatewiki'
copyright = '2023, debatewiki Contributors'
author = 'debatewiki Contributors'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "The Debate Wiki"
html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    #"sidebar_hide_name": True,
    #"light_logo": "assets/logo.png",
    #"dark_logo": "assets/logo_white.png",
    "light_css_variables": {
        # Both theme variables
        "font-stack": '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif',
        "admonition-font-size": "1rem",
        "admonition-title-font-size": "1rem",
        # Light theme only variables
    },
    "dark_css_variables" : {
        "color-background-primary": "#1f2022",
    },
}

html_theme_options = {
    "source_repository": "https://github.com/awesomestcode/debatewiki",
    "source_branch": "master",
    "source_directory": "source/",
}
