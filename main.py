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
from sections.data_package import LINASDataPackage
from obj_classes.linas_entity import LinasEntity
from obj_classes.linas_item import LINASItem
from obj_classes.linas_abil import LINASAbility
from obj_classes.linas_technique import LinasTechnique
from campaigns.stirring_echoes import StirringEchoes
from systems.fantasy import Fantasy
from json import loads
import os
from sys import argv
import re

if __name__ == "__main__":
    # Define filenames and systems here
    cm=Fantasy()

    if 'campaign' in argv:
        if 'stirring_echoes' in argv:
            outFile = f"{os.getcwd()}/pdfs/stirring_echoes.pdf"

            # Create pdf generator
            se = StirringEchoes()

            generator = PDFGenerator(
                outputPath=outFile,
                cm=LINASDataPackage(se.contents, se.dm),
                debug=True
            )
            generator.writeOutToPDF()
    if 'technique' in argv:
        file = ""
        for arg in argv:
            if ".json" in arg:
                file = arg
        if os.path.exists(file):
            print(f'Writing out {os.path.basename(file).replace(".json","")} to disk ...')
            # Generate path to save file to
            outFile = f"{os.getcwd()}/pdfs/{os.path.basename(file).replace('.json','')}.pdf"

            # Load data from json and do some preprocessing
            f = open(file,'r')
            jdata = loads(f.read())
            f.close()

            # Create pdf generator
            generator = PDFGenerator(
                outputPath=outFile,
                cm=LinasTechnique(**jdata),
                debug=True
            )
            # Write out to file
            generator.writeOutToPDF()
        else:
            print(f'ERROR: Specified "{file}" as file to read but file does not exist.')
    if 'entity' in argv:
        file = ""
        for arg in argv:
            if ".json" in arg:
                file = arg
        if os.path.exists(file):
            print(f'Writing out {os.path.basename(file).replace(".json","")} to disk ...')
            # Generate path to save file to
            outFile = f"{os.getcwd()}/pdfs/{os.path.basename(file).replace('.json','')}.pdf"

            # Load data from json and do some preprocessing
            f = open(file,'r')
            jdata = loads(f.read())
            f.close()
            jdata['weapon'] = LINASItem(**jdata['weapon'])
            jdata['armor'] = LINASItem(**jdata['armor'])
            jdata['abilities'] = [ LINASAbility(**x) for x in jdata['abilities']]
            jdata['items'] = [ LINASItem(**x) for x in jdata['items'] ]

            # Create pdf generator
            generator = PDFGenerator(
                outputPath=outFile,
                cm=LinasEntity(**jdata),
                debug=True
            )
            # Write out to file
            generator.writeOutToPDF()
        else:
            print(f'ERROR: Specified "{file}" as file to read but file does not exist.')
    if 'book' in argv or 'all' in argv:
        print(f'Writing out handbook to disk ...')
        # Generate path to save file to
        outFile = f"{os.getcwd()}/pdfs/handbook.pdf"

        # Create pdf generator
        generator = PDFGenerator(
            outputPath=outFile,
            cm=cm,
            debug=True
        )
        # Write out to file
        generator.writeOutToPDF()
    if 'sheet' in argv or 'all' in argv:
        print("Writing out Character Sheet to disk ...")
        charSheetGenerator = PDFGenerator(
            outputPath=f"{os.getcwd()}/pdfs/character_sheet.pdf",
            cm=CharacterSheet(cm),
            debug=True
        )
        charSheetGenerator.writeOutToPDF()
    