import os, configparser, scipy
import subprocess as sp

# this is a main script for making audio dataset with fft

def findffmpeg():
    config = configparser.ConfigParser()
    config.read("automapper.cfg")

    ffmpegDir = config.get('ParseAudio', 'ffmpeg')
    ffmpeg = os.path.join(ffmpegDir,'ffmpeg.exe')
    if os.path.isfile(ffmpeg) == False:
        raise Exception("failed to find ffmpeg")
    else:
        return ffmpeg

# convert mp3 file to wav file
def toWav(audio):
    if os.path.isfile(audio) == False:
        raise Exception("failed to load audio : " + audio)
    wav = ('.').join(audio.split('.')[:-1]) + '.wav'

    p = sp.Popen([findffmpeg(), '-i', audio, wav], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

    if os.path.isfile(wav) == False:
        raise Exception('error occurred while converting : ' + audio + '\n')

def doFft(wav):
    pass

def loadSongData(audio):
    toWav(audio)
    fftArr = doFft(('.').join(audio.split('.')[:-1]) + '.wav')

if __name__ == "__main__":
    pass
# testcode