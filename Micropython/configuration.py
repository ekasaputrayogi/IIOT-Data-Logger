import machine

uart = machine.UART(2, 115200)
def open_config():
    f = open("config.txt", "r")
    config = f.read()
    config_split = config.splitlines()
    f.close()
    print(config_split)
    return config_split

def create_config():
    if uart.any() > 0:
        f = open("config.txt", "w")
        strMsg = uart.read()
        conf = f.write(strMsg)
        f.close()
        f = open("config.txt", "r")
        config = f.read()
        config_split = config.splitlines()
        f.close()
        return config_split
    else:
        pass

