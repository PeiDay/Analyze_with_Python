import os
import csv

# Path for input from the Resources and output to Analysis 
pybank_csv = os.path.join('Resources','budget_data.csv')
pybank_txt = os.path.join('Analysis','pyBank_analysis.txt')


# Set variables for list for calculations
Months_count = 0 # total month counts
NetChange = 0  # monthly P/L; value
Pre_NetChange = 0
totalNetChange = 0  # total P/L; value
Difference = 0  # total monthly P/L diff; value
totalDifference = 0  
Difference_count = 0
MaxNetChange = 0 # look for value
MaxNetChange_Month = "" # look for month
MinNetChange = 0
MinNetChange_Month = ""

# Read the cvs file and get the header row
with open(pybank_csv,'r') as pyBankBudget:
    budgetData = csv.reader(pyBankBudget, delimiter = ',')
    header = next(budgetData)
    # print(header)
    

    for row in budgetData:
        Months_count += 1
        NetChange = int(row[1])
        totalNetChange += NetChange

        if Pre_NetChange != 0:
            Difference = NetChange - Pre_NetChange
            Difference_count += 1
            totalDifference += Difference
          
        Pre_NetChange = NetChange

        if Difference > MaxNetChange:
            MaxNetChange = Difference
            MaxNetChange_Month = row[0]

        elif Difference < MinNetChange:
            MinNetChange = Difference
            MinNetChange_month = row[0]

    average = totalDifference/Difference_count
    averageDiff = round(average,2)

print('Financial Analysis')
print('-----------------------------------------------------')
print(f'Total Months: {Months_count}')
print(f'Total: ${totalNetChange}')
print(f'Average  Change: ${averageDiff}')
print(f'Greatest Increase in Profits: {MaxNetChange_Month} (${MaxNetChange})')
print(f'Greatest Decrease in Profits: {MinNetChange_month} (${MinNetChange})')
print('-----------------------------------------------------')


with open(pybank_txt, 'w') as textfile:
    textfile.write('Financial Analysis\n')
    textfile.write('-----------------------------------------------------\n')
    textfile.write(f'Total Months: {Months_count}\n')
    textfile.write(f'Total: ${totalNetChange}\n')
    textfile.write(f'Average  Change: ${averageDiff}\n')
    textfile.write(f'Greatest Increase in Profits: {MaxNetChange_Month} (${MaxNetChange})\n')
    textfile.write(f'Greatest Decrease in Profits: {MinNetChange_month} (${MinNetChange})\n')
    textfile.write('-----------------------------------------------------\n')
    textfile.close
