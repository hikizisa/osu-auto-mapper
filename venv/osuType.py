from enum import Enum
import operator


class HsSet(Enum):
    AUTO = 0
    NORMAL = 1
    SOFT = 2
    DRUM = 3


class Hitsound:
    def __init__(self, whistle = False, finish = False, clap = False):
        self.whistle = whistle
        self.finish = finish
        self.clap = clap


class HsInfo:
    def __init__(self, sampleSet = HsSet.AUTO, addSet = HsSet.AUTO,
                 volume = 0, customIndex = 0, filename = '', hitsound = Hitsound()):
        self.sampleSet = sampleSet
        self.addSet = addSet
        self.volume = volume
        self.customIndex = customIndex
        self.filename = filename
        self.hitsound = hitsound


class SliderType(Enum):
    L = 0
    P = 1
    B = 2
    C = 3


class Object:
    def __init__(self, x = 0, y = 0, time = 0, hsinfo = HsInfo(), nc = 0):
        self.x = x
        self.y = y
        self.time = time
        self.hsinfo = hsinfo
        self.nc = nc


class Circle(Object):
    # Circle doesn't have additional attributes
    def __init__(self, x = 0, y = 0, time = 0, hsinfo = HsInfo(), nc = 0):
        super(Circle, self).__init__(x, y, time, hsinfo, nc)


class Slider(Object):
    def __init__(self, x = 0, y = 0, time = 0, hsinfo = HsInfo(), nc = 0,
                 curvePoints = [], repeat = 1, pixelLength = 0, edgeHitsounds = []):
        super(Slider, self).__init__(x, y, time, hsinfo, nc)
        if curvePoints == []:
            curvePoints = [(x,y)]
        if edgeHitsounds == []:
            edgeHitsounds = [Hitsound()]

        # (x, y) type of curve points
        self.curvePoints = curvePoints
        self.repeat = repeat
        self.pixelLength = pixelLength
        # HsInfo type of hitsound, repeat + 1 length
        self.edgeHitsounds = edgeHitsounds


class Spinner(Object):
    def __init__(self, x = 0, y = 0, time = 0, hsinfo = HsInfo(), nc = 0, endtime = 0):
        super(Spinner, self).__init__(x, y, time, hsinfo, nc)
        self.endtime = endtime


class Hold(Object):
    # mania only
    pass


class TimingPoint:
    def __init__(self, offset = 0, beatlength = 500, meter = 4, hsinfo = HsInfo(), inherited = 0, kiai = 0):
        self.offset = offset
        self.beatlength = beatlength
        self.meter = meter
        self.hsinfo = hsinfo
        self.inherited = inherited
        self.kiai = kiai


class BeatmapData:
    def __init__(self):
        self.objects = []
        self.timings = []
        # relative route from song folder
        self.mp3 = 'audio.mp3'

        self.stackLeniency = 5.0
        self.mode = 0
        self.sampleSet = 1

        self.hp = 5
        self.cs = 5
        self.od = 5
        self.ar = 5

        # sm = SliderMultiplier, st = SliderTickRate
        self.sm = 1.0
        self.st = 1.0

        self.events = []

        self.title = ''
        self.id = 0
        self.version = ''

    def setVersion(self, version):
        self.version = version

    def general(self, mp3 = '', stackLeniency = 0.0, mode = 0, sampleSet = 1):
        self.mp3 = mp3
        self.stackLeniency = stackLeniency
        # 0 = std, 1 = taiko, 2 = ctb, 3 = mania
        self.mode = mode
        # 0 = normal, 1 = soft, 2 = drum
        self.sampleSet = sampleSet

    def difficulty(self, hp = 5, cs = 5, od = 5, ar = 5, sm = 1.0, st = 1.0):
        self.hp = hp
        self.cs = cs
        self.od = od
        self.ar = ar
        self.sm = sm
        self.st = st

    def events(self, events):
        # array of lines, just to restore .osu file later
        self.events = events

    def metadata(self, title = '', id = 0, version = ''):
        self.title = title
        self.id = id
        self.version = version

    def timing(self, timingPoint):
        self.timing.append(timingPoint)

    def addObjects(self, obj):
        self.objects.append(obj)

    def sortObjectTime(self):
        self.objects.sort(key=operator.attrgetter('time'))