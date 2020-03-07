from __future__         import print_function, division
from obj_classes.pdfgen import PDFGen

generator = PDFGen(True)
generator.writeOutPdf('./test.pdf')