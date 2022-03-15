from configuration import open_config
from machine import ADC, Pin

config = open_config()

#---Analog Pin Configuration---#

#PIN 0
pin0 = ADC(Pin(34))
pin0.atten(ADC.ATTN_11DB)
pin0.width(ADC.WIDTH_12BIT)
pin0_split = config[6].split()

def pin0_read():   
    pin0_ = pin0.read() 
    pin0_data = (int(pin0_split[5]) - int(pin0_split[4])/4095)*pin0_ + int(pin0_split[4])
    return pin0_data          