# CSVStandardDeviationAutoParser

To analyze data, it is required to take the current deviation of different time intervals that come in the form of .CSV files. These .CSV files are from [RigolDM3058ECurrentRecording](https://github.com/jeromeocode/RigolDM3058ECurrentRecording) with the data listed as a long single column.

## How it works

Steps through the directory specified in the code. For every .CSV file in the directory, it calculates the sample standard deviation of all the data in the file and outputs it to the console alongside the name of the file.

## How to use it

- Change the code so that it will read the folder of CSV files that you want

```python
#change this directory path to the folder of CSVs you want to apply standard deviation
directory = r"C:\Users\Nicoya-LT\Desktop\Python stuff\THORNEWTEST"
```

-Run the program and it will display the sample standard deviation for you underneath the file name