import sys
import Connection
import sensortype
import autocal
import datetime
from threading import Thread

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

host = "192.168.111.222"
port = 502

sp_list = None
mas_stb_time = None
fur_stb_time = None
standard_mas_std = None
mas_temp_diff = None

c = 0

controller = Connection.FloatModbusClient(
    host, port, unit_id=1, auto_open=True)

def show_temperature():
    ch1_temp.set(str(controller.read_float(33280,1)))
    ch2_temp.set(str(controller.read_float(33288,1)))
    ch3_temp.set(str(controller.read_float(33296,1)))
    ch4_temp.set(str(controller.read_float(33304,1)))
    if(c == 0):
        root.after(1000, show_temperature)



def exit_function():
    c = 1
    # controller.close()
    root.destroy()
    sys.exit()


root = Tk()

host = StringVar()
var = StringVar()
message_var = StringVar()
mas_std_var = StringVar()
mas_temp_var = StringVar()
sensor_var = StringVar()
sensor_type_var1 = StringVar()
sensor_type_var2 = StringVar()
sensor_type_var3 = StringVar()
sensor_type_var4 = StringVar()
ch1_temp = StringVar()
ch2_temp = StringVar()
ch3_temp = StringVar()
ch4_temp = StringVar()

sensor_type = 'T/C', 'RTD'
sensor_var.set('T/C')

root.geometry("601x403+429+141")
root.resizable(width=False, height=False)
root.title("Temperature")
root.configure(background="#94bfff")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")


def clear_message():
    message_var.set("")


ch_label_frame = LabelFrame(root)
ch_label_frame.place(relx=0.02, rely=0.10, relheight=0.10, relwidth=0.97)
ch_label_frame.configure(relief=FLAT)
ch_label_frame.configure(foreground="black")
ch_label_frame.configure(background="#94bfff")
ch_label_frame.configure(highlightbackground="#d9d9d9")
ch_label_frame.configure(highlightcolor="black")
ch_label_frame.configure(width=580)

ch1_label = Label(root)
ch1_label.place(relx=0.05, rely=0.06, height=22, width=84, y=-11, h=15)
ch1_label.configure(background="#94bfff")
ch1_label.configure(disabledforeground="#a3a3a3")
ch1_label.configure(foreground="#000000")
ch1_label.configure(text='''Channel 1''')
ch1_label.configure(width=84)

ch2_label = Label(root)
ch2_label.place(relx=0.29, rely=0.06, height=22, width=84, y=-11, h=15)
ch2_label.configure(background="#94bfff")
ch2_label.configure(disabledforeground="#a3a3a3")
ch2_label.configure(foreground="#000000")
ch2_label.configure(text='''Channel 2''')
ch2_label.configure(width=84)

ch3_label = Label(root)
ch3_label.place(relx=0.53, rely=0.06, height=22, width=84, y=-11, h=15)
ch3_label.configure(background="#94bfff")
ch3_label.configure(disabledforeground="#a3a3a3")
ch3_label.configure(foreground="#000000")
ch3_label.configure(text='''Channel 3''')
ch3_label.configure(width=84)

ch4_label = Label(root)
ch4_label.place(relx=0.77, rely=0.06, height=22, width=84, y=-11, h=15)
ch4_label.configure(background="#94bfff")
ch4_label.configure(disabledforeground="#a3a3a3")
ch4_label.configure(foreground="#000000")
ch4_label.configure(text='''Channel 4''')
ch4_label.configure(width=84)

ch1_temp_label = Label(root)
ch1_temp_label.place(relx=0.03, rely=0.12, height=21, width=124)
ch1_temp_label.configure(activebackground="#f9f9f9")
ch1_temp_label.configure(activeforeground="black")
ch1_temp_label.configure(background="#c9e2ff")
ch1_temp_label.configure(disabledforeground="#a3a3a3")
ch1_temp_label.configure(foreground="#000000")
ch1_temp_label.configure(highlightbackground="#d9d9d9")
ch1_temp_label.configure(highlightcolor="black")
ch1_temp_label.configure(textvariable=ch1_temp)

ch2_temp_label = Label(root)
ch2_temp_label.place(relx=0.27, rely=0.12, height=21, width=124)
ch2_temp_label.configure(activebackground="#f9f9f9")
ch2_temp_label.configure(activeforeground="black")
ch2_temp_label.configure(background="#c9e2ff")
ch2_temp_label.configure(disabledforeground="#a3a3a3")
ch2_temp_label.configure(foreground="#000000")
ch2_temp_label.configure(highlightbackground="#d9d9d9")
ch2_temp_label.configure(highlightcolor="black")
ch2_temp_label.configure(textvariable=ch2_temp)

