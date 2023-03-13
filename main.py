#from __future__         import print_function, division
# from obj_classes.pdfgen import PDFGen

# generator = PDFGen(True)
# generator.writeOutPdf('./test.pdf')
"""
Main driver class used to run pdf generation
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.pdf_generator import PDFGenerator
from sections.character_sheet import CharacterSheet
from systems.fantasy import Fantasy
import os

if __name__ == "__main__":


    # Define filenames and systems here
    contentManagers = {
         "linas_fantasy":Fantasy()
    }

    for system in contentManagers:
        print(f'Writing out {system} to disk ...')
        # Generate path to save file to
        outFile = f"{os.getcwd()}/pdfs/{system}.pdf"

        # Create pdf generator
        generator = PDFGenerator(
            outputPath=outFile,
            cm=contentManagers[system],
            debug=True
        )

        charSheetGenerator = PDFGenerator(
            outputPath=f"{os.getcwd()}/pdfs/character_sheet.pdf",
            cm=CharacterSheet(contentManagers[system]),
            debug=True
        )

        # Write out to file
        generator.writeOutToPDF()
        charSheetGenerator.writeOutToPDF()