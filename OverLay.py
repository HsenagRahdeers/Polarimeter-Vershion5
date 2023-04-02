import csv
import matplotlib.pyplot as plt
import numpy as np

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
        for i in range(len(his_inten) - 1):
            if his_inten[i] == 6969:
                his_inten[i] = his_inten[i + 1]
        return his_angle, his_inten
    except FileNotFoundError:
        print("No such file found!")
        
def plot_mult():
    file1read = input("Please enter first file to plot:  ")  
    ang , inten1 = read_data(file1read)
    file2read = input("Please enter second file to plot:  ")  
    ang , inten2 = read_data(file2read)
    file3read = input("Please enter third file to plot:  ")  
    ang , inten3 = read_data(file3read)
    file4read = input("Please enter fourth file to plot:  ")  
    ang , inten4 = read_data(file4read)
    file5read = input("Please enter fifth file to plot:  ")  
    ang , inten5 = read_data(file5read)

    plt.plot(ang, inten1, color='r', label='00% Solution')
    plt.plot(ang, inten2, color='g', label='05% Solution')
    plt.plot(ang, inten3, color='m', label='10% Solution')
    plt.plot(ang, inten4, color='b', label='15% Solution')
    plt.plot(ang, inten5, color='k', label='20% Solution')
    
    plt.xlabel('Angles')
    plt.ylabel('Intensities')
    plt.ylim([0.9*min(inten5), 1.1*max(inten1)])
    plt.xlim([min(ang) - 5, max(ang) + 5])

    plt.title('Polarimeter V5')
    plt.legend()

    manager = plt.get_current_fig_manager()
    plt.show() 
  
plot_mult()



