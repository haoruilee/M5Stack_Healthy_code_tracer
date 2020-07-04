# M5Stack_Healthy_code_tracer
:milky_way: Use M5GO to track healthy code/position/RFID/temperature by [ONENET](https://open.iot.10086.cn/devdoc/).
![ONENET](https://img-blog.csdnimg.cn/20200512224033117.png)

English version README : [README](https://github.com/haoruilee/M5Stack_Healthy_code_tracer/blob/master/README_EN.md) 

# How to use
- 你可以在Try_and_small_samples文件夹内找到一些小的、样例程序，他们是我开发这个项目的基础:wink:欢迎参考并进行二次开发
- 你可以在maixpy_qr文件夹中找到Unit-V识别二维码并进行串口通信的代码
- 所有的.py文件均可以在MicroPython1.11上上运行
 - 检查WIFI,Key是否匹配您的设备
 - 主控FINAL.py程序均在[UIflow 1.4.5](https://flow.m5stack.com/) 上测试通过
 - Remote程序在[在线IDE](https://flow.m5stack.com/)有时不稳定，建议下载至本地
 - FINAL.py为M5GO的主控程序
 - 请参考代码中的注释行进行运行

## Structure
![假设](https://img-blog.csdnimg.cn/20200515213214713.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjIzMzMyMw==,size_16,color_FFFFFF,t_70)

## Documents
 [CSDN教学文档](https://blog.csdn.net/weixin_46233323/article/details/106054434)
 万字长文:yum:保教包会
## Requirements
- (Base:) MIcropython  v1.11+
- (Core:) M5GO
- (Unit:) GPS、RFID、ENV、M5Camera
- (IDE:) Maixpy Ardunio

你可以在[UIFLOW Tutorial](https://docs.m5stack.com/#/en/uiflow/uiflow_home_page)下载M5Burner进行固件烧录。

![烧录界面](https://img-blog.csdnimg.cn/20200511000423632.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjIzMzMyMw==,size_16,color_FFFFFF,t_70)



# 成品效果
![成品](https://img-blog.csdnimg.cn/20200514235029301.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjIzMzMyMw==,size_16,color_FFFFFF,t_70)

# Contributers
**- :ok_woman: If you want to use some codes, I would be grateful if you can mention somewhere in the README that you are building on top of the work**

**- if you have any licencing issues please let me know, I can put a friendly MIT**

[@haoruilee](https://github.com/haoruilee)

[@HibaraAI](https://github.com/DaiyangLuan)
