from __future__ import print_function, division
from obj_classes.data_manager import DataManager
from typing import List
class LINASDataPackage:
    def __init__(self, contents : List[str], data : DataManager):
        self.data : DataManager = data
        self.contents : List[str] = contents
    
    def toHTMLList(self):
        html = []
        for key in self.contents:
            html += [ f'    {x}' for x in 
                self.data.typeToHTMLList(key.lower())
            ]
        return html
    
        