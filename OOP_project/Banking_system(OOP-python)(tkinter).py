import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# 1. THEME & STYLING (Derived from my CSS)
# ==========================================
BG_DARK = "#0a0a0a"
BG_CARD = "#161616"
PRIMARY_RED = "#e50914"
TEXT_MAIN = "#f4f4f4"
TEXT_MUTED = "#aaaaaa"
FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUBTITLE = ("Segoe UI", 16, "bold")
FONT_NORM = ("Segoe UI", 12)


# ==========================================
# 2. OOP BACKEND (Core Logic)
# ==========================================

# Abstraction & Encapsulation
class Account:
    def __init__(self, account_type):
        self._account_number = str(random.randint(10000, 99999))
        self._balance = 0.0  # Encapsulated data
        self.account_type = account_type

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    # Abstract-like method to be overridden
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False


# Inheritance & Polymorphism
class SavingsAccount(Account):
    def __init__(self):
        super().__init__("Savings")

    def withdraw(self, amount):
        # Polymorphism: Savings accounts might have minimum balance rules
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False


class CheckingAccount(Account):
    def __init__(self):
        super().__init__("Checking")

    def withdraw(self, amount):
        # Polymorphism: Checking accounts allow full withdrawal
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False


# Base User Class
class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def verify_password(self, pwd):
        return self._password == pwd


# Inheritance: Client inherits from User
class Client(User):
    def __init__(self, user_id, password, name, gender, profession, is_working, salary):
        super().__init__(user_id, password)
        self.name = name
        self.gender = gender
        self.profession = profession
        self.is_working = is_working
        self.salary = salary
        self.accounts = []
        self.gold_grams = 0.0

    def add_account(self, account):
        self.accounts.append(account)

    def get_formatted_name(self):
        prof_title = ""
        prof = self.profession.lower()
        if "engineer" in prof:
            prof_title = "ENG. "
        elif "doctor" in prof:
            prof_title = "DR. "
        elif "professor" in prof:
            prof_title = "PROF. "
        else:
            prof_title = "Mr." if self.gender.lower() == "male" else "Ms."

        return f"{prof_title}{self.name}"


# Database Mock
class BankSystem:
    def __init__(self):
        self.clients = {}  # Dictionary to store registered users

    def register_client(self, client):
        self.clients[client._user_id] = client

    def get_client(self, user_id):
        return self.clients.get(user_id)


