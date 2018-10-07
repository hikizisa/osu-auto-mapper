class Object:
	def hs(hs):
		pass

class Hitsound:
	pass

class BeatmapData:
	def __init__():
		self.objects = []
	def general(mp3 = '', stackLeniency = 0.0, mode = 0, sampleSet = 1):
		self.mp3 = mp3
		self.stackLeniency = stackLeniency
		# 0 = std, 1 = taiko, 2 = ctb, 3 = mania
		self.mode = mode
		# 0 = normal, 1 = soft, 2 = drum
		sampleSet = sampleSet
	def difficulty(hp = 5, cs = 5, od = 5, ar = 5, sm = 1.0, st = 1.0):
		#sm = SliderMultiplier, st = SliderTickRate
		self.hp = hp
		self.cs = cs
		self.od = od
		self.ar = ar
		self.sm = sm
		self.st = st
	def metadata(title = '', id = 0, version = ''):
		self.title = title
		self.id = id
		self.version = version
	def timing(self):
		pass
	def addobjects(object):
		self.objects.append(object)
	def sortobjectTime():
		self.objects.sort()