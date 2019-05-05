# Methods to set the notebook up
# Note that these have to be called in order


from IPython.core.display import HTML
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import set_matplotlib_formats

import json
import sys
import matplotlib
from matplotlib import pyplot as plt


# Name of this repo/folder
REPO_NAME = 'meetups/meetups/meetup-2019-05-02/martina-pugliese-object-detection-tensorflow/code'

# Relative paths to style files
CSS_FILE = 'custom.css'


def config_ipython():

    # Print vars on multiple lines in same cell without "print"
    InteractiveShell.ast_node_interactivity = "all"

    # Setting retina dispay quality for plots
    set_matplotlib_formats('retina')


def set_css_style(css_file_path=CSS_FILE):
    """
    Read the custom CSS file and load it into Jupyter.
    Pass the file path to the CSS file.
    """

    styles = open(css_file_path, 'r').read()
    return HTML(styles)
