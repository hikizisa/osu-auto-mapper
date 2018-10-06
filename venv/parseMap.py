import numpy as np
import os, configparser
import osuT as o

# this is a script for making beatmap dataset

def general(f, data):
    pass

def editor(f, data):
    pass

def metadata(f, data):
    pass

def difficulty(f, data):
    pass

def timing(f, data):
    pass

def hitobjects(f, data):
    pass

def findHeader(header):
    return header[1:len(header)-2]

def processHeader(header, f, data):
    if header == 'General':
        f = general(f, data)
    elif header == 'Editor':
        f = editor(f, data)
    elif header == 'Metadata':
        f = metadata(f, data)
    elif header == 'Difficulty':
        f = difficulty(f, data)
    elif header == 'TimingPoints':
        f = timing(f, data)
    elif header == 'HitObjects':
        f = hitobjects(f, data)
    else:
        pass

    # do I have to return file object?
    return f

def readFile(osu):
    f = open(osu, 'r')
    data = o.BeatmapData()

    line = f.readline()
    while True:
        if not line: break
        if line.startswith('['):
            header = findHeader(line)
        else:
            line = f.readline()
            continue

        f = processHeader(header,f,data)

    f.close()