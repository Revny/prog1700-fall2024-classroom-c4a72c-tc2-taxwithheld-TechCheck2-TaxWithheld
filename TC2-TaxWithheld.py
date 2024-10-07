# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    weeklysalary=float(input("what is your weekly salary?"))
    
    
    provincialtax=6
    federaltax=25
    dependents=float(input("how many dependents?"))
    provincialtaxwithheld=weeklysalary*provincialtax/100
    federaltaxwithheld=weeklysalary*federaltax/100
    dependentdeduction=dependents*20
    print(provincialtaxwithheld)
    print(federaltaxwithheld)
    print(dependentdeduction)
    total=provincialtaxwithheld+federaltaxwithheld-dependentdeduction
    print(total)






    # YOUR CODE ENDS HERE

main()
