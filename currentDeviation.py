import os
import csv
import statistics
import pdb
from numpy import genfromtxt
# pdb.set_trace()

array1 = []

#change this directory path to the folder of CSVs you want to apply standard deviation
directory = r"C:\Users\Nicoya-LT\Desktop\Python stuff\THORNEWTEST"

#steps through folder and looks for csv files
for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".csv"):

			#outputs the file name
			print(file)

			with open(file) as csvfile:
				#changed the format of csv so that they have a header (if no header in your csv file, change to skip_header=0)
				dataReader = genfromtxt(file, delimiter=',', skip_header=1)

				#iterates through each row in the csv
				for row in dataReader:
					#row[1] is the column of data that I was using but you can change it to the first column by replacing it with row[0]
					array1.append(row[1])

				#prints the standard deviation (I multiplied by 1e6 because my deviations were relatively small, you can remove that)
				print(statistics.stdev(array1)*1000000)

				#clears array for the next file
				array1=[]

wait = input("PRESS ENTER TO CONTINUE.")
