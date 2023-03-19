from __future__ import print_function, division
import os
import re

# file:///{os.getcwd()}/assets/logo.png
class AssetManager:
    __icon = 'style="height:15px; width:auto;"'
    def __init__(self):
        self.__internal = {}
        for file in os.listdir(f'{os.getcwd()}/assets'):
           self.__internal[re.sub(r'\.[a-zA-Z0-9]+','',file)] = f'file:///{os.getcwd()}/assets/{file}'.replace('\\','/')
    
    def get(self, name : str):
        if name in self.__internal:
            return self.__internal[name]
        else: 
            return ''
    
    def tag(self, name):
        return f'<img src="{self.get(name)}" {AssetManager.__icon}/>'
