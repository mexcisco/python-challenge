import os

import csv

csvpath = os.path.join('C:/Users/Cisco/OneDrive/python-challenge/PyBank/Resources/budget_data.csv')
file_to_output = "analysis/budget_analysis_1.txt"



total_months = 0 
prev_revenue = 0 
month_of_change = []
revenue_change_list = []
greatest_increse = ["", 0]
greatest_decrese = ["", 99999999999999999999]
total_revenue = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
       
       #track total
       total_months = total_months + 1
       total_revenue = total_revenue + int(row["Revenue"])

       #track Rev change
       revenue_change = int(row["Revenue"]) - prev_revenue
       prev_revenue = int(row["Revenue"])
       revenue_change_list = revenue_change_list + [revenue_change]
       month_of_change = month_of_change = [row["Date"]]

       #calc greatest increase
       if (revenue_change > greatest_increse[1]):
           greatest_increse[0] = row["Date"]
           greatest_increse[1] = revenue_change
        
        #calc greatest decrease
       if (revenue_change < greatest_decrese[1]):
           greatest_decrese[0] = row["Date"]
           greatest_decrese[1] = revenue_change

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increse[0]} (${greatest_increse[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrese[0]} ($){greatest_decrese[1]})\n"
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)