ch3_temp_label = Label(root)
ch3_temp_label.place(relx=0.5, rely=0.12, height=21, width=124)
ch3_temp_label.configure(activebackground="#f9f9f9")
ch3_temp_label.configure(activeforeground="black")
ch3_temp_label.configure(background="#c9e2ff")
ch3_temp_label.configure(disabledforeground="#a3a3a3")
ch3_temp_label.configure(foreground="#000000")
ch3_temp_label.configure(highlightbackground="#d9d9d9")
ch3_temp_label.configure(highlightcolor="black")
ch3_temp_label.configure(textvariable=ch3_temp)

ch4_temp_label = Label(root)
ch4_temp_label.place(relx=0.73, rely=0.12, height=21, width=124)
ch4_temp_label.configure(activebackground="#f9f9f9")
ch4_temp_label.configure(activeforeground="black")
ch4_temp_label.configure(background="#c9e2ff")
ch4_temp_label.configure(disabledforeground="#a3a3a3")
ch4_temp_label.configure(foreground="#000000")
ch4_temp_label.configure(highlightbackground="#d9d9d9")
ch4_temp_label.configure(highlightcolor="black")
ch4_temp_label.configure(textvariable=ch4_temp)

Frame1 = Frame(root)
Frame1.place(relx=0.02, rely=0.22, relheight=0.33, relwidth=0.96)
Frame1.configure(relief=RIDGE)
Frame1.configure(borderwidth="2")
Frame1.configure(background="#94bfff")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=575)
"""
Frame2 = Frame(Frame1)
Frame2.place(relx=0.02, rely=0.07, relheight=0.85, relwidth=0.13)
Frame2.configure(borderwidth="2")
Frame2.configure(background="#94bfff")
Frame2.configure(highlightbackground="#d9d9d9")
Frame2.configure(highlightcolor="black")
Frame2.configure(width=75)

tc_radiobutton = Radiobutton(
    Frame2, text='T/C', variable=sensor_var, value='T/C')
tc_radiobutton.place(relx=0.13, rely=0.09, relheight=0.22, relwidth=0.64)
tc_radiobutton.configure(activebackground="#94bff0")
tc_radiobutton.configure(activeforeground="#000000")
tc_radiobutton.configure(background="#94bfff")
tc_radiobutton.configure(disabledforeground="#a3a3a3")
tc_radiobutton.configure(foreground="#000000")
tc_radiobutton.configure(highlightbackground="#d9d9d9")
tc_radiobutton.configure(highlightcolor="black")
tc_radiobutton.configure(justify=LEFT)

rtd_radiobutton = Radiobutton(
    Frame2, text='RTD', variable=sensor_var, value='RTD')
rtd_radiobutton.place(relx=0.13, rely=0.43, relheight=0.22, relwidth=0.67)
rtd_radiobutton.configure(activebackground="#d9d9d9")
rtd_radiobutton.configure(activeforeground="#000000")
rtd_radiobutton.configure(background="#94bfff")
rtd_radiobutton.configure(disabledforeground="#a3a3a3")
rtd_radiobutton.configure(foreground="#000000")
rtd_radiobutton.configure(highlightbackground="#d9d9d9")
rtd_radiobutton.configure(highlightcolor="black")
rtd_radiobutton.configure(justify=LEFT)"""

fur_stb_time_combo = ttk.Combobox(Frame1, values=('1 Minute', '2 Minutes', '3 Minutes',
                                                  '4 Minutes', '5 Minutes', '6 Minutes', '7 Minutes', '8 Minutes', '9 Minutes', '10 Minutes'))
fur_stb_time_combo.set('1 Minute')
fur_stb_time_combo.place(relx=0.71, rely=0.07, relheight=0.16, relwidth=0.14)
fur_stb_time_combo.configure(width=83)
fur_stb_time_combo.configure(background="#feffe8")
fur_stb_time_combo.configure(takefocus="")

fur_stb_time_label = Label(Frame1)
fur_stb_time_label.place(relx=0.45, rely=0.07, height=21, width=120)
fur_stb_time_label.configure(activebackground="#f9f9f9")
fur_stb_time_label.configure(activeforeground="black")
fur_stb_time_label.configure(background="#94bfff")
fur_stb_time_label.configure(disabledforeground="#a3a3a3")
fur_stb_time_label.configure(font="Helvetica 8 bold")
fur_stb_time_label.configure(foreground="#000000")
fur_stb_time_label.configure(highlightbackground="#d9d9d9")
fur_stb_time_label.configure(highlightcolor="black")
fur_stb_time_label.configure(justify=LEFT)
fur_stb_time_label.configure(text='''Furnace Stability Time''')
fur_stb_time_label.configure(width=114)

