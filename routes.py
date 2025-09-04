# routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from ibm_api import generate_budget_summary

router = APIRouter()

# ---------------- Existing Models ----------------
class BudgetData(BaseModel):
    income: float
    expenses: Dict[str, float]
    savings_goal: float

class BudgetSummaryRequest(BaseModel):
    user_text: str
    user_type: str
    budget_data: BudgetData

# ---------------- Budget Summary Endpoint ----------------
@router.post("/budget-summary")
def budget_summary_endpoint(request: BudgetSummaryRequest):
    # request is automatically validated here
    result = generate_budget_summary(
        user_text=request.user_text,
        user_type=request.user_type,
        budget_data=request.budget_data.dict()
    )
    return result


# ---------------- Q&A Chatbot Endpoint ----------------
class QuestionRequest(BaseModel):
    question: str

@router.post("/qna")
def qna_endpoint(req: QuestionRequest):
    q = req.question.lower()

    # Predefined answers
    sample_answers = {
        "tax": "💡 You can save on taxes by investing in Section 80C options like ELSS, PPF, or NPS. Also, health insurance under 80D provides additional benefits.",
        "savings": "💡 A good rule is the 50/30/20 budget: 50% needs, 30% wants, 20% savings. Start automating savings every month.",
        "budget": "💡 Track your expenses using categories (rent, food, transport). Always aim to save 20-30% of income.",
        "loan": "💡 Always pay high-interest loans first, like credit cards. Consider consolidating if you have multiple EMIs.",
        "investment": "💡 Diversify! Mutual funds, index funds, and SIPs are safe starting points. Avoid putting all money in one asset.",
        "emergency fund": "💡 Keep at least 3–6 months of expenses in a liquid fund or savings account for emergencies.",
        "retirement": "💡 Start early! Even small SIPs in mutual funds or NPS compound greatly over decades.",
        "credit score": "💡 Pay your EMIs/credit card bills on time, keep utilization under 30%, and avoid too many loan applications.",
        "insurance": "💡 Health insurance and term life insurance are must-haves. They protect your family and finances.",
        "expenses": "💡 Track small daily spends — they add up. Cut unnecessary subscriptions and reduce eating out."
    }

    # Match keywords
    for keyword, reply in sample_answers.items():
        if keyword in q:
            return {"answer": reply}

    # Default fallback
    return {
        "answer": "🤔 That's a great question! I don’t have a direct answer, but try to budget wisely, save regularly, and invest for long-term growth."
    }




