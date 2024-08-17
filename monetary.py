def monetary_unit():
    remaining_amount = int(amount * 100)

    number_of_dollars = remaining_amount // 100
    remaining_amount = remaining_amount % 100

    number_of_quarters = remaining_amount // 25
    remaining_amount = remaining_amount % 25

    number_of_dimes = remaining_amount // 10
    remaining_amount = remaining_amount % 10

    number_of_nickels = remaining_amount // 5
    remaining_amount = remaining_amount % 5

    number_of_pennies = remaining_amount

    return f"Your amount {amount} consists of \n \t {number_of_dollars} dollars \n \t {number_of_quarters} quarters \n \t {number_of_dimes} dimes \n \t {number_of_nickels} nickles \n \t {number_of_pennies} pennies"
    


amount = eval(input("Enter the amount: "))
print(monetary_unit())