# ==========================================
# 3. GUI FRONTEND (Tkinter)
# ==========================================

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ZZ.Bnk - Dominate Your Finances")
        self.geometry("900x700")
        self.configure(bg=BG_DARK)
        self.bank = BankSystem()
        self.current_user = None

        # Container for screens
        self.container = tk.Frame(self, bg=BG_DARK)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self.show_login_screen()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # --- STYLE HELPERS ---
    def create_card(self, parent):
        card = tk.Frame(parent, bg=BG_CARD, bd=1, relief="ridge", highlightbackground="#222", highlightthickness=1)
        return card

    def create_button(self, parent, text, command, bg_color=PRIMARY_RED, fg_color="#fff"):
        btn = tk.Button(parent, text=text.upper(), command=command, font=FONT_NORM, bg=bg_color, fg=fg_color,
                        activebackground=BG_DARK, activeforeground=PRIMARY_RED, bd=0, padx=20, pady=10, cursor="hand2")
        return btn

    def create_entry(self, parent, is_password=False):
        entry = tk.Entry(parent, font=FONT_NORM, bg=BG_DARK, fg=TEXT_MAIN, insertbackground=PRIMARY_RED, bd=1,
                         relief="solid")
        if is_password:
            entry.config(show="*")
        return entry

    # --- SCREENS ---
    def show_login_screen(self):
        self.clear_container()
        self.current_user = None

        frame = tk.Frame(self.container, bg=BG_DARK)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="ZZ.Bnk", font=("Segoe UI", 36, "bold"), bg=BG_DARK, fg=TEXT_MAIN).pack(pady=(0, 5))
        tk.Label(frame, text="Dominate your Finances", font=FONT_NORM, bg=BG_DARK, fg=TEXT_MUTED).pack(pady=(0, 30))

        card = self.create_card(frame)
        card.pack(ipadx=40, ipady=40)

        tk.Label(card, text="ID / Username", font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w", pady=(0, 5))
        id_entry = self.create_entry(card)
        id_entry.pack(fill="x", pady=(0, 20), ipady=5)

        tk.Label(card, text="Password", font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w", pady=(0, 5))
        pw_entry = self.create_entry(card, is_password=True)
        pw_entry.pack(fill="x", pady=(0, 30), ipady=5)

        def login():
            user = self.bank.get_client(id_entry.get())
            if user and user.verify_password(pw_entry.get()):
                self.current_user = user
                self.show_dashboard()
            else:
                messagebox.showerror("Error", "Invalid ID or Password")

        self.create_button(card, "Login", login).pack(fill="x", pady=(0, 10))

        register_btn = tk.Button(card, text="Create New Account", font=FONT_NORM, bg=BG_CARD, fg=PRIMARY_RED, bd=0,
                                 activebackground=BG_CARD, activeforeground="#fff", command=self.show_register_screen)
        register_btn.pack()

    def show_register_screen(self):
        self.clear_container()

        frame = tk.Frame(self.container, bg=BG_DARK)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Join ZZ.Bnk", font=FONT_TITLE, bg=BG_DARK, fg=TEXT_MAIN).pack(pady=(0, 20))
        card = self.create_card(frame)
        card.pack(ipadx=30, ipady=30)

        # Fields
        fields = {}
        labels = ["ID (Username)", "Password", "Full Name", "Gender (Male/Female)", "Profession (Engineer/Doctor/etc)",
                  "Working? (Yes/No)"]
        for label in labels:
            tk.Label(card, text=label, font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w")
            ent = self.create_entry(card)
            ent.pack(fill="x", pady=(0, 10))
            fields[label] = ent

        def proceed():
            is_working = fields["Working? (Yes/No)"].get().strip().lower() == "yes"

            # Temporary storage to pass to setup
            self.temp_reg_data = {
                "id": fields["ID (Username)"].get(),
                "pw": fields["Password"].get(),
                "name": fields["Full Name"].get(),
                "gender": fields["Gender (Male/Female)"].get(),
                "prof": fields["Profession (Engineer/Doctor/etc)"].get(),
                "is_working": is_working
            }
            self.show_setup_screen()

        self.create_button(card, "Next Step", proceed).pack(fill="x", pady=(20, 0))

    def show_setup_screen(self):
        self.clear_container()
        frame = tk.Frame(self.container, bg=BG_DARK)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        card = self.create_card(frame)
        card.pack(ipadx=30, ipady=30)

        tk.Label(card, text="Account Setup", font=FONT_TITLE, bg=BG_CARD, fg=TEXT_MAIN).pack(pady=(0, 20))

        # Salary if working
        salary_entry = None
        if self.temp_reg_data["is_working"]:
            tk.Label(card, text="Enter your Monthly Salary ($)", font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(
                anchor="w")
            salary_entry = self.create_entry(card)
            salary_entry.pack(fill="x", pady=(0, 15))

        tk.Label(card, text="Choose Account Type", font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w")
        acc_type_var = tk.StringVar(value="Checking")
        tk.Radiobutton(card, text="Checking Account", variable=acc_type_var, value="Checking", bg=BG_CARD, fg=TEXT_MAIN,
                       selectcolor=BG_DARK).pack(anchor="w")
        tk.Radiobutton(card, text="Savings Account", variable=acc_type_var, value="Savings", bg=BG_CARD, fg=TEXT_MAIN,
                       selectcolor=BG_DARK).pack(anchor="w", pady=(0, 15))

        tk.Label(card, text="Initial Deposit ($)", font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w")
        deposit_entry = self.create_entry(card)
        deposit_entry.pack(fill="x", pady=(0, 20))

        def finish_setup():
            salary = float(salary_entry.get()) if salary_entry else 0.0
            initial_dep = float(deposit_entry.get()) if deposit_entry.get() else 0.0

            # Instantiate Client
            new_client = Client(
                self.temp_reg_data["id"], self.temp_reg_data["pw"], self.temp_reg_data["name"],
                self.temp_reg_data["gender"], self.temp_reg_data["prof"],
                self.temp_reg_data["is_working"], salary
            )

            # Create Account
            if acc_type_var.get() == "Checking":
                acc = CheckingAccount()
            else:
                acc = SavingsAccount()

            acc.deposit(initial_dep)
            new_client.add_account(acc)

            # Save to Bank Database
            self.bank.register_client(new_client)

            # Output Celebration Message
            celebration = f"Account Created Successfully!\n\nWelcome to ZZ.Bnk,\n{new_client.get_formatted_name()}."
            messagebox.showinfo("Welcome!", celebration)

            # Force Logout
            messagebox.showwarning("Security", "For security reasons, please log in with your new credentials.")
            self.show_login_screen()

        self.create_button(card, "Complete Registration", finish_setup).pack(fill="x")

    def show_dashboard(self):
        self.clear_container()

        # Welcome Header
        header = tk.Frame(self.container, bg=BG_DARK)
        header.pack(fill="x", pady=20, padx=40)
        tk.Label(header, text=f"Welcome back, {self.current_user.get_formatted_name()}", font=FONT_TITLE, bg=BG_DARK,
                 fg=TEXT_MAIN).pack(side="left")
        self.create_button(header, "Logout", self.show_login_screen, bg_color="#333").pack(side="right")

        # --- TOP: Main Banking Operations (Middle of screen) ---
        main_dash = tk.Frame(self.container, bg=BG_DARK)
        main_dash.pack(fill="x", padx=40, pady=10)

        # Accounts List (The "Plus" feature to show all accounts)
        accounts_frame = self.create_card(main_dash)
        accounts_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), ipadx=10, ipady=10)
        tk.Label(accounts_frame, text="Your Accounts", font=FONT_SUBTITLE, bg=BG_CARD, fg=PRIMARY_RED).pack(anchor="w",
                                                                                                            pady=(0,
                                                                                                                  10))

        active_account = self.current_user.accounts[0]  # Default to first account for simplicity

        for acc in self.current_user.accounts:
            acc_info = f"{acc.account_type.upper()} | #: {acc.get_account_number()} | Bal: ${acc.get_balance():.2f}"
            tk.Label(accounts_frame, text=acc_info, font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w")

        # Add New Account Button
        def add_acc():
            new_acc = SavingsAccount()
            self.current_user.add_account(new_acc)
            self.show_dashboard()  # Refresh

        tk.Button(accounts_frame, text="+ Open New Vault", bg=BG_CARD, fg=PRIMARY_RED, bd=0, font=FONT_NORM,
                  activebackground=BG_CARD, cursor="hand2", command=add_acc).pack(anchor="w", pady=10)

        # Operations Frame
        ops_frame = self.create_card(main_dash)
        ops_frame.pack(side="right", fill="both", expand=True, padx=(10, 0), ipadx=20, ipady=20)
        tk.Label(ops_frame, text="Quick Transfer", font=FONT_SUBTITLE, bg=BG_CARD, fg=PRIMARY_RED).pack(anchor="w")

        amount_entry = self.create_entry(ops_frame)
        amount_entry.pack(fill="x", pady=10)

        btn_row = tk.Frame(ops_frame, bg=BG_CARD)
        btn_row.pack(fill="x")

        def perform_deposit():
            try:
                amt = float(amount_entry.get())
                if active_account.deposit(amt):
                    self.show_dashboard()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        def perform_withdraw():
            try:
                amt = float(amount_entry.get())
                if active_account.withdraw(amt):
                    self.show_dashboard()
                else:
                    messagebox.showerror("Error", "Insufficient funds")
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        self.create_button(btn_row, "Deposit", perform_deposit).pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.create_button(btn_row, "Withdraw", perform_withdraw, bg_color="#333").pack(side="right", fill="x",
                                                                                        expand=True, padx=(5, 0))

        # --- BOTTOM: Analytical Dashboard (Gold Investment) ---
        analytics = tk.Frame(self.container, bg=BG_DARK)
        analytics.pack(fill="both", expand=True, padx=40, pady=20)
        tk.Label(analytics, text="Analytical Dashboard", font=FONT_TITLE, bg=BG_DARK, fg=TEXT_MAIN).pack(anchor="w",
                                                                                                         pady=(0, 10))

        gold_card = self.create_card(analytics)
        gold_card.pack(fill="both", expand=True, ipadx=20, ipady=20)

        gold_price = 154.98  # Mock price per gram

        col1 = tk.Frame(gold_card, bg=BG_CARD)
        col1.pack(side="left", fill="both", expand=True)
        tk.Label(col1, text="Gold Portfolio", font=FONT_SUBTITLE, bg=BG_CARD, fg=TEXT_MUTED).pack(anchor="w")
        tk.Label(col1, text=f"{self.current_user.gold_grams:.2f} g", font=("Segoe UI", 36, "bold"), bg=BG_CARD,
                 fg="#FFD700").pack(anchor="w")
        tk.Label(col1, text=f"Total Value: ${self.current_user.gold_grams * gold_price:.2f}", font=FONT_NORM,
                 bg=BG_CARD, fg=TEXT_MAIN).pack(anchor="w")

        col2 = tk.Frame(gold_card, bg=BG_CARD)
        col2.pack(side="right", fill="both", expand=True)
        tk.Label(col2, text=f"Current Market Rate: ${gold_price}/g", font=FONT_NORM, bg=BG_CARD, fg=TEXT_MAIN).pack(
            anchor="e")

        invest_entry = self.create_entry(col2)
        invest_entry.pack(side="top", anchor="e", pady=10)

        def invest_gold():
            try:
                amt = float(invest_entry.get())
                # Deduct from balance, convert to gold
                if active_account.withdraw(amt):
                    grams_bought = amt / gold_price
                    self.current_user.gold_grams += grams_bought
                    messagebox.showinfo("Success", f"Invested ${amt:.2f}.\nAcquired {grams_bought:.2f}g of Gold.")
                    self.show_dashboard()
                else:
                    messagebox.showerror("Error", "Insufficient funds to invest that amount.")
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        self.create_button(col2, "Invest USD in Gold", invest_gold).pack(side="top", anchor="e")


if __name__ == "__main__":
    app = BankApp()
    app.mainloop()