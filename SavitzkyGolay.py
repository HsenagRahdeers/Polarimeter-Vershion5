import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

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

def read_data(old_file):
    try:
        his_angle = []
        his_inten = []   
        with open(old_file + '.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                his_angle.append(float(row[0]))  
                his_inten.append(float(row[1]))
        fil_inten = savgol_filter(his_inten, 51, 3)
        return his_angle, his_inten, fil_inten
    except FileNotFoundError:
        print("No such file found!")

def write_data(new_file, angles, intensities):
    try:
        with open(new_file + ".csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ANGLES', 'INTENSITIES'])
            for i in range(len(angles) - 1):
                writer.writerow([angles[i], intensities[i]])
        print("Data Successfully Written!")                       
    except NameError:
        print("Task Failed Successfully!")
        
def plot_data(ang, inten):
    min_ix = find_min_index(inten)
    min_vl = ang[min_ix]
    max_ix = find_max_index(inten)
    max_vl = ang[max_ix]

    plt.plot(ang, inten)
    plt.xlabel('Angles')
    plt.ylabel('Intensities')
    plt.ylim([0.9*min(inten), 1.1*max(inten)])
    plt.xlim([min(ang) - 5, max(ang) + 5])
    plt.axvline(x = min_vl, color = 'g', label = 'Min Val =' + str(min_vl));
    plt.axvline(x = max_vl, color = 'r', label = 'Max Val =' + str(max_vl));
    plt.title('Polarimeter V5')
    plt.legend()

    manager = plt.get_current_fig_manager()
    plt.show() 

filename = input("Enter filename (to read):")
ang, unfilin, filin = read_data(filename)
plot_data(ang, unfilin)
plot_data(ang, filin)
wrtname = input("Enter filename (to write):")
write_data(wrtname, ang, filin)