mas_stb_time_label = Label(Frame1)
mas_stb_time_label.place(relx=0.45, rely=0.3, height=21, width=120)
mas_stb_time_label.configure(activebackground="#f9f9f9")
mas_stb_time_label.configure(activeforeground="black")
mas_stb_time_label.configure(background="#94bfff")
mas_stb_time_label.configure(disabledforeground="#a3a3a3")
mas_stb_time_label.configure(font="Helvetica 8 bold")
mas_stb_time_label.configure(foreground="#000000")
mas_stb_time_label.configure(highlightbackground="#d9d9d9")
mas_stb_time_label.configure(highlightcolor="black")
mas_stb_time_label.configure(justify=LEFT)
mas_stb_time_label.configure(text='''Master Stability Time''')
mas_stb_time_label.configure(width=114)

mas_temp_label = Label(Frame1)
mas_temp_label.place(relx=0.45, rely=0.52, height=21, width=120)
mas_temp_label.configure(activebackground="#f9f9f9")
mas_temp_label.configure(activeforeground="black")
mas_temp_label.configure(background="#94bfff")
mas_temp_label.configure(disabledforeground="#a3a3a3")
mas_temp_label.configure(font="Helvetica 8 bold")
mas_temp_label.configure(foreground="#000000")
mas_temp_label.configure(highlightbackground="#d9d9d9")
mas_temp_label.configure(highlightcolor="black")
mas_temp_label.configure(text='''Master Temp (+/-)''')
mas_temp_label.configure(width=114)

mas_stddev_label = Label(Frame1)
mas_stddev_label.place(relx=0.45, rely=0.74, height=21, width=120)
mas_stddev_label.configure(activebackground="#f9f9f9")
mas_stddev_label.configure(activeforeground="black")
mas_stddev_label.configure(background="#94bfff")
mas_stddev_label.configure(disabledforeground="#a3a3a3")
mas_stddev_label.configure(font="Helvetica 8 bold")
mas_stddev_label.configure(foreground="#000000")
mas_stddev_label.configure(highlightbackground="#d9d9d9")
mas_stddev_label.configure(highlightcolor="black")
mas_stddev_label.configure(text='''Master Std Dev''')
mas_stddev_label.configure(width=114)

mas_stb_time_combo = ttk.Combobox(Frame1, values=('1 Minute', '2 Minutes', '3 Minutes',
                                                  '4 Minutes', '5 Minutes', '6 Minutes', '7 Minutes', '8 Minutes', '9 Minutes', '10 Minutes'))
mas_stb_time_combo.set('1 Minute')
mas_stb_time_combo.place(relx=0.71, rely=0.3, relheight=0.16, relwidth=0.14)
mas_stb_time_combo.configure(width=83)
mas_stb_time_combo.configure(background="#feffe8")
mas_stb_time_combo.configure(takefocus="")


def set_type_command():
    global fur_stb_time
    fur_stb_time = fur_stb_time_combo.get()
    global mas_stb_time
    mas_stb_time = mas_stb_time_combo.get()
    global mas_temp_diff
    mas_temp_diff = mas_temp_entry.get()
    global standard_mas_std
    standard_mas_std = mas_std_entry.get()
    for child in Frame1.winfo_children():
        child.configure(state='disabled')
    for child in Frame3.winfo_children():
        child.configure(state='normal')
    reset_type_button.configure(state='normal')


set_type_button = Button(Frame1, command=set_type_command)
set_type_button.place(relx=0.89, rely=0.22, height=24, width=47)
set_type_button.configure(activebackground="#d9d9d9")
set_type_button.configure(activeforeground="#000000")
set_type_button.configure(background="#ffc7ff")
set_type_button.configure(disabledforeground="#a3a3a3")
set_type_button.configure(foreground="#000000")
set_type_button.configure(highlightbackground="#d9d9d9")
set_type_button.configure(highlightcolor="black")
set_type_button.configure(pady="0")
set_type_button.configure(text='''Set''')


def reset_type_command():
    global fur_stb_time
    fur_stb_time = None
    global mas_stb_time
    mas_stb_time = None
    global mas_temp_diff
    mas_temp_diff = None
    global standard_mas_std
    standard_mas_std = None
    for child in Frame1.winfo_children():
        child.configure(state='normal')
    for child in Frame3.winfo_children():
        child.configure(state='disabled')
    set_type_button.configure(state='normal')


