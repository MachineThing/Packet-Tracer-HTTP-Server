from gui import GUI as gui
import time
gui.setup()

class InvalidErrorLevel(Exception):
	def __init__(self, lvl=None, msg="Invalid error level!"):
		if type(lvl).__name__ != 'int':
			msg = msg + " Error level is not an int but a(n) \"" + type(lvl).__name__ + "\"!"
		elif lvl > 3:
			msg = msg + " Error level is greater than 3!"
		elif lvl < 0:
			msg = msg + " Error level is less than 0!"
		else:
			msg = msg + " Unknown error!"
		super().__init__(self.msg)

def log(errorlvl, text):
	try:
		if errorlvl > 3 or errorlvl < 0:
			raise Exception
	except:
		raise InvalidErrorLevel(errorlvl)
	else:
		gui.update(errorlvl, time.strftime("%H:%M:%S")+" - " + text)
