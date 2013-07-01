#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""md2pdf - Markdown to PDF conversion tool.

Usage: md2pdf.py [options] INPUT.MD OUTPUT.PDF

Options:
    --css=STYLE.CSS
"""

import sys

from docopt import docopt
from markdown2 import markdown_path
from weasyprint import HTML, CSS


__title__ = 'md2pdf'
__version__ = '0.1'
__author__ = 'Julien Maupetit'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Julien Maupetit'


def main(argv=None):

    # Parse command line arguments
    arguments = docopt(
        __doc__,
        version='md2pdf %s' % __version__)

    # Paths
    md_file_path = arguments.get('INPUT.MD')
    pdf_file_path = arguments.get('OUTPUT.PDF')
    css_file_path = arguments.get('STYLE.CSS', None)

    # Convert markdown to html
    raw_html = markdown_path(md_file_path)

    # Weasyprint HTML object
    html = HTML(string=raw_html)

    # Get styles
    css = []
    if css_file_path:
        css.append(CSS(filename=css_file_path))

    # Generate PDF
    html.write_pdf(pdf_file_path, stylesheets=css)

    return 1


if __name__ == '__main__':
    sys.exit(main())
