"""
Class used to manage storing and retrieving data for a given system
"""
from __future__ import print_function, division
from typing import Dict, List, Any
import copy

from obj_classes.data_collection import DataCollection
class DataManager:
    def __init__(
        self,
        data : Dict[str, List[Any]]
    )-> None:
        """
        Class used to manage storing and retrieving data for a given system

        Parameters
        ----------
        data : `Dict[str, List[Any]]`
            A list of section objects defining the various data parameters for
            the system
        """
        self.__dataMap = {}
        for key in data:
            self.__dataMap[key.lower()] = {}
            for item in data[key]:
                if isinstance(item, DataCollection) or item.template == None:
                    self.__dataMap[key.lower()][item.name.lower()] = item
                else:
                    for element in item.template:
                        it = copy.deepcopy(item)
                        it.name = it.name.format(**element)
                        it.desc = it.desc(**element)
                        self.__dataMap[key.lower()][it.name.lower()] = copy.deepcopy(it)

    
    def addKey(self, keyName : str, keyData : List[Any]):
        self.__dataMap[keyName.lower()] = {}
        for item in keyData:
            self.__dataMap[keyName.lower()][item.name.lower()] = item
    
    def getItem(
        self,
        section : str,
        itemName : str,
    ) -> Any:
        """
        Used to look up a specific item stored in the internal data map

        Parameters
        ----------
        section : `str`
            The category to look for the item in
        itemName : `str`
            The name of the item to look up

        Returns
        -------
        item : `Any`
            The retrieved item if it was found; or None if it was not found
        """
        if section.lower() in self.__dataMap:
            if itemName.lower() in self.__dataMap[section.lower()]:
                return self.__dataMap[
                    section.lower()
                ][
                    itemName.lower()
                ]
        return None

    def typeToHTMLList(
        self,
        section : str
    ) -> List[str]:
        """
        Converts the data for a given section to a list of HTML tags

        Parameters
        ----------
        section : `str`
            The section to convert to HTML

        Returns
        -------
        html_tags : `List[str]`
            A list of strings representing the contained HTML
        """
        html = []
        sectionL = section.lower()
        if sectionL in self.__dataMap:
            for key in sorted(self.__dataMap[sectionL]):
                item= self.__dataMap[sectionL][key]
                html += [ f'{x}' for x in item.toHTMLList() ]
        return html