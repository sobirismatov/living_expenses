# Monthly expenses
monthly_expenses = {
    'rent': 1200,
    'utilities': 300,
    'transport': 450,
    'food': 600,
    'entertainment': 110,
    'clothing': 220,
    'health': 30,
    'internet': 60,
    'education': 200,
    'other': 100
}

# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    total = 0
    for key in monthly_expenses:
        total += monthly_expenses[key]
    return total



# Find the least expensive expense
def least_expensive(monthly_expenses: dict) -> str:
    """
    Find the least expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        least_expensive: least expensive expense
    """
    values = list(monthly_expenses.values())
    mn = values[0]
    for value in values[1:]:
        if mn > value:
            mn = value

    return mn


# Find the most expensive expense
def most_expensive(monthly_expenses: dict) -> str:
    """
    Find the most expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        most_expensive: most expensive expense
    """
    values = list(monthly_expenses.values())
    mx = values[0]
    for value in values[1:]:
        if mx < value:
            mx = value

    return mx


print(total_expenses(monthly_expenses))
print(least_expensive(monthly_expenses))
print(most_expensive(monthly_expenses))