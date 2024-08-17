def financial_pay_roll():
    gross_pay = number_of_hours_worked * hourly_pay_rate
    federal_tax = (20 / 100) * gross_pay
    state_tax = (9 / 100) * gross_pay
    total_deduct = federal_tax + state_tax
    net_pay = gross_pay - total_deduct


    print(f"Hours Worked:{number_of_hours_worked:.1f}")
    print(f"Pay Rate: ${hourly_pay_rate}")
    print(f"Gross Pay: ${gross_pay:.1f}")
    print(f"Deductions: \n Federal Witholding (20.0%) : ${federal_tax:.1f} \n State Witholding (9.0%): ${state_tax:.2f} \n Total Deduction: ${total_deduct:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")


employee_name = (input("Enter employee's name:  "))
number_of_hours_worked = eval(input("Enter number of hours worked in a week: "))
hourly_pay_rate = eval(input("Enter hourly pay rate: "))
federal_tax_witholding_rate = eval(input("Enter federal tax withholding rate: "))
state_tax_witholding_rate = eval(input("Enter state tax witholding rate: "))

Employee_name = (input("Employee Name:  "))
(financial_pay_roll())