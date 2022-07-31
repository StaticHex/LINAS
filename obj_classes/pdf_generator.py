"""
Class used to write out stored internal data to file
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
import os
import sys
import pdfkit

class PDFGenerator:
    """
    Class used to write out stored internal data to file

    Parameters
    ----------
    outputFile : `str`
        Location to write out the finalized pdf to
    cm : `ContentManager`
        The content manager for the class
    debug : `bool`
        If true is passed in, an HTML file will be printed alongside the PDF,
        default value is False (no html output)
    """
    def __init__(
        self,
        outputPath : str,
        cm         : ContentManager,
        debug      : bool = False
    ) -> None:
        self.outputPath = outputPath
        self.debug = debug
        self.cm = cm

        # Get directory of calling file i.e. name
        self.__cwd = os.getcwd()

        # Set up config for pdfkit
        self.__config   = pdfkit.configuration(
            wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
        )

        # Set up options for pdfkit
        msize='1.0in'
        self.__options = {
            'footer-center': '[page]',
            'page-size': 'Letter',
            'margin-top': msize,
            'margin-bottom': msize,
            'margin-left': msize,
            'margin-right': msize,
        }

        # Initialize internal HTML tag list
        self.__html = [ 
            "<!DOCTYPE html>",
            "<html>",
            "    <head>"
        ]

        # Append CSS to internal HTML
        self.__html.append("        <style>")
        fin = open(f"{self.__cwd}/styles.css", "r")
        for line in [ x.replace("\n","") for x in fin.readlines()]:
            self.__html.append(f"            {line}")
        fin.close()
        self.__html.append("        </style>")

        # Close head and open body for internal HTML
        self.__html.append("    </head>")
        self.__html.append("    <body>")

        # Add content from content manager to pdf
        self.__html += [ f"        {x}" for x in cm.toHTMLList() ]

    def writeOutToPDF(
        self
    ) -> None:
        # Finalize HTML
        self.__html.append("    </body>")
        self.__html.append("</html>")

        # if debugging, print out HTML doc
        if self.debug:
            f = open(f"{self.__cwd}/debug.html","w")
            f.write("\n".join(self.__html))
            f.close()

        # Write out pdf
        pdfkit.from_string( 
            "\n".join(self.__html), 
            self.outputPath, 
            configuration=self.__config,
            options=self.__options
        )