reset_type_button = Button(Frame1, command=reset_type_command)
reset_type_button.place(relx=0.89, rely=0.59, height=24, width=47)
reset_type_button.configure(activebackground="#d9d9d9")
reset_type_button.configure(activeforeground="#000000")
reset_type_button.configure(background="#abffae")
reset_type_button.configure(disabledforeground="#a3a3a3")
reset_type_button.configure(foreground="#000000")
reset_type_button.configure(highlightbackground="#d9d9d9")
reset_type_button.configure(highlightcolor="black")
reset_type_button.configure(pady="0")
reset_type_button.configure(text='''Reset''')

mas_temp_entry = Entry(Frame1)
mas_temp_entry.place(relx=0.71, rely=0.52, height=20, relwidth=0.15)
mas_temp_entry.configure(background="white")
mas_temp_entry.configure(disabledforeground="#a3a3a3")
mas_temp_entry.configure(font="Helvetica 9")
mas_temp_entry.configure(foreground="#000000")
mas_temp_entry.configure(highlightbackground="#d9d9d9")
mas_temp_entry.configure(highlightcolor="black")
mas_temp_entry.configure(insertbackground="black")
mas_temp_entry.configure(selectbackground="#c4c4c4")
mas_temp_entry.configure(selectforeground="black")
mas_temp_entry.configure(width=84)
mas_temp_entry.configure(textvariable=mas_temp_var)

mas_std_entry = Entry(Frame1)
mas_std_entry.place(relx=0.71, rely=0.74, height=20, relwidth=0.15)
mas_std_entry.configure(background="white")
mas_std_entry.configure(disabledforeground="#a3a3a3")
mas_std_entry.configure(font="Helvetica 9")
mas_std_entry.configure(foreground="#000000")
mas_std_entry.configure(highlightbackground="#d9d9d9")
mas_std_entry.configure(highlightcolor="black")
mas_std_entry.configure(insertbackground="black")
mas_std_entry.configure(selectbackground="#c4c4c4")
mas_std_entry.configure(selectforeground="black")
mas_std_entry.configure(width=84)
mas_std_entry.configure(textvariable=mas_std_var)

ch1_sensor_label = Label(Frame1)
ch1_sensor_label.place(relx=0.02, rely=0.07, height=21, width=74)
ch1_sensor_label.configure(activebackground="#94bfff")
ch1_sensor_label.configure(activeforeground="black")
ch1_sensor_label.configure(background="#94bfff")
ch1_sensor_label.configure(disabledforeground="#a3a3a3")
ch1_sensor_label.configure(font="Helvetica 8 bold")
ch1_sensor_label.configure(foreground="#000000")
ch1_sensor_label.configure(highlightbackground="#d9d9d9")
ch1_sensor_label.configure(highlightcolor="black")
ch1_sensor_label.configure(justify=LEFT)
ch1_sensor_label.configure(text='''Channel 1''')
ch1_sensor_label.configure(width=74)

ch2_sensor_label = Label(Frame1)
ch2_sensor_label.place(relx=0.02, rely=0.3, height=21, width=74)
ch2_sensor_label.configure(activebackground="#f9f9f9")
ch2_sensor_label.configure(activeforeground="black")
ch2_sensor_label.configure(background="#94bfff")
ch2_sensor_label.configure(disabledforeground="#a3a3a3")
ch2_sensor_label.configure(font="Helvetica 8 bold")
ch2_sensor_label.configure(foreground="#000000")
ch2_sensor_label.configure(highlightbackground="#d9d9d9")
ch2_sensor_label.configure(highlightcolor="black")
ch2_sensor_label.configure(justify=LEFT)
ch2_sensor_label.configure(text='''Channel 2''')
ch2_sensor_label.configure(width=74)

ch3_sensor_label = Label(Frame1)
ch3_sensor_label.place(relx=0.02, rely=0.52, height=21, width=74)
ch3_sensor_label.configure(activebackground="#f9f9f9")
ch3_sensor_label.configure(activeforeground="black")
ch3_sensor_label.configure(background="#94bfff")
ch3_sensor_label.configure(disabledforeground="#a3a3a3")
ch3_sensor_label.configure(font="Helvetica 8 bold")
ch3_sensor_label.configure(foreground="#000000")
ch3_sensor_label.configure(highlightbackground="#d9d9d9")
ch3_sensor_label.configure(highlightcolor="black")
ch3_sensor_label.configure(justify=LEFT)
ch3_sensor_label.configure(text='''Channel 3''')
ch3_sensor_label.configure(width=74)

