"""
Class used to hold and modify data for LINAS' classes
"""
from __future__ import print_function, division
from typing import Any, List, Tuple, Dict
from obj_classes.data_manager import DataManager
from obj_classes.data_collection import DataCollection
from obj_classes.linas_item import LINASItem
import re
import os
import copy

class ItemRecord:
    """
    Internal struct used to more cleanly parse passed in
    items

    Parameters
    ----------
    item : `Any`
        Can either be a LINASItem or a Tuple representing an item to look up in
        the data manager or an item itself
    qty : `int`
        The number (quantity) of items to give 
    """
    def __init__(
        self,
        item : Any,
        qty  : int
    ) -> None:
        self.item = item
        self.qty = qty

class LINASClass:
    def __init__(
        self,
        name        : str,
        description : str,
        skills      : List[Tuple[str, int]] ,
        items       : List[ItemRecord],
        data        : DataManager,
        image       : str = "empty_image.png",
        template    : List[Dict[str,str]] = None,
        notes       : List[str] = []
    ) -> None:
        """
        Class used to hold and modify data for LINAS' classes

        Parameters
        ----------
        name : `str`
            The name of the class
        description : `str`
            The text description for the class
        skills : `List[Tuple[str, int]]`
            List of skills and their values to assign to the class
        items : `List[Tuple[str, int]]`
            A list of items (and the number of each item) to be given to the class
        data : `DataManager`
            The data for the class, needed load in the abilities for the race
        image : `str`
            Image to use for the race, image must exist under the assets
            directory
        template : `List[Dict[str,str]]`
            An (optional) template to expand the current template by
        notes : `List[str]`
            A list of notes to display about the class
        """
        self.name      = name
        self.desc      = re.sub(r'[\ \n]+', ' ', description)
        self.skills    = skills
        self.items     = items
        self.image     = f"file:///{os.getcwd()}/assets/{os.path.basename(image)}"
        self.template  = template
        self.notes     = notes

        # Post processing of abilities i.e. find the abilities in the data
        # manager and cache them
        expandedItems : List[Tuple[LINASItem, int]] = []
        for record in self.items:
            if isinstance(record.item, LINASItem):
                expandedItems.append((record.item, record.qty))
            elif isinstance(record.item, tuple):
                itemName, itemType = record.item
                section : DataCollection = data.getItem(
                    'items', 
                    itemType.title()
                )
                foundItem : LINASItem = section.getChild(
                    itemName.title()
                )
                expandedItems.append((foundItem, record.qty))
        self.items = expandedItems

    def toHTMLList(
        self
    ) -> List[str]:
        """
        Returns contents of class as a formatted HTML block

        Returns
        -------
        html_tags : `List[str]`
            A list of strings representing the contained HTML
        """
        html = [
            f'<div style="page-break-before: always;"></div>',
            f'<div class="container pop">',
            f'    <div class="cont-title">',
            f'        <h3 class="nopad">{self.name}</h3>',
            f'    </div>',
            f'    <div class="cont-inner">',
            f'        <img class="img-wrapped" src="{self.image}"/>',
            f'        {self.desc}'
            f'    </div>',
            f'    <div class="cont-sub-title cont-inner">',
            f'        <strong>Skills</strong>',
            f'    </div>',
            f'    <div class="cont-inner">',
            f'        <ul>',
        ]
        for skill in self.skills:
            skillName, skillValue = skill
            skillValue = f'+{skillValue}' if skillValue >= 0 else skillValue
            html.append(f'            <li>{skillName.title()}: {skillValue}</li>')
        html+= [
            f'        </ul>',
            f'    </div>',
            f'    <div class="cont-sub-title cont-inner">',
            f'        <strong>Items</strong>',
            f'    </div>',
            f'    <div class="cont-inner" style="font-size:11pt;">'
        ]
        for item, qty in self.items:
            it = copy.deepcopy(item)
            it.cost = qty
            html += [ 
                x.replace("Cost:","Qty:")
                for x in it.toHTMLList() 
            ]
            break
        html += [
            f'    </div>',
            f'</div>'
        ]
        if len(self.notes):
            html += [
                f'<strong><u>Notes: </u></strong>',
                f'<ul>'
            ]
            for note in self.notes:
                note = re.sub(r'[\ \n]+',' ', note)
                html.append(f"    <li>{note}</li>")
            html.append('</ul>')
        return html