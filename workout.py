from math import exp
import enum

class Unit:
	def __init__(self):
		self.identity = 1
		self.type


class Meter(Unit):
	def __init__(self):
		Unit.__init__(self)

def add_method(cls, is_property=False):
	def decorator(func):
		if is_property:
			setattr(cls, func.__name__, property(func))
		else:
			setattr(cls, func.__name__, func)
		return func
	return decorator


def o2cost(vel,*,units=Meter):
	"""
	Compute the oxygen cost in ml/kg/minute for exercise
	of a given intensity (velocity) in meters/minute
	"""
	return 0.182258*vel + 0.000104*(vel*vel) - 4.6

def dropdead(t: float):
	"""
	Compute the percentage of maximum exertion an athlete can expend for
	the given duration in minutes
	"""
	return math.exp(-0.1932605*t)*0.2989558 + 0.1894393*math.exp(-0.012778*t) + 0.8

def vo2req(t, d):
	"""
	Compute the required oxygen availability in ml/kg/min for an athlete to complete
	the given distance (in meters) in the allotted time (in minutes)
	"""
	return o2cost(d/t)/dropdead(t)