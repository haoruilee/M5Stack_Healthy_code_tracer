# Samples

本文件夹提供了很多小的micropython开发M5Stack的样例。

**由于官方样例缺少HTTP方面的例子，本Sample主要在于HTTP模块上进行发展**

# Includes
- [x] 使用HTTP进行发报（POST）
  - 您应该替换WIFI模块的SSID，key，HTTP模块的服务器地址和证书
- [x] 检测RFID信息并控制POST
  - 您应该检查RFID模组的端口和您的设备是否相同
- [x] 使用Remote控制Emoji
  - 您可以发现emoji是自动刷新的
  - Remote的原理是MQTT上传数据到M5STACK服务器，所以您应设置好wifi

# Requirements
所有样例在UIflow 1.2上正确运行
