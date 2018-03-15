# CSVStandardDeviationAutoParser
To analyze data, it is required to take the current deviation of different time intervals that come in the form of .CSV files. These .CSV files are from [RigolDM3058ECurrentRecording] (https://github.com/jeromeocode/RigolDM3058ECurrentRecording) with the data listed as a long single column.

# How it works
Steps through the directory specified in the code. For every .CSV file in the directory, it calculates the sample standard deviation of all the data in the file and outputs it to the console alongside the name of the file.
