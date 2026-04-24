import streamlit as st
import random
import time


# 1. PAGE CONFIGURATION & CSS INJECTION  (the system styling injecting form my css)  ⭐⭐⭐⭐⭐

st.set_page_config(page_title="ZZ.Bnk | Dominate Your Finances", layout="wide")


def inject_custom_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0a0a0a;
            color: #f4f4f4;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        }

        /* Container / Card Styling */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #161616 !important;
            border: 1px solid #222 !important;
            border-radius: 8px !important;
        }

        /* Buttons */
        .stButton > button[data-testid="baseButton-primary"] {
            background-color: #e50914 !important;
            color: white !important;
            border: 2px solid #e50914 !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
        }
        .stButton > button[data-testid="baseButton-primary"]:hover {
            background-color: transparent !important;
            color: #e50914 !important;
            box-shadow: 0 0 20px rgba(229, 9, 20, 0.6) !important;
        }

        /* Titles & Logos */
        .logo {
            font-size: 38px;
            font-weight: 900;
            color: #f4f4f4;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-align: center;
        }
        .logo span { color: #e50914; }

        .section-title {
            font-size: 28px;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 20px;
        }
        .section-title span { color: #e50914; }

        .text-gold { 
            color: #FFD700; 
            font-size: 42px; 
            font-weight: 800; 
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
        }
        .text-muted { color: #aaaaaa; }
        </style>
    """, unsafe_allow_html=True)



# 2. OOP BACKEND (the system details) ⭐⭐⭐⭐⭐

class Account:
    def __init__(self, account_type):
        self._account_number = str(random.randint(10000, 99999))
        self._balance = 0.0
        self.account_type = account_type

    def get_balance(self): return self._balance

    def get_account_number(self): return self._account_number

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount): pass


class SavingsAccount(Account):
    def __init__(self): super().__init__("Savings")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False


class CheckingAccount(Account):
    def __init__(self): super().__init__("Checking")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False


class Client:
    def __init__(self, user_id, password, name, gender, profession, is_working, salary):
        self._user_id = user_id
        self._password = password
        self.name = name
        self.gender = gender
        self.profession = profession
        self.is_working = is_working
        self.salary = salary
        self.accounts = []
        self.gold_grams = 0.0

    def verify_password(self, pwd): return self._password == pwd

    def add_account(self, account): self.accounts.append(account)

    def get_formatted_name(self):
        prof = self.profession.lower()
        title = "ENG. " if "engineer" in prof else "DR. " if "doctor" in prof else "Mr." if self.gender == "Male" else "Ms."
        return f"{title}{self.name}"


class BankSystem:
    def __init__(self): self.clients = {}

    def register_client(self, client): self.clients[client._user_id] = client

    def get_client(self, user_id): return self.clients.get(user_id)



# 3. APP STATE & ROUTING (networking part)  ⭐⭐⭐⭐⭐

if 'bank' not in st.session_state: st.session_state.bank = BankSystem()
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'page' not in st.session_state: st.session_state.page = 'login'
if 'temp_data' not in st.session_state: st.session_state.temp_data = {}


def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()


# 4. GUI SCREENS ⭐⭐⭐⭐⭐

def show_login_screen():
    st.markdown('<div class="logo">ZZ<span>.Bnk</span></div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;' class='text-muted'>Dominate your Finances</p><br>",
                unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        with st.container(border=True):
            st.subheader("Login to your Vault")
            u_id = st.text_input("ID / Username")
            u_pw = st.text_input("Password", type="password")
            if st.button("Login", use_container_width=True, type="primary"):
                user = st.session_state.bank.get_client(u_id)
                if user and user.verify_password(u_pw):
                    st.session_state.current_user = user
                    switch_page('dashboard')
                else:
                    st.error("Invalid ID or Password")
            if st.button("Create New Account", use_container_width=True): switch_page('register')


def show_register_screen():
    st.markdown('<div class="logo">ZZ<span>.Bnk</span></div><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        with st.container(border=True):
            st.markdown("<div class='section-title'>Join <span>ZZ.Bnk</span></div>", unsafe_allow_html=True)
            u_id = st.text_input("ID (Username)")
            u_pw = st.text_input("Password", type="password")
            u_name = st.text_input("Full Name")
            u_gender = st.selectbox("Gender", ["Male", "Female"])
            u_prof = st.text_input("Profession")
            u_work = st.radio("Are you currently working?", ["Yes", "No"])
            if st.button("Next Step", use_container_width=True, type="primary"):
                st.session_state.temp_data = {"id": u_id, "pw": u_pw, "name": u_name, "gender": u_gender,
                                              "prof": u_prof, "is_working": u_work == "Yes"}
                switch_page('setup')


def show_setup_screen():
    st.markdown('<div class="logo">ZZ<span>.Bnk</span></div><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        with st.container(border=True):
            st.markdown("<div class='section-title'>Account <span>Setup</span></div>", unsafe_allow_html=True)
            salary = st.number_input("Monthly Salary ($)", min_value=0.0) if st.session_state.temp_data.get(
                "is_working") else 0.0
            acc_type = st.radio("Choose Account Type", ["Checking", "Savings"])
            initial_dep = st.number_input("Initial Deposit ($)", min_value=0.0)
            if st.button("Complete", use_container_width=True, type="primary"):
                d = st.session_state.temp_data
                client = Client(d["id"], d["pw"], d["name"], d["gender"], d["prof"], d["is_working"], salary)
                acc = CheckingAccount() if acc_type == "Checking" else SavingsAccount()
                acc.deposit(initial_dep)
                client.add_account(acc)
                st.session_state.bank.register_client(client)

                congrats = "him" if d["gender"] == "Male" else "her"
                st.balloons()
                st.success(f"Congratulations to {congrats}! Welcome to the elite, {client.get_formatted_name()}.")
                st.warning("⚠️ For security reasons, please log in with your new credentials.")
                time.sleep(4)
                switch_page('login')


def show_dashboard():
    user = st.session_state.current_user
    gold_rate = 151.94  # Mock market rate

    col_h1, col_h2 = st.columns([4, 1])
    with col_h1:
        st.markdown(f"<h2>Welcome back, <span style='color: #e50914;'>{user.get_formatted_name()}</span></h2>",
                    unsafe_allow_html=True)
    with col_h2:
        if st.button("Logout", use_container_width=True):
            st.session_state.current_user = None
            switch_page('login')

    st.markdown("---")

    # ROW 1: Operations   ⭐⭐⭐⭐⭐
    left, right = st.columns(2)
    with left:
        st.markdown("<div class='section-title'>Your <span>Vaults</span></div>", unsafe_allow_html=True)
        with st.container(border=True):
            for acc in user.accounts:
                st.markdown(f"**{acc.account_type.upper()}** | #: `{acc.get_account_number()}`")
                st.markdown(f"<h3 style='color: #e50914; margin-top: -10px;'>${acc.get_balance():.2f}</h3>",
                            unsafe_allow_html=True)
                st.markdown("<hr style='border-color: #222; margin: 5px 0;'>", unsafe_allow_html=True)

            new_type = st.radio("Open New Vault:", ["Checking", "Savings"], horizontal=True)
            if st.button("+ Create Account", type="primary"):
                user.add_account(CheckingAccount() if new_type == "Checking" else SavingsAccount())
                st.rerun()

    with right:
        st.markdown("<div class='section-title'>Quick <span>Transfer</span></div>", unsafe_allow_html=True)
        with st.container(border=True):
            acc_map = {f"{a.account_type} ({a.get_account_number()})": a for a in user.accounts}
            sel_acc = st.selectbox("Source Account", list(acc_map.keys()))
            amt = st.number_input("Amount ($)", min_value=0.01)

            c1, c2 = st.columns(2)
            if c1.button("Deposit", use_container_width=True, type="primary"):
                acc_map[sel_acc].deposit(amt)
                st.rerun()
            if c2.button("Withdraw", use_container_width=True):
                if acc_map[sel_acc].withdraw(amt):
                    st.rerun()
                else:
                    st.error("Insufficient Funds")

    # ROW 2: Analytical Dashboard   ⭐⭐⭐⭐⭐
    st.markdown("<br><div class='section-title'>Analytical <span>Dashboard</span></div>", unsafe_allow_html=True)
    with st.container(border=True):
        g_col1, g_col2 = st.columns(2)
        with g_col1:
            st.markdown("<p class='text-muted'>Gold Portfolio</p>", unsafe_allow_html=True)
            st.markdown(f"<div class='text-gold'>{user.gold_grams:.2f} g</div>", unsafe_allow_html=True)
            st.write(f"**Estimated Market Value:** ${user.gold_grams * gold_rate:.2f}")

        with g_col2:
            st.markdown(f"<p style='text-align: right;' class='text-muted'>Current Market Rate: ${gold_rate}/g</p>",
                        unsafe_allow_html=True)
            invest_amt = st.number_input("USD to Invest in Gold", min_value=0.0, step=10.0)
            if st.button("Purchase Gold Assets", use_container_width=True, type="primary"):
                if user.accounts[0].withdraw(invest_amt):
                    user.gold_grams += (invest_amt / gold_rate)
                    st.success(f"Successfully added gold to your portfolio.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Insufficient funds in main account.")


# 5. EXECUTION   ⭐⭐⭐⭐⭐

inject_custom_css()
if st.session_state.page == 'login':
    show_login_screen()
elif st.session_state.page == 'register':
    show_register_screen()
elif st.session_state.page == 'setup':
    show_setup_screen()
elif st.session_state.page == 'dashboard':
    show_dashboard()