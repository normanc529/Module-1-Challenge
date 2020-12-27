import csv
from pathlib import Path
csvpath = Path('inexpensive_loans.csv')

#print(csvpath)                     check file path relative
#print(csvpath.absolute())          check file path absolute

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

loan_costs = [500, 600, 200, 1000, 450]
# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

# this is the length of the loan list, sum of the loan list, and average cost of the loan list
# it will print out each respective piece of info

total_number_of_loans = len(loan_costs)
print(f"The total number of loans in the list loan costs is : {total_number_of_loans}")

sum_of_loan_costs = sum(loan_costs)
print(f"The sum of the loans in the list loan costs is: {sum_of_loan_costs}")

average_of_loan_costs = sum_of_loan_costs / total_number_of_loans
print(f"The average of the loans in the loan costs list is: {average_of_loan_costs}")

#this is the dictionary: loan, and I am pulling the "future_value" key and "remaining_months" key values and printing them

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

future_value = loan["future_value"]
print(f" The future value of this loan is ${future_value}")


remaining_months = loan["remaining_months"]
print(f" There are {remaining_months} months remaining in the loan")


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

discount_rate = 0.20
fair_value = future_value / (1 + discount_rate/12) ** remaining_months

print(f" the fair value is: {fair_value:.2f}")

#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

#print(loan["loan_price"])                   #uncomment to check loan price from dictionary key


if fair_value >= loan["loan_price"]:
    print("This loan is a good buy because it is a better fair value than the loan price")

else:
    print("this price is a bad buy because the fair value is lower than the loan price")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""
#for a new loan


new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

#figuring out present value by taking the key values from the new_loan dictionary which are FV and remaining months

present_value = new_loan["future_value"] / (1 + discount_rate/12) ** new_loan["remaining_months"]

print(f"The present value of the new loan is: ${present_value:.2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
# @TODO: Create an empty list called `inexpensive_loans`

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list

#i am trying to loop through a list called loans, and in that list i am going to check if the loan_price key value is  <= to the value_to_be_under criteria i have set
#loan(can be named anything) represents the dictionaries in the list that i convert into a variable to input into the function

inexpensive_loans = []
value_to_be_under = 500

for loan in loans:

    if loan["loan_price"] <= (value_to_be_under):

        #inexpensive_loans.append(loan["loan_price"])       this only gives back the value in the loan_price key which is 500, 200
        inexpensive_loans.append(loan)                      #but if i draw from the inexpensive_loans.append(loan), it will give me the whole dictionary item in the loans list


        #for the inexpensive loans list that i created,
        # append the information from the loan["loan_price"] dictionary 'key'
        # which correlates with

# @TODO: Print the `inexpensive_loans` list
#this will print the loan amounts that fit the criteria of being under the set number in the value_to_be_under variable i set up
#this needs to be outside the iteration loop so that it does not print multiple outputs when running through the loop each time
#print(inexpensive_loans)

"""Part 5: Save the results.
Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

    with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)
"""
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path

output_path = Path("inexpensive_loans.csv")         #outputs the information to a csv file called inexpensive_loans.csv

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!



#trying to covert my first dictionary of info into a list of strings
#{'loan_price': 500, 'remaining_months': 13, 'repayment_interval': 'bullet', 'future_value': 1000}
#final output that i want is the 500, 13, bullet, 100 in a [x, x, x, x] format

with open(csvpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        # create a new row variable to store the formatted list of strings we use for csvwriter.writerow input
        formatted_row = []
        for h in header:
            col = loan[h]
            formatted_row.append(col)
        # for loop through header is complete here so formatted_row is the complete formatted list of strings
        csvwriter.writerow(formatted_row)   #after completing this line it will go back into the for loan in inexpensive_loans statement to run through the second item --> inexpensive_loan[1]



#the basic code to append 1 list without a loop would be like this
#loan_p = inexpensive_loans[0]["loan_price"]
#remaining_m = inexpensive_loans[0]["remaining_months"]
#repayment_i = inexpensive_loans[0]["repayment_interval"]
#fv = inexpensive_loans[0]["future_value"]
#first_loan_list = []
#first_loan_list.append(loan_p)
#first_loan_list.append(remaining_m)
#first_loan_list.append(repayment_i)
#first_loan_list.append(fv)
#print(first_loan_list)

#when making a  for loop, check to see what is always changing and make the loop for that item --- in this case the thing changing would be header[x,x,x,x]