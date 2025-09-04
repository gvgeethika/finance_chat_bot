def build_prompt(user_type, user_text, nlu_data, budget_data):
    """
    Build prompt for LLM using provided NLU data.
    """
    prompt = f"""
User type: {user_type}
User text: {user_text}
NLU data: {nlu_data}
Budget data: {budget_data}
Please provide a budget summary and recommendations.
"""
    return prompt