ch4_sensor_label = Label(Frame1)
ch4_sensor_label.place(relx=0.02, rely=0.74, height=21, width=74)
ch4_sensor_label.configure(activebackground="#f9f9f9")
ch4_sensor_label.configure(activeforeground="black")
ch4_sensor_label.configure(background="#94bfff")
ch4_sensor_label.configure(disabledforeground="#a3a3a3")
ch4_sensor_label.configure(font="Helvetica 8 bold")
ch4_sensor_label.configure(foreground="#000000")
ch4_sensor_label.configure(highlightbackground="#d9d9d9")
ch4_sensor_label.configure(highlightcolor="black")
ch4_sensor_label.configure(justify=LEFT)
ch4_sensor_label.configure(text='''Channel 4''')
ch4_sensor_label.configure(width=74)

ch1_sensortype_label = Label(Frame1)
ch1_sensortype_label.place(relx=0.17, rely=0.07, relheight=0.16, relwidth=0.17)
ch1_sensortype_label.configure(activebackground="#f9f9f9")
ch1_sensortype_label.configure(activeforeground="black")
ch1_sensortype_label.configure(background="#94bfff")
ch1_sensortype_label.configure(disabledforeground="#a3a3a3")
ch1_sensortype_label.configure(foreground="#000000")
ch1_sensortype_label.configure(highlightbackground="#d9d9d9")
ch1_sensortype_label.configure(highlightcolor="black")
ch1_sensortype_label.configure(text="Furnace")

ch2_sensortype_label = Label(Frame1)
ch2_sensortype_label.place(relx=0.17, rely=0.3, relheight=0.16, relwidth=0.17)
ch2_sensortype_label.configure(activebackground="#f9f9f9")
ch2_sensortype_label.configure(activeforeground="black")
ch2_sensortype_label.configure(background="#94bfff")
ch2_sensortype_label.configure(disabledforeground="#a3a3a3")
ch2_sensortype_label.configure(foreground="#000000")
ch2_sensortype_label.configure(highlightbackground="#d9d9d9")
ch2_sensortype_label.configure(highlightcolor="black")
ch2_sensortype_label.configure(text="Furnace")
ch2_sensortype_label.configure(textvariable=sensor_type_var2)

ch3_sensortype_label = Label(Frame1)
ch3_sensortype_label.place(relx=0.17, rely=0.52, relheight=0.16, relwidth=0.17)
ch3_sensortype_label.configure(activebackground="#f9f9f9")
ch3_sensortype_label.configure(activeforeground="black")
ch3_sensortype_label.configure(background="#94bfff")
ch3_sensortype_label.configure(disabledforeground="#a3a3a3")
ch3_sensortype_label.configure(foreground="#000000")
ch3_sensortype_label.configure(highlightbackground="#d9d9d9")
ch3_sensortype_label.configure(highlightcolor="black")
ch3_sensortype_label.configure(text="Furnace")
ch3_sensortype_label.configure(textvariable=sensor_type_var3)

ch4_sensortype_label = Label(Frame1)
ch4_sensortype_label.place(relx=0.17, rely=0.74, relheight=0.16, relwidth=0.17)
ch4_sensortype_label.configure(activebackground="#f9f9f9")
ch4_sensortype_label.configure(activeforeground="black")
ch4_sensortype_label.configure(background="#94bfff")
ch4_sensortype_label.configure(disabledforeground="#a3a3a3")
ch4_sensortype_label.configure(foreground="#000000")
ch4_sensortype_label.configure(highlightbackground="#d9d9d9")
ch4_sensortype_label.configure(highlightcolor="black")
ch4_sensortype_label.configure(text="Furnace")
ch4_sensortype_label.configure(textvariable=sensor_type_var4)


Frame3 = Frame(root)
Frame3.place(relx=0.02, rely=0.57, relheight=0.21, relwidth=0.96)
Frame3.configure(relief=RIDGE)
Frame3.configure(borderwidth="2")
Frame3.configure(background="#94bfff")
Frame3.configure(highlightbackground="#d9d9d9")
Frame3.configure(highlightcolor="black")
Frame3.configure(width=575)

