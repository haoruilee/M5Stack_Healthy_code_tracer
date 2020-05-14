  '''
  This is the final main program for "Healthy code tracer"
  @author haoruili
  2020.5.12
  To run this file, you are supposed to change 
  1.DEVICE_ID
  2.API_KEY
  3.SSID
  4.PASSWORD
  '''
  from m5ui import *
  from uiflow import *
  import urequests
  import unit
  import urequests
  import network
  import socket
  import time
  import json
  from emoji import Emoji
  import wifiCfg
  from machine import UART,Pin

  #初始化
  setScreenColor(0x222222)
  gps0 = unit.get(unit.GPS, unit.PORTC)
  rfid0 = unit.get(unit.RFID, unit.PORTA)
  env0 = unit.get(unit.ENV, unit.PORTA)
  uart = UART(1, baudrate=115200,rx=16,tx=17,timeout=10)

  #UI界面
  emoji0 = Emoji(7, 7, 15, 9)
  rect4 = M5Rect(60, 61, 200, 1, 0xFFFFFF, 0xFFFFFF)
  label0 = M5TextBox(54, 7, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
  rect5 = M5Rect(60, 63, 1, 100, 0xFFFFFF, 0xFFFFFF)
  rect6 = M5Rect(60, 164, 200, 1, 0xFFFFFF, 0xFFFFFF)
  rect7 = M5Rect(259, 64, 1, 100, 0xFFFFFF, 0xFFFFFF)


  #全局变量
  #请将DEVICE_ID, API_KEY替换为您的HTTP接受端证书
  #请将SSI，PASSWORD替换为您的WIFI名称和密码
  DEVICE_ID='*******'
  API_KEY='***************8' 
  SSID="HWAWEI-HQ83GQ"
  PASSWORD="7312164459"
  wlan=None
  s=None

  ''' 
  def connectWifi(ssid,passwd):
    '''
    如果您的Micropython不携带WifiCfg.doconnect，请参考本函数
    函数作用：连接至名称为SSID，密码为passwd的wifi
    '''
    global wlan
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid,passwd)
    while(wlan.ifconfig()[0]=='0.0.0.0'):
      time.sleep(1)
    return True
  '''

  def http_put_data(data):
      '''
      传输单个数据点至ONENET平台的temperature数据流
      data:单个数据点
      url：http的post地址
      values:请参考https://open.iot.10086.cn/doc/multiprotocol/  文档中的"HTTP协议上传数据点模块，配置json格式信息"
      API_KEY:设备发送HTTP请求的证书，请参考https://open.iot.10086.cn/doc/multiprotocol/book/develop/http/api/api-usage.html  文档中的"鉴权说明"
      '''
      url='http://api.heclouds.com/devices/595818301/datapoints'
      values={'datastreams':[{"id":"temperature","datapoints":[{"value":data}]}]}
      jdata = json.dumps(values)                 
      r=urequests.post(url,
      data=jdata,
      headers={"api-key":API_KEY})
      return r

  def http_put_location(lon,lat):
      '''
      传输地理位置数据点至ONENET平台的location数据流
      lon:longitude,经度
      lat: latitude,纬度
      url：http的post地址
      values:请参考https://open.iot.10086.cn/doc/multiprotocol/  文档中的"HTTP协议上传数据点模块，配置json格式信息"
      API_KEY:设备发送HTTP请求的证书，请参考https://open.iot.10086.cn/doc/multiprotocol/book/develop/http/api/api-usage.html  文档中的"鉴权说明"
      '''
      url='http://api.heclouds.com/devices/595818301/datapoints'
      values={'datastreams':[{"id":"location","datapoints":[{"value":{"lon":lon,"lat":lat}}]}]}
      jdata = json.dumps(values)                 
      r=urequests.post(url,data=jdata,headers={"api-key":API_KEY})
      return r


  def http_put_RFID(data):
      '''
      传输RFID的卡片ID数据至ONENET平台的cus_RFID数据流
      data:RFID读取到的卡片ID
      url：http的post地址
      values:请参考https://open.iot.10086.cn/doc/multiprotocol/  文档中的"HTTP协议上传数据点模块，配置json格式信息"
      API_KEY:设备发送HTTP请求的证书，请参考https://open.iot.10086.cn/doc/multiprotocol/book/develop/http/api/api-usage.html  文档中的"鉴权说明"
      '''
      url='http://api.heclouds.com/devices/595818301/datapoints'
      values={'datastreams':[{"id":"cus_RFID","datapoints":[{"value":data}]}]}
      jdata = json.dumps(values)                 
      r=urequests.post(url,
      data=jdata,
      headers={"api-key":API_KEY})
      return r

    def http_put_qr(data):
      '''
      传输识别到的二维码至ONENET平台的cus_QR数据流
      data:QR Code info
      url：http的post地址
      values:请参考https://open.iot.10086.cn/doc/multiprotocol/  文档中的"HTTP协议上传数据点模块，配置json格式信息"
      API_KEY:设备发送HTTP请求的证书，请参考https://open.iot.10086.cn/doc/multiprotocol/book/develop/http/api/api-usage.html  文档中的"鉴权说明"
      '''
      url='http://api.heclouds.com/devices/595818301/datapoints'
      values={'datastreams':[{"id":"cus_QR","datapoints":[{"value":data}]}]}
      jdata = json.dumps(values)                 
      r=urequests.post(url,
      data=jdata,
      headers={"api-key":API_KEY})
      return r
    
    
  #Wifi连接并以emoji展示连接状态
  #wifi not connected
  emoji0.show_map([[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,0,0,0,1,0],[1,0,1,1,1,0,1],[0,1,0,0,0,1,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0xff0000)
  wifiCfg.doConnect('H10', 'xiaoDA11')
  #wifi connected
  if wifiCfg.wlan_sta.isconnected():
    emoji0.show_map([[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,0,0,0,1,0],[1,0,1,1,1,0,1],[0,1,0,0,0,1,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0x33ff33)
  else:
    wifiCfg.doConnect('H10', 'xiaoDA11')
    if wifiCfg.wlan_sta.isconnected():
      emoji0.show_map([[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,0,0,0,1,0],[1,0,1,1,1,0,1],[0,1,0,0,0,1,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0x33ff33)
    else:
      emoji0.show_map([[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]], 0xff0000)
      wait(20)
  emoji0.show_map([[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,0,0,0,1,0],[1,0,1,1,1,0,1],[0,1,0,0,0,1,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]], 0x33ff33)
  wait(1)

  #循环判断是否有卡片接近
  while(True):
    #熄灭RGB灯
    rgb.setBrightness(0)
    #清空Emoji显示
    emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]], 0x000000)
    #判断是否有卡片接近
    if rfid0.isCardOn():
      #有卡片接近显示对号
      emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,1],[1,0,0,0,1,1,0],[0,1,1,1,1,0,0],[0,0,1,1,0,0,0]], 0x33ff33)
      #发送RFID读取到的卡片ID
      rsp_RFID = http_put_RFID((str(rfid0.readUid())))
      #防止测试时无信号
      if str(gps0.pos_quality) != "1" and str(gps0.pos_quality) != "6":
        lon=116.39137751349433
        lat=39.8969585128568
      else:
        lon=gps0.longitude
        lat=gps0.latitude
      try:
        rsp_LOCATION=http_put_location(float(lon),float(lat))
      except:
        emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,1],[1,0,0,0,1,1,0],[0,1,1,1,1,0,0],[0,0,1,1,0,0,0]], 0xff0000)
      #传输温度
      rsp = http_put_data(env0.temperature)
      #完成后指示灯变绿
      rgb.setColorAll(0x33ff33)
      rgb.setBrightness(10)
      #等待乘客拿出手机扫码
      wait(5)
    #等待时间结束，RGB变色
    rgb.setColorAll(0x0DF6F6)
    if uart.any():
        rgb.setColorAll(0xFFFF)
        #接受串口数据
        b_data = uart.read()
        dat = '{}'.format(b_data.decode('UTF-8','ignore'))
        rsp_qr=http_put_qr(dat)
        emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,1],[1,0,0,0,1,1,0],[0,1,1,1,1,0,0],[0,0,1,1,0,0,0]], 0x000000)
    else:
      #可选是否断开wifi
      #wlan.disconnect()
      #wlan.active(False)
      #等待卡片接近时，Emoji展示"。。。"
      emoji0.show_map([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,1,0,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]], 0x000000)
    wait(1)
