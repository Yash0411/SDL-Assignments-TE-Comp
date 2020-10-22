# Yash Morankar
# TECOB220 

# import pandas
import pandas as pd

# Get data as dataframe form the given file
df =  pd.read_csv("month_temperature.csv")

# Check number of NaN in each column 
print("\n No. of NaNs for each day : ")
print(df.isna().sum())

# Get mean of each column
print("\n Average values for each day : ")
print(df.mean())

# Replace each NaN by its column mean
df.fillna(df.mean(),inplace=True)

# Declare max values, min values, average
month_min = 99999
month_max = -99999
month_sum = 0

print("\n Min, Max, Average values for each day : ")
for i in df.columns:
  print(f'{i}:- Min:{df[i].min()},  Max: {df[i].max()}, Average: {round(df[i].mean(),2)}')    # Print min, max, average of each column
  
  month_sum += round(df[i].mean(),2)    # Add mean to sum by rounding it off

  if df[i].min() < month_min:   
    month_min = df[i].min()     # change minimum value
  if df[i].max() > month_max:
    month_max = df[i].max()     # change maximum value

month_avg = month_sum/df.shape[1]     # Get average

# Print min, max and average temperature of the month
print('\n\nMin, Max And Average Temperature of the month:-')
print(f'Min: {month_min}\nMax: {month_max}\nAverage: {round(month_avg,2)}')