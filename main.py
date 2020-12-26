
total_number_of_loans = len(loan_costs)
print(f"The total number of loans in the list loan costs is : {total_number_of_loans}")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

sum_of_loan_costs = sum(loan_costs)
print(f"The sum of the loans in the list loan costs is: {sum_of_loan_costs}")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

average_of_loan_costs = sum_of_loan_costs / total_number_of_loans
print(f"The average of the loans in the loan costs list is: {average_of_loan_costs}")
