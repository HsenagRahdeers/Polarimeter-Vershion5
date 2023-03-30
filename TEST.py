import serial
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

dev_cal_fact = 1.00
resAng = 0.225
calAng = []
intensities = []

root = tk.Tk()
root.title("Polarimeter V5")
root.configure(bg='black')

port_label = tk.Label(root, text="Port Name:",font=('Arial', 14), bg="black", fg="white")
port_entry = tk.Entry(root, font=('Arial', 14), width= 10, bg="gray")
start_button = tk.Button(root, text="Start", width= 10,  bg="green", fg="white", command=lambda: start_polarimeter(port_entry.get()))
exit_button = tk.Button(root, text="Exit",width= 10, bg="red", fg="white", command=lambda: close_all())
his_button = tk.Button(root, text="History",width= 10,  bg="blue", fg="white", command=lambda: file_history())
calib_button = tk.Button(root, text="Calibrate",width= 10,  bg="orange", fg="white", command=lambda: dev_calib())
status_label = tk.Label(root, text="Status: Not running",font=('Arial', 12), bg="black", fg="red")
write_button = tk.Button(root, text="Write Data",   bg="green", fg="white", command=lambda: write_data())

port_label.grid(row=0, column=0, padx=7, pady=5)
port_entry.grid(row=0, column=1, padx=7, pady=7)
his_button.grid(row=1, column=0, padx=5, pady=7)
calib_button.grid(row=1, column=1, padx=5, pady=7)
start_button.grid(row=2, column=0, padx=5, pady=7)
exit_button.grid(row=2, column=1, padx=5, pady=7)
status_label.grid(row=3, column=0, columnspan=2, padx=7, pady=7)
write_button.grid(row=4,column=0, columnspan=2, padx=5, pady=7)


def find_max_index(lst):
    max_idx = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx

def find_min_index(lst):
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_idx]:
            min_idx = i
    return min_idx

def dev_calib():
    plt.clf()
    calwin = tk.Tk()
    calwin.title("Device Calibration")
    calwin.configure(bg='black')
    
    msd_label = tk.Label(calwin, text="Msrd Value:",font=('Arial', 14), bg="black", fg="white")
    msd_entry = tk.Entry(calwin, font=('Arial', 14), width= 10, bg="gray")
    msd_label.grid(row=0, column=0, padx=5, pady=5)
    msd_entry.grid(row=0, column=1, padx=7, pady=7)

    act_label = tk.Label(calwin, text="True Value:",font=('Arial', 14), bg="black", fg="white")
    act_entry = tk.Entry(calwin, font=('Arial', 14), width= 10, bg="gray")
    act_label.grid(row=1, column=0, padx=5, pady=5)
    act_entry.grid(row=1, column=1, padx=7, pady=7)
    
    cal_button = tk.Button(calwin, text="Calibrate",width= 10, bg="blue", fg="white", command=lambda: do_cal())
    cal_cls_button = tk.Button(calwin, text="Done",width= 10, bg="green", fg="white", command=lambda: done_cal())
    cal_button.grid(row=3, column=0, padx=5, pady=7)
    cal_cls_button.grid(row=3, column=1, padx=5, pady=7)

    cal_status_label = tk.Label(calwin, text="Device Not Calibrated",font=('Arial', 16), bg="black", fg="blue")
    cal_status_label.grid(row=4, column=0, columnspan=2, padx=7, pady=7)

    def done_cal():
        calwin.destroy()
    
    def do_cal():
        try:
            av = float(act_entry.get())
            mv = float(msd_entry.get())
            dev_cal_fact = av/mv
            cal_status_label.config(fg = "green", text="Sucessfully Recalibrated!")
        except ValueError:
            cal_status_label.config(fg = "red", text="Try Again!")
    
    calwin.mainloop()
    
