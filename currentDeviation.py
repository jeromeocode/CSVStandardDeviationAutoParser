import os
import csv
import statistics
import pdb
from numpy import genfromtxt
# pdb.set_trace()

array1 = []

directory = r"C:\Users\Nicoya-LT\Desktop\Python stuff\coolwhitespheres2"
for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".csv"):
			print(file)
			with open(file) as csvfile:
				dataReader = genfromtxt(file, delimiter=',')
				for row in dataReader:
					array1.append(row)
				print(statistics.stdev(array1)*1000000)
				array1=[]

wait = input("PRESS ENTER TO CONTINUE.")
