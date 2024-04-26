import json
import sys
import os
import Operator.Path as p

def FileFormats():
    with open(p.ConfigFiles() + "\\File.json",'r',encoding='utf-8') as f:
        file_config = json.load(f)
        return file_config['Formats']

def get_filtered_files(path):
    filterd_files = []
    files = os.listdir(path)
    for format in FileFormats():
        for file in files:
            if(file.endswith(format)):
                filterd_files.append(file)
    return filterd_files

