import os
import csv
import statistics
import pdb
from numpy import genfromtxt
# pdb.set_trace()

array1 = []

directory = r"C:\Users\Nicoya-LT\Desktop\Python stuff\THORNEWTEST"
for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".csv"):
			print(file)
			with open(file) as csvfile:
				#changed the format of csv so that they have a header
				dataReader = genfromtxt(file, delimiter=',', skip_header=1)
				for row in dataReader:
					#row[1] contains the current data
					array1.append(row[1])
				print(statistics.stdev(array1)*1000000)
				array1=[]

wait = input("PRESS ENTER TO CONTINUE.")
