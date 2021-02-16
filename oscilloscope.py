import tkinter as tk
from tkinter import *
from tkinter import ttk
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import threading
matplotlib.use("TkAgg")
LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

global connected, ser
connected = 0

data_string = ""
xs = [i for i in range(10)]
ys = []
global data
data = []

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def connect():
  global connected,ser
  ser = serial.Serial('/dev/cu.usbmodem141101', 9800, timeout=1)
  connected = 1
  print("hi")

def close():
  global connected,ser
  ser.close()
  connected = 0
  print("bye")

def animate(i):
  print("Start animation!")
  global data
  if (connected==0):
    return

  b = ser.readline()  # read a byte string
  string_n = b.decode()  # decode byte string into Unicode
  string = string_n.rstrip()  # remove \n and \r
  print("curr: ", string)
  if (isfloat(string)):
    flt = float(string)
  else:
    flt = 0
  data.append(flt)
  ax.clear()
  ax.grid()
  ax.plot(range(len(data)), data, marker='o', color='orange')
  time.sleep(0.2)

def data_loader(data):
  b = ser.readline()  # read a byte string
  string_n = b.decode()  # decode byte string into Unicode
  string = string_n.rstrip()  # remove \n and \r
  print("curr: ", string)
  if (isfloat(string)):
    flt = float(string)
  else:
    flt = 0
  data.append(flt)
  return data

def show():
  print("Connected: ", connected)

def plot():
  dpts = []
  while connected:
    ax.clear()
    ax.grid()
    dpts = data_loader(dpts)
    ax.plot(range(len(dpts)), dpts, marker='o', color='orange')
    #graph.draw()

    time.sleep(0.1)

    if(len(dpts)>20):
      return

def plotter():
  print("Start plotting")
  global data
  data = []

  graph = FigureCanvasTkAgg(fig, master=page)
  graph.get_tk_widget().grid(row=2, column=1, padx=10, pady=5)
  graph.draw()

  toolbarFrame = Frame(master=page)
  toolbarFrame.grid(row=3, column=1)
  toolbar = NavigationToolbar2Tk(graph, toolbarFrame)
  toolbar.update()


page = tk.Tk()
page.title("Oscilloscope")

button_1 = tk.Button(page,text="Connect",width=10,command=connect).grid(row=0,column=0,sticky=tk.W,padx=10,pady=5)
button_2 = tk.Button(page,text="Close",width=10,command=close).grid(row=0,column=1,padx=10,pady=5)
button_3 = tk.Button(page,text="Show Connection",width=10,command=show).grid(row=0,column=2,padx=10,pady=5)

lab = Label(page, text="Live Plotting").grid(row=1,column=1,padx=10,pady=5)
button_4 = tk.Button(page,text="Start Plotting",width=10,command=plotter).grid(row=1,column=2,padx=10,pady=5)
button_5 = tk.Button(page,text="Stop Plotting",width=10,command=close).grid(row=2,column=2,padx=10,pady=5)
fig = Figure()
ax = fig.add_subplot(111)
ax.set_xlabel("Voltage")
ax.set_ylabel("Time")
ax.grid()
ani = animation.FuncAnimation(fig, animate, interval=200)


page.mainloop()