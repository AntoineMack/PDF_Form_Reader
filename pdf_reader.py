#RCCS Health Form mass data entry program


import pandas as pd
import re, csv
import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime as dt
from pdf2image import convert_from_path
'''
User uploads a folder of medical forms of specific type
App places desired data from coordinates to df
Exports to csv
'''

# Select form type variable within Django

### import MDL Submission Report
root = tk.Tk()
root.withdraw()
a = True

'''upload folder'''

while a == True:
    try:
        print("Upload form folder")
        form_dir = filedialog.askdirectory(title='Choose Upload Folder')
        print("Folder", form_dir, " has been Uploaded")

    except:
        a = False
    else:
        break

form_dir = form_dir.replace(os.sep,'/')

'''Create Folder for Converted PNG Files'''
now = dt.now().strftime("%H:%M:%S").replace(":","_")
png_dir_path = os.path.join(form_dir, "PNG_Converts "+ now)
os.mkdir(png_dir_path)
print(png_dir_path, " created!")

error_list = []
'''Convert Each pdf file to PNG'''
for pdf_file in os.listdir(form_dir):
    try:
        if os.path.isfile(os.path.join(form_dir, pdf_file)):
            to_convert = form_dir + '/' + pdf_file
            image = convert_from_path(to_convert, single_file = True, first_page =1,\
                last_page = 1 )
            image[0].save(png_dir_path+'/'+str(pdf_file) +'.png', 'PNG')
            print(pdf_file + " converted")
    except:
        add_error = str('error converting ' + pdf_file)
        print(add_error)
        error_list.append(add_error)
        pass

'''Saving error list to txt file'''
if len(error_list) > 0:
    with open(png_dir_path+'/'+' Error_list.txt', 'w') as err:
        for item in error_list:
            err.write("%s\n" % item)
else:
    pass

'''Print list of files in dir'''



#make folder for converted pdf forms
# while a == True:
#     try:
#         print("Upload form folder")
#         mdl = filedialog.askopenfilename()
#         print("Folder has been Uploaded")
#     except:
#         a = False
#     else:
#         break
