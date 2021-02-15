import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/cu.usbmodem141101', 9800, timeout=1)
cond = 0
'''def led_on_off():
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
ser.close()'''

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

# Read and record the data
data =[]                       # empty list to store the data
for i in range(20):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip() # remove \n and \r
    print("curr: ",string)
    if (isfloat(string)):
        flt = float(string)
    else:
        flt = 0
    #flt = float(string)        # convert string to float
    #print(flt)
    data.append(flt)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()

plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()