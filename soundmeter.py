import usb.core
import usb.util
import random
import time

class soundmeter:
    def __init__(self): 
        #connect to Digital Sound Level Meter
        self.dev = usb.core.find(idVendor=0x64bd, idProduct=0x74e3)

        if self.dev == None:
            print("no Sound Meter found!")
            exit()

        if self.dev.is_kernel_driver_active(0):
            self.dev.detach_kernel_driver(0)
        usb.util.claim_interface(self.dev, 0)

        self.eout = self.dev[0][(0,0)][0]
        self.ein  = self.dev[0][(0,0)][1]

        self.STATE_REQUEST = bytearray([0xb3, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 0, 0, 0, 0])
        self.dev.read(self.ein.bEndpointAddress, self.ein.wMaxPacketSize) #clear buffer

    def get_spl(self):
        self.dev.write(self.eout.bEndpointAddress, self.STATE_REQUEST)
        time.sleep(0.1)
        buffer = []

        while True:
            #print("read")
            buffer += self.dev.read(self.ein.bEndpointAddress, self.ein.wMaxPacketSize)
            if len(buffer) == 8:
                break

        #print(buffer)
        return (buffer[0]*256 + buffer[1])/10


if __name__ == "__main__":
    sound = soundmeter()
    while True:
        print(sound.get_spl())
