from m5stack import *
from m5ui import *
from uiflow import *
from emoji import Emoji
remoteInit()
setScreenColor(0x222222)



emoji0 = Emoji(7, 7, 15, 9)

temperature_s = None
x = None


def _remote_Slider_TEMP(temperature_s):
  global x 
  if temperature_s <= 38:
    emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[1,0,0,0,0,1,0],[0,1,0,0,1,0,0],[0,0,1,1,0,0,0],[0,0,0,0,0,0,0]], 0x33ff33)
  else:
    emoji0.show_map([[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]], 0xff0000)
#可以发现是自动刷新的
lcd.qrcode('http://flow-remote.m5stack.com/?remote=6yn2RgVrvOu2IQjiL3eA5HExU3VTyn3i', 1, 1, 10)