sp1_entry = Entry(Frame3)
sp1_entry.place(relx=0.02, rely=0.59, height=20, relwidth=0.13)
sp1_entry.configure(background="white")
sp1_entry.configure(disabledforeground="#a3a3a3")
sp1_entry.configure(font="Helvetica 9")
sp1_entry.configure(foreground="#000000")
sp1_entry.configure(highlightbackground="#d9d9d9")
sp1_entry.configure(highlightcolor="black")
sp1_entry.configure(insertbackground="black")
sp1_entry.configure(selectbackground="#c4c4c4")
sp1_entry.configure(selectforeground="black")

sp2_entry = Entry(Frame3)
sp2_entry.place(relx=0.17, rely=0.59, height=20, relwidth=0.13)
sp2_entry.configure(background="white")
sp2_entry.configure(disabledforeground="#a3a3a3")
sp2_entry.configure(font="Helvetica 9")
sp2_entry.configure(foreground="#000000")
sp2_entry.configure(highlightbackground="#d9d9d9")
sp2_entry.configure(highlightcolor="black")
sp2_entry.configure(insertbackground="black")
sp2_entry.configure(selectbackground="#c4c4c4")
sp2_entry.configure(selectforeground="black")

sp3_entry = Entry(Frame3)
sp3_entry.place(relx=0.33, rely=0.59, height=20, relwidth=0.13)
sp3_entry.configure(background="white")
sp3_entry.configure(disabledforeground="#a3a3a3")
sp3_entry.configure(font="Helvetica 9")
sp3_entry.configure(foreground="#000000")
sp3_entry.configure(highlightbackground="#d9d9d9")
sp3_entry.configure(highlightcolor="black")
sp3_entry.configure(insertbackground="black")
sp3_entry.configure(selectbackground="#c4c4c4")
sp3_entry.configure(selectforeground="black")

sp4_entry = Entry(Frame3)
sp4_entry.place(relx=0.49, rely=0.59, height=20, relwidth=0.13)
sp4_entry.configure(background="white")
sp4_entry.configure(disabledforeground="#a3a3a3")
sp4_entry.configure(font="Helvetica 9")
sp4_entry.configure(foreground="#000000")
sp4_entry.configure(highlightbackground="#d9d9d9")
sp4_entry.configure(highlightcolor="black")
sp4_entry.configure(insertbackground="black")
sp4_entry.configure(selectbackground="#c4c4c4")
sp4_entry.configure(selectforeground="black")

sp5_entry = Entry(Frame3)
sp5_entry.place(relx=0.64, rely=0.59, height=20, relwidth=0.13)
sp5_entry.configure(background="white")
sp5_entry.configure(disabledforeground="#a3a3a3")
sp5_entry.configure(font="Helvetica 9")
sp5_entry.configure(foreground="#000000")
sp5_entry.configure(highlightbackground="#d9d9d9")
sp5_entry.configure(highlightcolor="black")
sp5_entry.configure(insertbackground="black")
sp5_entry.configure(selectbackground="#c4c4c4")
sp5_entry.configure(selectforeground="black")

sp_label = Label(Frame3)
sp_label.place(relx=0.02, rely=0.24, height=21, width=149)
sp_label.configure(activebackground="#f9f9f9")
sp_label.configure(activeforeground="black")
sp_label.configure(background="#94bfff")
sp_label.configure(disabledforeground="#a3a3a3")
sp_label.configure(foreground="#000000")
sp_label.configure(highlightbackground="#d9d9d9")
sp_label.configure(highlightcolor="black")
sp_label.configure(text='''Total Number of Set Points''')


def set_spstate(Event):
    num = sp_combo.get()
    sp5_entry.configure(state='normal')
    sp4_entry.configure(state='normal')
    sp3_entry.configure(state='normal')
    sp2_entry.configure(state='normal')
    sp1_entry.configure(state='normal')
    if(num == '1'):
        sp5_entry.configure(state='disabled')
        sp4_entry.configure(state='disabled')
        sp3_entry.configure(state='disabled')
        sp2_entry.configure(state='disabled')
    elif(num == '2'):
        sp5_entry.configure(state='disabled')
        sp4_entry.configure(state='disabled')
        sp3_entry.configure(state='disabled')
    elif(num == '3'):
        sp5_entry.configure(state='disabled')
        sp4_entry.configure(state='disabled')
    elif(num == '4'):
        sp5_entry.configure(state='disabled')


sp_combo = ttk.Combobox(Frame3)
sp_combo.place(relx=0.31, rely=0.24, relheight=0.25, relwidth=0.18)
sp_combo.configure(values=('1', '2', '3', '4', '5'))
sp_combo.set('5')
sp_combo.configure(takefocus="")
sp_combo.bind('<<ComboboxSelected>>', set_spstate)


