# Samples

本文件夹提供了小的micropython开发M5Stack的样例。

**由于官方样例缺少HTTP方面的例子，本Sample主要在于HTTP模块上进行发展**

# Includes
- [x] 使用HTTP进行发报（POST）
  - 您应该替换WIFI模块的SSID，key，HTTP模块的服务器地址和证书
- [x] 检测RFID信息并控制POST
  - 您应该检查RFID模组的端口和您的设备是否相同
- [x] 使用Remote控制Emoji
  - 您可以发现emoji是自动刷新的
  - Remote的原理是MQTT上传数据到M5STACK服务器，所以您应设置好wifi

# How to use
 - 检查WIFI,Key是否匹配您的设备
 - 所有程序在[UIflow 1.4.5](https://flow.m5stack.com/) 上测试通过
 - Remote程序在[在线IDE](https://flow.m5stack.com/)有时不稳定，建议下载至本地

# Requirements
MIcropython  v1.11+

你可以在[M5STACK Community]上下载M5Burner进行固件烧录。

烧录过程：

![烧录界面](https://img-blog.csdnimg.cn/20200511000423632.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjIzMzMyMw==,size_16,color_FFFFFF,t_70)
