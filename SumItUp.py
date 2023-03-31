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
    plt.title('shit')
    plt.legend()

    manager = plt.get_current_fig_manager()
    plt.show() 
  
l0a1 , l0i1 = read_data('00per_sam1')
l0a2 , l0i2 = read_data('00per_sam2')
l0a3 , l0i3 = read_data('00per_sam3')
l0a4 , l0i4 = read_data('00per_sam4')
l0a5 , l0i5 = read_data('00per_sam5')
l0a = []
l0i = []
for j in range(len(l0a1)):
    l0a.append( l0a1[j])
    l0i.append( l0i1[j] + l0i2[j] + l0i3[j] + l0i4[j] + l0i5[j] )
plot_data(l0a, l0i) 
write_data('Sum00SolnNoFil',l0a, l0i)

l5a1 , l5i1 = read_data('05per_sam1')
l5a2 , l5i2 = read_data('05per_sam2')
l5a3 , l5i3 = read_data('05per_sam3')
l5a4 , l5i4 = read_data('05per_sam4')
l5a5 , l5i5 = read_data('05per_sam5')
l5a = []
l5i = []
for j in range(len(l5a1)):
    l5a.append( l5a1[j])
    l5i.append( l5i1[j] + l5i2[j] + l5i3[j] + l5i4[j] + l5i5[j] )
plot_data(l5a, l5i) 
write_data('Sum05SolnNoFil',l5a, l5i)

l10a1 , l10i1 = read_data('10per_sam1')
l10a2 , l10i2 = read_data('10per_sam2')
l10a3 , l10i3 = read_data('10per_sam3')
l10a4 , l10i4 = read_data('10per_sam4')
l10a5 , l10i5 = read_data('10per_sam5')
l10a = []
l10i = []
for j in range(len(l10a1)):
    l10a.append( l10a1[j])
    l10i.append( l10i1[j] + l10i2[j] + l10i3[j] + l10i4[j] + l10i5[j] )
plot_data(l10a, l10i) 
write_data('Sum10SolnNoFil',l10a, l10i)

l15a1 , l15i1 = read_data('15per_sam1')
l15a2 , l15i2 = read_data('15per_sam2')
l15a3 , l15i3 = read_data('15per_sam3')
l15a4 , l15i4 = read_data('15per_sam4')
l15a5 , l15i5 = read_data('15per_sam5')
l15a = []
l15i = []
for j in range(len(l15a1)):
    l15a.append( l15a1[j])
    l15i.append( l15i1[j] + l15i2[j] + l15i3[j] + l15i4[j] + l15i5[j] )
plot_data(l15a, l15i) 
write_data('Sum15SolnNoFil',l15a, l15i)

l20a1 , l20i1 = read_data('20per_sam1')
l20a2 , l20i2 = read_data('20per_sam2')
l20a3 , l20i3 = read_data('20per_sam3')
l20a4 , l20i4 = read_data('20per_sam4')
l20a5 , l20i5 = read_data('20per_sam5')
l20a = []
l20i = []
for j in range(len(l20a1)):
    l20a.append( l20a1[j])
    l20i.append( l20i1[j] + l20i2[j] + l20i3[j] + l20i4[j] + l20i5[j] )
plot_data(l20a, l20i) 
write_data('Sum20SolnNoFil',l20a, l20i)


