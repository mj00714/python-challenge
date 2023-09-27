# import the moudles
import os
import csv

# set the path for the PyBank file (run from the Python-Challenge directory)
budget_data = os.path.join('PyBank/Resources/budget_data.csv')

number_of_months = 0
total_profit_loss = 0
running_profit = 0
profit_change = 0
date = []
profit_loss = []


# open the csv file with the proper encoding
with open(budget_data, encoding='UTF-8') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")

    # add a header row to the CSV file
    budget_data_header = next(csvreader)
    # print the header as a check
    # print(f"CSV Header: {budget_data_header}")
    
    # set the reader to the first row for all of the variables
    first_row = next(csvreader)
    number_of_months += 1 # same as months = months + 1
    total_profit_loss += int(first_row[1])
    running_profit = int(first_row[1])
    
    # looping through the data after the header
    for row in csvreader:  
        # track the dates
        date.append(row[0])
       
        # calculate the change in profit and add it to the list
        profit_change =  int(row[1]) - running_profit
        profit_loss.append(profit_change)
        running_profit = int(row[1])

        # add 1 to the total number of months for the total count
        number_of_months += 1

        # add to the total P & L
        total_profit_loss += int(row[1])

        # greatest increase in profits
        greatest_increase = max(profit_loss)
        greatest_index = profit_loss.index(greatest_increase)
        date_greatest = date[greatest_index]

        # greatest decrease in profits
        greatest_dec = min(profit_loss)
        greatest_dec_index = profit_loss.index(greatest_dec)
        date_greatest_dec = date[greatest_dec_index]

        # calculate the average month-to-month change
        avg_change = (sum(profit_loss) / (number_of_months - 1))

    # print the data
    print('')
    print('Financial Analysis ')
    print('')
    print('------------------------------------')
    print(f'Total Months: {number_of_months}')
    print(f'Total: ${total_profit_loss}')
    print(f'Average Change: ${round(avg_change,2)}')
    print(f'Greatest Increase in Profits: {date_greatest}, ${greatest_increase}')
    print(f'Greatest Decrease in Profits: {date_greatest_dec}, ${greatest_dec}')
    print('')

    # create a txt file and export the data
    output_path = os.path.join('PyBank/analysis/analysis_data.csv')
    with open(output_path, "w", newline='') as datafile:
        print('Financial Analysis\n'
        '------------------------\n'
        f'Total Months: {number_of_months}\n'
        f'Total: ${total_profit_loss}\n'
        f'Average Change: ${round(avg_change,2)}\n'
        f'Greatest Increase in Profits: {date_greatest}, ${greatest_increase}\n'
        f'Greatest Decrease in Profits: {date_greatest_dec}, ${greatest_dec}', file=datafile)