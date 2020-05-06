#This file show a sample http connect to onenet

from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
from emoji import Emoji
import network
import socket
import time
import json

setScreenColor(0x000000)



emoji0 = Emoji(7, 7, 15, 9)
rect4 = M5Rect(60, 61, 200, 1, 0xFFFFFF, 0xFFFFFF)
label0 = M5TextBox(54, 7, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
rect5 = M5Rect(60, 63, 1, 100, 0xFFFFFF, 0xFFFFFF)
rect6 = M5Rect(60, 164, 200, 1, 0xFFFFFF, 0xFFFFFF)
rect7 = M5Rect(259, 64, 1, 100, 0xFFFFFF, 0xFFFFFF)



 
DEVICE_ID='595818301'
API_KEY='master-key'#You should change this
 
SSID="H10"
PASSWORD="xiaoDA11"
wlan=None
s=None
 
def connectWifi(ssid,passwd):
 #connect to the wifi
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True
 
def http_put_data(data):
 #post data into onenet
    url='http://api.heclouds.com/devices/'+DEVICE_ID+'/datapoints'
    values={'datastreams':[{"id":"temperature","datapoints":[{"value":data}]}]}
    jdata = json.dumps(values)                 
    r=urequests.post(url,data=jdata,headers={"api-key":API_KEY})
    return r

#If success, it will show a transverse line
try:
  connectWifi(SSID,PASSWORD)
  rsp = http_put_data(86)
  emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]], 0xff0000)
except:
  wlan.disconnect()
  wlan.active(False)
  emoji0.show_map([[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0xff0000)

#There is a samlpe code:
#for count in range(3):
#  try:
#    wifiCfg.doConnect('HUAWEI-HQ83GQ', '7312164459')
#    req = urequests.request(method='POST', url='http://api.heclouds.com/devices/595818301/datapoints',json={"datastreams":[{"id":"temperature","datapoints":[{"value":30}]}]}, headers={"apikey":"u6nZShsdI71Bc3ghDnn8Jy0GKZw="})
#    emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]], 0xff0000)
#  except:
#    emoji0.show_map([[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0xff0000)
