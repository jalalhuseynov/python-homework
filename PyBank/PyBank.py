# Importing the pathlib and csv library

from pathlib import Path
import csv

# Setting the file path
csvpath = Path('budget_data.csv')

# Openning the csv file as an object

with open (csvpath, 'r') as csvfile:
    
    # csv file to the csv.reader() function

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Readding the header row
    csv_header = next(csvreader)
    
   
    #Initializing variables
    
    month_count = 0
    total_pnl = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    previous_month = 0
    total = 0
    month = 0
    
    #Initializing a list
    monthly_difference = []
    
    # Read each row of data after the header
    for row in csvreader:
     
        #number of months
        month_count = month_count + 1
        #total profit/loss calculation
        total_pnl += int(row[1])
        
        #checking month by month to calculate the avearage change
        if  row[0] == "Jan-2010":
            previous_month = int(row[1])
            month += 1
            total += int(row[1])
            greatest_increase = 0
            greatest_increase_month = row[0]
            greatest_decrease = 0
            greatest_decrease_month = row[0]
            
       #finding the greatest increase and the greates decrease
        else:
            month += 1
            total += int(row[1])
            monthly_difference.append(int(row[1])-previous_month)
            if (int(row[1]) - previous_month) > greatest_increase:
                greatest_increase = int(row[1]) -previous_month
                greatest_increase_month = row [0]
                
            if (int(row[1]) - previous_month) < greatest_decrease:
                greatest_decrease = int(row[1]) -previous_month
                greatest_decrease_month = row [0]
            
            previous_month = int(row[1])
            
    # Printing final results: total months, total pnl, avearage change, greatest increase and greatest decrease   
    print("Financial Analysis")
    print("_________________________")
    print(f"Total Months: {month_count}")
    print(f"Total PnL: ${total_pnl}")
    print(f"Average Change: {round(sum(monthly_difference)/len(monthly_difference), 2)} ")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    
# Setting output file name    
result_path = 'results.txt'

# Openning the output path as a file object
with open(result_path, 'w') as file:
    
    file.write("Financial Analysis")
    file.write("_________________________")
    file.write(f"Total Months: {month_count}")
    file.write(f"Total PnL: ${total_pnl}")
    file.write(f"Average Change: {round(sum(monthly_difference)/len(monthly_difference), 2)} ")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")