from pathlib import Path
import csv

csvpath = Path('budget_data.csv')

with open (csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
   
    #Initializing variables
    
    month_count = 0
    total_pnl = 0
    monthly_difference = []
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    previous_month = 0
    total = 0
    month = 0
    
    for row in csvreader:
     
        #number of months
        month_count += 1
        #total profit/loss calculation
        total_pnl += int(row[1])
        
        if row[0] == "Date":
            pass
        elif row[0] == "Jan-2010":
            previous_month = int(row[1])
            month_count += 1
            total += int(row[1])
            greatest_increase = 0
            greatest_increase_month = row[0]
            greatest_decrease = 0
            greatest_decrease_month = row[0]
        elif row[0] == "Feb-2010":
            greatest_increase = int(row[1]) - previous_month
            greatest_decrease = int(row[1]) - previous_month
            month += 1
            total += int(row[1])
            greatest_increase_month = row[0]
            monthly_difference.append(int(row[1]) - previous_month)
            previous_month = int(row[1])
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
            
    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {month_count-1}")
    print(f"Total PnL: ${total_pnl}")
    print(f"Average Change: {round(sum(monthly_difference)/85, 2)} ")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")