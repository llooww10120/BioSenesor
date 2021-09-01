import time
import Adafruit_DHT

GPIO_PIN=4
try:
    print('ctrl+c quit')
    while True:
        h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
        if h is not None and t is not None:
            print('temp={0:0.1f}C humid={1:0.1f}%'.format(t,h))
        else:
            print('error')
        time.sleep(10)
except KeyboardInterrupt:
    print('close')