def sp_set_command():
    global sp_list
    sp_list = []
    num = sp_combo.get()
    err = 0
    try:
        if(num == '1'):
            sp_list.append(float(sp1_entry.get()))
        elif(num == '2'):
            sp_list.append(float(sp1_entry.get()))
            sp_list.append(float(sp2_entry.get()))
        elif(num == '3'):
            sp_list.append(float(sp1_entry.get()))
            sp_list.append(float(sp2_entry.get()))
            sp_list.append(float(sp3_entry.get()))
        elif(num == '4'):
            sp_list.append(float(sp1_entry.get()))
            sp_list.append(float(sp2_entry.get()))
            sp_list.append(float(sp3_entry.get()))
            sp_list.append(float(sp4_entry.get()))
        elif(num == '5'):
            sp_list.append(float(sp1_entry.get()))
            sp_list.append(float(sp2_entry.get()))
            sp_list.append(float(sp3_entry.get()))
            sp_list.append(float(sp4_entry.get()))
            sp_list.append(float(sp5_entry.get()))
    except ValueError:
        err = 1
    
    if(err == 1):
        message_var.set("Enter valid Temperature values.")
        root.after(700,clear_message)
    elif(err == 0):
        message_var.set("Set Points are %s" % str(sorted(sp_list)))
        root.after(700, clear_message)
        sp1_entry.configure(state='disabled')
        sp2_entry.configure(state='disabled')
        sp3_entry.configure(state='disabled')
        sp4_entry.configure(state='disabled')
        sp5_entry.configure(state='disabled')
"""
    def sp_reset_command():
        sp1_entry.configure(state='normal')
        sp2_entry.configure(state='normal')
        sp3_entry.configure(state='normal')
        sp4_entry.configure(state='normal')
        sp5_entry.configure(state='normal')

"""
sp_set_button = Button(Frame3, command=sp_set_command)
sp_set_button.place(relx=0.52, rely=0.24, height=24, width=57)
sp_set_button.configure(activebackground="#d9d9d9")
sp_set_button.configure(activeforeground="#000000")
sp_set_button.configure(background="#ffc7ff")
sp_set_button.configure(disabledforeground="#a3a3a3")
sp_set_button.configure(foreground="#000000")
sp_set_button.configure(highlightbackground="#d9d9d9")
sp_set_button.configure(highlightcolor="black")
sp_set_button.configure(pady="0")
sp_set_button.configure(text='''Set''')
"""
sp_reset_button = Button(Frame3, command=sp_set_command)
sp_reset_button.place(relx=0.66, rely=0.24, height=24, width=57)
sp_reset_button.configure(activebackground="#d9d9d9")
sp_reset_button.configure(activeforeground="#000000")
sp_reset_button.configure(background="#abffae")
sp_reset_button.configure(disabledforeground="#a3a3a3")
sp_reset_button.configure(foreground="#000000")
sp_reset_button.configure(highlightbackground="#d9d9d9")
sp_reset_button.configure(highlightcolor="black")
sp_reset_button.configure(pady="0")
sp_reset_button.configure(text='''Reset''')
"""

def calibration():
    global result_list
    result_list = list(autocal.main(sp_list, mas_stb_time, fur_stb_time, standard_mas_std, mas_temp_diff))


cal_button = Button(Frame3, command=calibration)
cal_button.place(relx=0.8, rely=0.24, height=24, width=97)
cal_button.configure(activebackground="#d9d9d9")
cal_button.configure(activeforeground="#000000")
cal_button.configure(background="#ffc7ff")
cal_button.configure(disabledforeground="#a3a3a3")
cal_button.configure(foreground="#000000")
cal_button.configure(highlightbackground="#d9d9d9")
cal_button.configure(highlightcolor="black")
cal_button.configure(pady="0")
cal_button.configure(text='''Calibration''')
cal_button.configure(width=97)

def gen_report():
    t_now = str(datetime.datetime.now())
    filetype = '.txt'
    filename = t_now+filetype
    with open(filename,'w') as f:
        f.write("Standard Deviation list for Furnace Temperature: %i" %(result_list[0]))
        f.write("Standard Deviation list for Master Temperature: %i" %(result_list[1]))
        f.close()


gen_report_button = Button(Frame3,command=gen_report)
gen_report_button.place(relx=0.8, rely=0.59, height=24, width=96)
gen_report_button.configure(activebackground="#d9d9d9")
gen_report_button.configure(activeforeground="#000000")
gen_report_button.configure(background="#ffc7ff")
gen_report_button.configure(disabledforeground="#a3a3a3")
gen_report_button.configure(foreground="#000000")
gen_report_button.configure(highlightbackground="#d9d9d9")
gen_report_button.configure(highlightcolor="black")
gen_report_button.configure(pady="0")
gen_report_button.configure(text='''Generate Report''')

