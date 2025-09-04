def generate_budget_summary(user_text, user_type, budget_data):
    """
    Generate a human-readable budget summary.
    """
    income = budget_data["income"]
    expenses = budget_data["expenses"]
    savings_goal = budget_data["savings_goal"]

    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    can_save = remaining >= savings_goal

    # Build readable summary
    summary = f"Your total income is ${income:.2f}.\n"
    summary += "Your expenses are:\n"
    for key, value in expenses.items():
        summary += f" - {key}: ${value:.2f}\n"
    summary += f"Total expenses: ${total_expenses:.2f}\n\n"
    summary += f"Remaining money after expenses: ${remaining:.2f}\n"

    if can_save:
        summary += f"✅ You can save your goal of ${savings_goal:.2f} this month!"
    else:
        summary += f"⚠️ You need to reduce some expenses to save your goal of ${savings_goal:.2f}."

    # Include NLU data (optional)
    nlu_data = {
        "sentiment": "neutral",
        "keywords": list(expenses.keys())
    }

    return {
        "response": summary,
        "nlu_data": nlu_data
    }