def view_old(old_file):
    try:
        his_angle = []
        his_inten = []
    
        with open(old_file + '.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                his_angle.append(float(row[0]))  
                his_inten.append(float(row[1]))
            
        min_ix = find_min_index(his_inten)
        min_vl = his_angle[min_ix]
        max_ix = find_max_index(his_inten)
        max_vl = his_angle[max_ix]

        plt.plot(his_angle, his_inten)
        plt.xlabel('Angles')
        plt.ylabel('Intensities')
        plt.ylim([10, 280])
        plt.xlim([min(his_angle) - 5, max(his_angle) + 5])
        plt.axvline(x = min_vl, color = 'g', label = 'Min Val =' + str(min_vl));
        plt.axvline(x = max_vl, color = 'r', label = 'Max Val =' + str(max_vl));
        plt.title(old_file)
        plt.legend()

        manager = plt.get_current_fig_manager()
        #manager.window.state('zoomed')

        plt.show()

    except FileNotFoundError:
        messagebox.showerror('No File Found', 'Unable to read ' + old_file + ':  No such file found!')

def file_history():
    his = tk.Tk()
    his.title("Old Files")
    his.configure(bg='black')

    def close_his():
        his.destroy()

    his_flname_label = tk.Label(his, text="File Name:",font=('Arial', 14), bg="black", fg="white")
    his_flname_entry = tk.Entry(his, font=('Arial', 14), width= 10, bg="gray")
    his_flname_label.grid(row=0, column=0, padx=7, pady=10)
    his_flname_entry.grid(row=0, column=1, padx=7, pady=10)

    read_button = tk.Button(his, text="Read File", width= 10,  bg="green", fg="white", command=lambda: view_old(his_flname_entry.get()))
    exit_button = tk.Button(his, text="Exit",width= 10, bg="red", fg="white", command=lambda: close_his())
    read_button.grid(row=1, column=0, padx=7, pady=10)
    exit_button.grid(row=1, column=1, padx=7, pady=10)

    his.mainloop()
        

def close_all():
    root.destroy()
    exit()

def write_data():
    wrt = tk.Tk()
    wrt.title("Data Writer")
    wrt.configure(bg='black')
    
    store_button = tk.Button(wrt, text="Write Data", width= 10,  bg="orange", fg="white", command=lambda: wrtr_fun())
    store_button.grid(row=2, column=3, columnspan=2, padx=5, pady=7)
    d_button = tk.Button(wrt, text="Done", width= 10,  bg="green", fg="white", command=lambda: close_wrtr())
    d_button.grid(row=2, column=0, padx=5, pady=7)

    name_label = tk.Label(wrt, text="Filename: ",font=('Arial', 14), bg="black", fg="white")
    name_entry = tk.Entry(wrt, font=('Arial', 14), width= 25, bg="gray")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry.grid(row=0, column=1, padx=7, pady=7)

    wrt_stat_label = tk.Label(wrt, text="Data Not Written", font=('Arial', 14), bg="black", fg="blue")
    wrt_stat_label.grid(row=1, column=0, columnspan=2, padx=7, pady=7)

    def close_wrtr():
        wrt.destroy()

    def wrtr_fun():
        try:
            with open(name_entry.get() + ".csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ANGLES', 'INTENSITIES'])
                for i in range(len(calAng)):
                    writer.writerow([calAng[i], intensities[i]])
            wrt_stat_label.config(fg = "green", text="Data Successfully Written!")
                        
        except NameError:
            wrt_stat_label.config(fg = "red", text="Task Failed Successfully!")
    wrt.mainloop()
    print("Successfully written!")
            

def start_polarimeter(portname):
    start_button.config(state=tk.DISABLED)
    status_label.config(text="Running...")
    
    ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 115200, timeout = 1)
    #ser.flushInput()

    global intensities
    global calAng
    global max_index
    global min_index
    
    def resCal(lst, cal, dcal):
        result = []
        for i in lst:
            result.append(i * cal * dcal)
        return result

    intensities = []

    ser.write(b'1')
    #ser.flushInput()

    while True: 
        fromArduino = ser.readline().decode().strip()
        print(fromArduino)
        if fromArduino == 'exit':
            ser.write(b'B')
            break
        else:
            try:
                intensities.append(float(fromArduino))
            except ValueError:
                intensities.append(6969)

    serAng = [i for i in range(len(intensities))]
    calAng = resCal(serAng, resAng, dev_cal_fact)

    print("Angles = ", serAng)
    print("Intensities = ",intensities)
    ser.close()

    min_index = find_min_index(intensities)
    min_val = calAng[min_index]
    max_index = find_max_index(intensities)
    max_val = calAng[max_index]

    plt.plot(calAng, intensities)
    plt.xlabel('Angles')
    plt.ylabel('Intensities')
    plt.ylim([10, 200])
    plt.xlim([min(calAng) - 5, max(calAng) + 5])
    plt.axvline(x = min_val, color = 'g', label = 'Min Val =' + str(min_val));
    plt.axvline(x = max_val, color = 'r', label = 'Max Val =' + str(max_val));
    plt.title('Polarimeter V5')
    plt.legend()

    manager = plt.get_current_fig_manager()
    #manager.window.state('zoomed')

    plt.show()

    status_label.config(text="Status: Not running")
    start_button.config(state=tk.NORMAL)

root.mainloop()



