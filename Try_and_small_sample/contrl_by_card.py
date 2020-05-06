from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import unit

setScreenColor(0x222222)
gps0 = unit.get(unit.GPS, unit.PORTC)
rfid0 = unit.get(unit.RFID, unit.PORTA)




from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
from emoji import Emoji

setScreenColor(0x000000)



emoji0 = Emoji(7, 7, 15, 9)
rect4 = M5Rect(60, 61, 200, 1, 0xFFFFFF, 0xFFFFFF)
label0 = M5TextBox(54, 7, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
rect5 = M5Rect(60, 63, 1, 100, 0xFFFFFF, 0xFFFFFF)
rect6 = M5Rect(60, 164, 200, 1, 0xFFFFFF, 0xFFFFFF)
rect7 = M5Rect(259, 64, 1, 100, 0xFFFFFF, 0xFFFFFF)


import urequests
import network
import socket
import time
import json
 
DEVICE_ID='595818301'
API_KEY='u6nZShsdI71Bc3ghDnn8Jy0GKZw='
 
SSID="HWAWEI-HQ83GQ"
PASSWORD="7312164459"
wlan=None
s=None
 
def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True
 
def http_put_data(data):
    url='http://api.heclouds.com/devices/'+DEVICE_ID+'/datapoints'
    values={'datastreams':[{"id":"temperature","datapoints":[{"value":data}]}]}
    jdata = json.dumps(values)                 
    r=urequests.post(url,data=jdata,headers={"api-key":API_KEY})
    return r
    
connectWifi(SSID,PASSWORD)

while(True):
  if rfid0.isCardOn():
    rsp = http_put_data(12)
    emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]], 0xff0000)
  else:
    #wlan.disconnect()
    #wlan.active(False)
    emoji0.show_map([[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0xff0000)
  wait(1)

