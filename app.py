# app.py
import streamlit as st
import json
import base64

# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="💰 Smart Finance Guide",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------- Background Styling ----------------------
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        .glass-card {{
            background: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.2);
            margin-bottom: 15px;
            color: black;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def container_card(title, content, color="#ffffffDD"):
    st.markdown(
        f"""
        <div class="glass-card" style="background:{color};">
        <h3 style="margin-top:0;">{title}</h3>
        <p style="font-size:16px; line-height:1.5;">{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------- Session State ----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "savings_history" not in st.session_state:
    st.session_state.savings_history = []

# ---------------------- Homepage ----------------------
if st.session_state.page == "home":
    set_background("bg.jpg")  # Optional background image

    st.markdown("""
        <div style="text-align:center; padding:40px;">
        <h1 style="color:black;">💡 BudgetBuddy</h1>
        <p style="color:grey; font-size:18px;">
            Your friendly guide to managing money
        </p>
        </div>
        <style>
        div.stButton > button {
            color: white !important;
            background-color: #4A4A4A !important;
            border: none !important;
            font-weight: 600 !important;
            padding: 10px 20px !important;
            border-radius: 8px !important;
        }
        div.stButton > button:hover {
            background-color: #6A6A6A !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col2:
        if st.button("📊 Budget Summary", use_container_width=True):
            st.session_state.page = "budget-summary"
            st.rerun()
        if st.button("🔎 Spending Insights", use_container_width=True):
            st.session_state.page = "spending-insights"
            st.rerun()
    with col3:
        if st.button("🎯 Goal Planning", use_container_width=True):
            st.session_state.page = "generate"
            st.rerun()
        if st.button("💬 Q&A Chatbot", use_container_width=True):
            st.session_state.page = "nlu"
            st.rerun()

# ---------------------- Budget Summary Page ----------------------
elif st.session_state.page == "budget-summary":
    set_background("bg.jpg")
    st.markdown("""
        <style>
        h2, h3, .stTextInput label, .stNumberInput label, .stSubheader, .stMarkdown {
            color: black !important;
        }
        label {
            font-weight: 600 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("📊 Budget Summary")
    history = st.session_state.savings_history

    

    income = st.number_input("Enter your total income:", min_value=0.0, step=100.0)
    rent = st.number_input("Enter Rent:", min_value=0.0, step=50.0)
    groceries = st.number_input("Enter Groceries:", min_value=0.0, step=50.0)
    transport = st.number_input("Enter Transport:", min_value=0.0, step=50.0)
    others = st.number_input("Other Expenses:", min_value=0.0, step=100.0)

    if st.button("Calculate Summary"):
        expenses = rent + groceries + transport+others
        savings = income - expenses
        history.append(savings)

        summary_text = f"""
         
     🏠 **Rent:** ₹{rent:,.2f}  
    🛒 **Groceries:** ₹{groceries:,.2f}  
     🚗 **Transportation:** ₹{transport:,.2f}   
     📦 **Other Expenses:** ₹{others:,.2f}  
     🔻 **Total Expenses:** ₹{expenses:,.2f}  
     🟢 **Estimated Savings:** ₹{savings:,.2f}

        """

        if savings > 0:
            summary_text += "✅ You're saving money. Keep it up!"
        else:
            summary_text += "⚠ Your expenses exceed your income. Consider adjusting your budget."

        container_card("Summary", summary_text)
        
        # Compare with last month
        if len(st.session_state.savings_history) > 1:
            prev_savings = st.session_state.savings_history[-2]
            if savings > prev_savings:
                st.success(f"📈 Great! Your savings improved by ₹{savings - prev_savings:,.2f} compared to last month.")
            elif savings < prev_savings:
                st.warning(f"📉 Your savings dropped by ₹{prev_savings - savings:,.2f} compared to last month.")
            else:
                st.info("ℹ️ Your savings are the same as last month.")

        # Show trend chart
        st.markdown("### 📊 Savings Trend")
        st.line_chart(st.session_state.savings_history)

    if st.button("🔙 Back", key="back_from_summary"):
        st.session_state.page = "home"
        st.rerun()

# ---------------------- Spending Insights Page ----------------------
elif st.session_state.page == "spending-insights":
    set_background("bg.jpg")
    # Inject CSS to make all labels and headers black
    st.markdown("""
    <style>
    h1, h2, h3, h4, h5, h6,
    .stTextInput label,
    .stNumberInput label,
    .stSubheader,
    .stMarkdown {
        color: black !important;
    }
    label {
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Spending Insights Section
    st.subheader("📈 Spending Insights")

# Income input
    income = st.number_input("Enter your monthly income ($):", min_value=0.0, step=100.0)

# Expense categories
    st.markdown("### 💸 Enter Your Monthly Expenses")
    housing = st.number_input("🏠 Housing/Rent:", min_value=0.0, step=50.0)
    food = st.number_input("🍽️ Food & Groceries:", min_value=0.0, step=50.0)
    transport = st.number_input("🚗 Transportation:", min_value=0.0, step=50.0)
    utilities = st.number_input("🔌 Utilities:", min_value=0.0, step=50.0)
    entertainment = st.number_input("🎉 Entertainment:", min_value=0.0, step=50.0)
    others = st.number_input("📦 Other Expenses:", min_value=0.0, step=50.0)

# Total expenses and balance
    total_expenses = housing + food + transport + utilities + entertainment + others
    balance = income - total_expenses

# Summary in bullet points
    st.markdown("### 📝 Monthly Summary")
    st.markdown(f"""
    - 💰 **Income:** ${income:,.2f}  
    - 🏠 **Housing/Rent:** ${housing:,.2f}  
    - 🍽️ **Food & Groceries:** ${food:,.2f}  
    - 🚗 **Transportation:** ${transport:,.2f}  
    - 🔌 **Utilities:** ${utilities:,.2f}  
    - 🎉 **Entertainment:** ${entertainment:,.2f}  
    - 📦 **Other Expenses:** ${others:,.2f}  
    - 🔻 **Total Expenses:** ${total_expenses:,.2f}  
    - 🟢 **Remaining Balance:** ${balance:,.2f}
    """)
    if st.button("🔙 Back", key="back_from_insights"):
        st.session_state.page = "home"
        st.rerun()

# ---------------------- Goal Planning Page ----------------------
elif st.session_state.page == "generate":
    
    set_background("bg.jpg")
    st.markdown("""
    <style>
    /* Make all headers and labels black */
    h1, h2, h3, h4, h5, h6,
    .stTextInput label,
    .stNumberInput label,
    .stSubheader,
    .stMarkdown {
        color: black !important;
    }

    /* Optional: Make labels bold for better visibility */
    label {
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

    st.subheader("🎯 Goal Planning")

    goal = st.text_input("Enter your goal (e.g., Laptop, Trip, Emergency Fund):")
    cost = st.number_input("Goal Cost ₹():", min_value=0.0, step=50.0)
    months = st.number_input("Months to Save:", min_value=1, step=1)
    monthly_income = st.number_input("Monthly Income:", min_value=0.0, step=100.0)
    monthly_expenses = st.number_input("Monthly Expenses:", min_value=0.0, step=50.0)

    if st.button("Plan Goal"):
        monthly_saving_needed = cost / months
        current_saving_capacity = monthly_income - monthly_expenses
        goal_text = (f"""
        🎯 Goal: {goal} ₹({cost:.2f})  
        ⏳ Timeline: {months} months  
        💵 Need to Save/Month: ₹{monthly_saving_needed:.2f}  
        ✅ Capacity/Month: ₹{current_saving_capacity:.2f}  

        { "🎉 You can reach your goal!" if current_saving_capacity >= monthly_saving_needed else "⚠ Adjust spending to achieve this goal." }
        """)
        container_card("Goal Plan", goal_text)

    if st.button("🔙 Back", key="back_from_goals"):
        st.session_state.page = "home"
        st.rerun()
# ---------------------- Q&A Chatbot Page ----------------------
elif st.session_state.page == "nlu":
   
    set_background("bg.jpg")
    st.markdown('<h1 style="color:black;">Q&A Chatbot</h1>', unsafe_allow_html=True)

# Prompt for user input
    st.markdown('<h3 style="color:black;">Type your financial question:</h3>', unsafe_allow_html=True)


   
    st.markdown("""
        <style>
        .stAlert {
            color: black !important;
            background-color: #f5f5f5 !important;
            border: 1px solid #ccc !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    query = st.text_area("Type your financial question:")

    if st.button("Get Answer"):
        if query.strip():
            import requests
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/qna",  # FastAPI backend URL
                    json={"question": query}
                )
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer received.")
                else:
                    answer = "⚠ Error: Could not get response from backend."
            except Exception as e:
                answer = f"⚠ Error: {e}"

            container_card("Chatbot Response", f"🤖 Your Question: {query}<br>✅ Answer: {answer}")

        else:
            st.warning("Please type a question first!")

    if st.button("🔙 Back", key="back_from_chat"):
        st.session_state.page = "home"
        st.rerun()