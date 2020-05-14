import sensor
import image
import lcd
import time
from fpioa_manager import fm, board_info
from machine import UART
import utime


#初始化uart
#注册引脚
fm.register(35, fm.fpioa.UART2_RX, force=True)
fm.register(34, fm.fpioa.UART2_TX, force=True)
#初始化uart
uart_Port = UART(UART.UART2, 115200,8,0,0, timeout=1000, read_buf_len= 1024)

clock = time.clock()
lcd.init()#lcd显示
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.run(1)
sensor.skip_frames(30)
while True:
    clock.tick()
    img = sensor.snapshot()#获得图像
    res = img.find_qrcodes()#识别二维码
    fps =clock.fps()
    if len(res) > 0:
        #print((res[0].payload()))
        mystr=str(res[0].payload())
        #mystr = mystr.encode('UTF-8','ignore')
        #uart传输
        uart_Port.write(mystr)
        print(mystr)
        time.sleep(3)
    lcd.display(img)#显示图像
