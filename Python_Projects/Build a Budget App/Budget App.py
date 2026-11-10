class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        result = "*" * ((30 - len(self.name)) // 2)
        result += self.name
        result += "*" * (30 - len(result))

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            result += f"\n{description:<23}{amount:>7}"

        result += f"\nTotal: {self.get_balance():.2f}"

        return result


def create_spend_chart(categories):
    # Calculate total withdrawals for all categories
    spent = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]

        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded down to nearest 10
    percentages = []

    for amount in spent:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((amount / total_spent) * 100)
            percentage = (percentage // 10) * 10

        percentages.append(percentage)

    # Chart title
    result = "Percentage spent by category\n"

    # Y-axis and bars
    for level in range(100, -1, -10):
        result += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                result += " o "
            else:
                result += "   "

        result += " \n"

    # Horizontal line
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        result += "     "

        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "

        if i < max_length - 1:
            result += "\n"

    return result