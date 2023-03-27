import os
import shutil
import matplotlib.pyplot as plt

# Set the source path of the files you want to copy
source_path = "C:\\Users\\12243\\Desktop\\miscut_data_process"  # source data file path

# Set the destination path for the copied files
destination_path = "C:\\Users\\12243\\Desktop\\miscut_data_process\\ras_file_folder" # all copied ras data files

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_path):
   os.makedirs(destination_path)

# Loop through each file in the source directory
for file_name in os.listdir(source_path):

   # Check if the file is a ras file (.ras extension)
   if file_name.endswith(".ras"):

       # Build the full path of the file
       file_path = os.path.join(source_path, file_name)

       # Copy the file to the destination directory
       shutil.copy(file_path, destination_path)

       #print(f"File {file_name} copied to {destination_path}")  #copy all ras file to data process folder



files= os.listdir(destination_path) #obtain all file name in the specific folder





offset = 0.04  # measurement offset
phi_step = int(input('phi interval :'))
import xrayutilities as xu
#data = xu.io.rigaku_ras.RASFile('YBT005_103_RSM.ras', path ="C:\\Users\\12243\\Desktop\\file name change" )
from matplotlib.pylab import *


f = figure(figsize=(7, 5))
i = 0
phi_list = []
omega_list_real = []
for file_name in files:

    phi = phi_step *i
    phi_list.append(phi)
    d = xu.io.RASFile(file_name, path=source_path)
    scan = d.scans[-1]
    tt = scan.data[scan.scan_axis] - offset # scan angle
    #print(tt)
    #print(scan.data['int']) #scan data
    max_intensity = max(scan.data['int'])  # find the highest intensity
    max_index = np.where(scan.data['int']==max_intensity)[0][0]  # find the index of the highest intensity
    max_position = tt[max_index]  # find the position corresponding to the highest intensity
    omega_list_real.append(max_position)
    i = i + 1

    # print(max_position)
    # semilogy(tt, scan.data['int'], 'o-', ms=3, label='data')
    # show()
# print(type(omega_list_real))
# print(phi_list)
plt.plot(phi_list,omega_list_real,'*-',label='miscut')
plt.xlabel('phi')
plt.ylabel('omega')
plt.legend()
#semilogy(phi_list, omega_list_real, 'o-', ms=3, label='data')
show()
