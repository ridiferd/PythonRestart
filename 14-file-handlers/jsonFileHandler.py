# Lab 14 - Modul pembaca berkas JSON
import json


def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
            print("berhasil berhasil berhasil hore")
    except IOError:
        print("Could not read file")
    return data
