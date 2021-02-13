import serial
import time
ser = serial.Serial('/dev/cu.usbmodem141101', 9800, timeout=1)
cond = 0
def led_on_off():
    data = ser.readline()[:-2]  # the last bit gets rid of the new-line chars
    if data:
        print(data)
    user_input = input("\n Type on / off / quit : ")
    if user_input =="on":
        print("LED is on...")
        time.sleep(0.1)
        val = '1'
        ser.write(val.encode("utf-8"))
        led_on_off()
    elif user_input =="off":
        print("LED is off...")
        time.sleep(0.1)
        val = '0'
        print(val.encode("utf-8"))
        ser.write(val.encode("utf-8"))
        led_on_off()
    elif user_input =="quit" or user_input == "q":
        print("Program Exiting")
        time.sleep(0.1)
        cond = 1
    else:
        print("Invalid input. Type on / off / quit.")
        led_on_off()
        cond = 1

time.sleep(2) # wait for the serial connection to initialize

led_on_off()
ser.close()