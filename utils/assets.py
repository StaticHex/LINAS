from __future__ import print_function, division
import os
import re

# file:///{os.getcwd()}/assets/logo.png
class AssetManager:
    def __init__(self):
        self.__internal = {}
        for file in os.listdir(f'{os.getcwd()}/assets'):
           self.__internal[re.sub(r'\.[a-zA-Z0-9]+','',file)] = f'file:///{os.getcwd()}/assets/{file}'
    
    def get(self, name : str):
        if name in self.__internal:
            return self.__internal[name]
        else: 
            return ''
