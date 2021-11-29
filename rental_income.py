class RentalCalc():
    def __init__(self):

        self.Investment = ''
        self.Rent = ''
        self.Expenses = ''
        self.flowcash = []

        # Call other class to pass into next block.
        self.Add_Investment()

# Have user input total investment amount.

    def Add_Investment(self):
        self.Investment = int(
            input("Please enter your total cash investment in digits: "))
        print(f'Your total investment is: ${self.Investment}')
        print("----------------------------------------------------")

        # Call other class to pass into next block.
        self.RentIncome()

# Have user input total rental income.

    def RentIncome(self):
        self.Rent = int(
            input("Please enter your monthly rent income in digits: "))
        print(f'Your rent income is: ${self.Rent}')
        print("----------------------------------------------------")

        # Call other class to pass into next block.
        self.Total_Expenses()

# Have user input total expenses.

    def Total_Expenses(self):
        self.Expenses = int(
            input("Please enter your total expenses in digits: "))
        print(f'Your total monthly expenses are: {self.Expenses}')
        print("----------------------------------------------------")

        # Call other class to pass into next block.
        self.Total_Cashflow()

# Calculate total cashflow.

    def Total_Cashflow(self):
        Cashflow = int(self.Rent) - int(self.Expenses)
        print(f'Total Cashflow is: ${Cashflow}')
        self.flowcash.append(Cashflow)
        print("----------------------------------------------------")

        # Call other class to pass into next block.
        self.CalcROI()

# Run simulation to calculate ROI.

    def CalcROI(self):
        for x in self.flowcash:
            Net_Profit = x * 12
        ROI = (Net_Profit / self.Investment) * 100
        print(f'Your ROI is: {ROI}%')
        print("----------------------------------------------------")


Calculate = RentalCalc()
