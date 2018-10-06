import numpy as np
import os, configparser
import osuT as o

# this is a script for making beatmap dataset

def general(f, data):
    line = f.readline()

    mp3 = '' ; stackLeniency = 0.0 ; mode = 0 ; sampleSet = 1

    while True:
        if line.startswith('['):
            break
        parsed = line.split('=')

        info = parsed[0].lstrip().rstrip() ; val = parsed[1].lstrip().rstrip()
        if info == 'AudioFilename': mp3 = val
        elif info == 'StackLeniency':
            try: stackLeniency = float(val)
            except SyntaxError: stackLeniency = 0.0
        elif info == 'Mode':
            try: mode = int(val)
            except SyntaxError: mode = 0
        elif info == 'SampleSet':
            if(val == 'Normal'): sampleSet = 0
            elif(val == 'Soft'): sampleSet = 1
            elif(val == 'Drum'): sampleSet = 2
        line = f.readline()

    data.general(mp3, stackLeniency, mode, sampleSet)

    return line

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
        line = general(f, data)
    elif header == 'Editor':
        line = editor(f, data)
    elif header == 'Metadata':
        line = metadata(f, data)
    elif header == 'Difficulty':
        line = difficulty(f, data)
    elif header == 'TimingPoints':
        line = timing(f, data)
    elif header == 'HitObjects':
        line = hitobjects(f, data)
    else:
        pass

    # do I have to return file object?
    return line

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

        line = processHeader(header,f,data)

    f.close()

if __name__ == "__main__":
    pass