class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def __repr__(self):
        desc = ''
        amount = ''
        items = ""
        title = f"{self.name:*^30}"
        for item in self.ledger:
            desc = f'{item["description"][:23]:<23}'
            amount = f'{item["amount"]:>7.2f}'
            items += desc + amount[:7] + "\n"
        total = f"Total: {self.get_balance()}"

        wallet = f"{title}\n{items}{total}"
        return wallet

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": float(amount), "description": description})
    def withdraw(self, amount, description=''):

        amount = float(amount)
        if amount < 0:
            amount = amount * -1
        funds = self.check_funds(amount)

        if funds:
            if amount > 0:
                amount = amount * -1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):

        balance = 0
        for x in self.ledger:
            balance += x["amount"]
        return balance
    def transfer(self, amount, destination):
        success = self.withdraw(int(amount), description=f'Transfer to {destination.name}')
        if success:
            destination.deposit(int(amount), description=f'Transfer from {self.name}')
            return True
        else:
            return False
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

def create_spend_chart(list):
    total_spent = 0
    spent_by_category = []
    #organizing the budget by category and the total amount
    for budget in list:
        amount = budget_amount(budget)
        spent_by_category.append([budget.name, amount])
        total_spent += budget_amount(budget)

    #calculating percentages and appending it to its category
    for spent in spent_by_category:
        percentage = (spent[1] * 100) / total_spent
        spent.append(int(f'{percentage:.0f}'))

    #formatting the chart
    #title
    title = "Percentage spent by category"

    #chart bars
    chart_perc = ''
    for n in reversed(range(0,101,10)):
        chart_perc += f"{n:>3}|"
        for percentages in spent_by_category:
            if "chart_bar" in percentages:
                chart_perc += " o "
            else:
                unity = int(str(percentages[2])[-1])
                percentage = percentages[2] - unity
                if n == percentage:
                    chart_perc += " o "
                    percentages.append("chart_bar")
                else:
                    chart_perc += "   "
        chart_perc += " "
        if n != 0:
            chart_perc += "\n"

    #horizontal line
    length = (len(list) * 3) + 1
    line = (" " * 4) + ("-" * length)

    #budget names
    i = 0
    vertical_names = ''
    for x in range(100):
        end = True
        vertical_names += "    "
        for budget in spent_by_category:
            try:
                vertical_names += f" {budget[0][i]} "
                end = False
            except:
                vertical_names += "   "
        vertical_names += " "
        if end:
            vertical_names = vertical_names[0:-15]
            break
        vertical_names += "\n"
        i += 1

    chart = title + '\n' + chart_perc + '\n' + line + '\n' + vertical_names
    return chart

def budget_amount(budget):
    spent = 0
    for x in budget.ledger:
        if "Transfer" in x["description"]:
            continue
        if x["amount"] < 0:
            spent += (x["amount"] * -1)
    return spent