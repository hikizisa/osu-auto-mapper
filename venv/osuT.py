class Object:
	def hs(hs):
		pass

class Hitsound:
	pass

class BeatmapData:
	class TimingPoint:
		def __init__(self, offset = 0, beatlength = 500, meter = 4, sampleSet = 0, sample = 0, volume = 100, inherited = 0, kiai = 0):
			self.offset = offset
			self.beatlength = beatlength
			self.meter = meter
			self.sampleSet = sampleSet
			self.sample = sample
			self.volume = volume
			self.inherited = inherited
			self.kiai = kiai
	def __init__(self):
		self.objects = []
		self.timing = []
	def general(self, mp3 = '', stackLeniency = 0.0, mode = 0, sampleSet = 1):
		self.mp3 = mp3
		self.stackLeniency = stackLeniency
		# 0 = std, 1 = taiko, 2 = ctb, 3 = mania
		self.mode = mode
		# 0 = normal, 1 = soft, 2 = drum
		sampleSet = sampleSet
	def difficulty(self, hp = 5, cs = 5, od = 5, ar = 5, sm = 1.0, st = 1.0):
		#sm = SliderMultiplier, st = SliderTickRate
		self.hp = hp
		self.cs = cs
		self.od = od
		self.ar = ar
		self.sm = sm
		self.st = st
	def metadata(self, title = '', id = 0, version = ''):
		self.title = title
		self.id = id
		self.version = version
	def timing(self, timingPoint):
		self.timing.append(timingPoint)
	def addobjects(self, object):
		self.objects.append(object)
	def sortobjectTime(self):
		self.objects.sort()