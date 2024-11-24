import tkinter as tk
from tkinter import messagebox
import pandas as pd

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget App")
        self.root.geometry("600x500")

        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

        # Create widgets for input
        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.label_date.pack(pady=5)

        self.entry_date = tk.Entry(root)
        self.entry_date.pack(pady=5)

        self.label_desc = tk.Label(root, text="Description:")
        self.label_desc.pack(pady=5)

        self.entry_desc = tk.Entry(root)
        self.entry_desc.pack(pady=5)

        self.label_amount = tk.Label(root, text="Amount:")
        self.label_amount.pack(pady=5)

        self.entry_amount = tk.Entry(root)
        self.entry_amount.pack(pady=5)

        self.button_add = tk.Button(root, text="Add Transaction", command=self.add_transaction)
        self.button_add.pack(pady=10)

        self.button_show = tk.Button(root, text="Show Transactions", command=self.show_transactions)
        self.button_show.pack(pady=10)

        self.button_balance = tk.Button(root, text="Show Balance", command=self.show_balance)
        self.button_balance.pack(pady=10)

        self.text_display = tk.Text(root, height=15, width=70)
        self.text_display.pack(pady=10)

        # Configure text tags for color
        self.text_display.tag_configure("income", foreground="green")
        self.text_display.tag_configure("expense", foreground="red")

    def add_transaction(self):
        date = self.entry_date.get()
        description = self.entry_desc.get()
        try:
            amount = float(self.entry_amount.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Amount must be a number")
            return

        new_transaction = pd.DataFrame({'Date': [date], 'Description': [description], 'Amount': [amount]})
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
        self.clear_entries()
        messagebox.showinfo("Transaction Added", "Transaction added successfully")

    def show_transactions(self):
        self.text_display.delete('1.0', tk.END)
        for index, row in self.transactions.iterrows():
            tag = "income" if row["Amount"] > 0 else "expense"
            self.text_display.insert(tk.END, f"{row['Date']} - {row['Description']} - {row['Amount']}\n", tag)

    def show_balance(self):
        balance = self.transactions['Amount'].sum()
        messagebox.showinfo("Current Balance", f"Current Balance: {balance}")

    def clear_entries(self):
        self.entry_date.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = BudgetApp(root)
root.mainloop()
