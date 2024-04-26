import json
import os
import sys


#Path of Project
def Project():
    return __file__.replace('\\UI\Operator\Path.py','')

def ConfigFiles():
    return Project() + '\\Config'


#Path in Config

def read_path_config(labels):
    if(labels == []):
        return ""
    with open(ConfigFiles() + '\\Path.json', 'r', encoding='utf-8') as f:
        pathConfig = json.load(f)
        try:
            current = pathConfig
            for label in labels:
                current = current[label]
            return current
        except:
            '[Error]: Unavailable Json Labels When Read Path Config'

def path_config():
    with open(ConfigFiles() + '\\Path.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def BlenderFoundation():
    return read_path_config(['Local','Blender Foundation'])

def WorkSpaces():
    return read_path_config(['WorkSpace'])

def AddWorkSpace(path):
    workspaces = WorkSpaces()
    if(workspaces == None):
        workspaces = [path]
    else:
        workspaces.append(path)
    config = path_config()
    config['WorkSpace'] = workspaces
    with open(ConfigFiles() + '\\Path.json','w',encoding='utf-8') as f:
        json.dump(config,f)