Frame4 = Frame(root)
Frame4.place(relx=0.02, rely=0.79, relheight=0.11, relwidth=0.96)
Frame4.configure(relief=RIDGE)
Frame4.configure(borderwidth="2")
Frame4.configure(background="#94bfff")
Frame4.configure(highlightbackground="#d9d9d9")
Frame4.configure(highlightcolor="black")
Frame4.configure(width=575)
"""
fur_stb_color_label = Label(Frame4)
fur_stb_color_label.place(relx=0.02, rely=0.22, height=21, width=50)
fur_stb_color_label.configure(activebackground="#f9f9f9")
fur_stb_color_label.configure(activeforeground="black")
fur_stb_color_label.configure(background="#ff0000")
fur_stb_color_label.configure(disabledforeground="#a3a3a3")
fur_stb_color_label.configure(foreground="#000000")
fur_stb_color_label.configure(highlightbackground="#d9d9d9")
fur_stb_color_label.configure(highlightcolor="black")
fur_stb_color_label.configure(text='''F''')

mas_stb_color_label = Label(Frame4)
mas_stb_color_label.place(relx=0.12, rely=0.22, height=21, width=50)
mas_stb_color_label.configure(activebackground="#f9f9f9")
mas_stb_color_label.configure(activeforeground="black")
mas_stb_color_label.configure(background="#ff0000")
mas_stb_color_label.configure(disabledforeground="#a3a3a3")
mas_stb_color_label.configure(foreground="#000000")
mas_stb_color_label.configure(highlightbackground="#d9d9d9")
mas_stb_color_label.configure(highlightcolor="black")
mas_stb_color_label.configure(text='''M''')
"""
exit_button = Button(Frame4, command=exit_function)
exit_button.place(relx=0.87, rely=0.22, height=24, width=67)
exit_button.configure(activebackground="#d9d9d9")
exit_button.configure(activeforeground="#000000")
exit_button.configure(background="#ff0000")
exit_button.configure(disabledforeground="#a3a3a3")
exit_button.configure(foreground="#000000")
exit_button.configure(highlightbackground="#d9d9d9")
exit_button.configure(highlightcolor="black")
exit_button.configure(pady="0")
exit_button.configure(text='''Exit''')

"""
ip_entry = Entry(Frame4)
ip_entry.place(relx=0.26, rely=0.22, height=20, relwidth=0.29)
ip_entry.configure(background="white")
ip_entry.configure(disabledforeground="#a3a3a3")
ip_entry.configure(font="Helvetica 9")
ip_entry.configure(foreground="#000000")
ip_entry.configure(insertbackground="black")
ip_entry.configure(textvariable=host)


def clear_message():
    message_var.set("")


def get_ip_addr():
    host = ip_entry.get()
    controller = Connection.FloatModbusClient(host, port, unit_id=1, auto_open=True)
    if host:
        for child in Frame1.winfo_children():
            child.configure(state='normal')
    message_var.set("Connected to %s" % (host))
    root.after(700, clear_message)


connect_button = Button(Frame4, command=get_ip_addr)
connect_button.place(relx=0.59, rely=0.22, height=24, width=56)
connect_button.configure(activebackground="#d9d9d9")
connect_button.configure(activeforeground="#000000")
connect_button.configure(background="#ffc7ff")
connect_button.configure(disabledforeground="#a3a3a3")
connect_button.configure(foreground="#000000")
connect_button.configure(highlightbackground="#d9d9d9")
connect_button.configure(highlightcolor="black")
connect_button.configure(pady="0")
connect_button.configure(text='''Connect''')"""

message = Message(root)
message.place(relx=0.02, rely=0.92, relheight=0.06, relwidth=0.97)
message.configure(background="#94bfcf")
message.configure(foreground="#000000")
message.configure(highlightbackground="#d9d9d9")
message.configure(highlightcolor="black")
message.configure(width=580)
message.configure(textvariable=message_var)

for child in Frame3.winfo_children():
    child.configure(state='disabled')



"""
sensor_type_var2.set(sensortype.sensortype(int(controller.read_coils(45324,8))))
sensor_type_var3.set(sensortype.sensortype(int(controller.read_coils(45580,8))))
sensor_type_var4.set(sensortype.sensortype(int(controller.read_coils(45836,8))))
"""
show_temperature()

root.mainloop()
