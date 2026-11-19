# Student Expense Tracker

A simple, command-line Python application designed to help students manage their monthly budget, log daily expenses, and monitor their remaining balance in Indian Rupees (Rs.).

## Features

* **Monthly Budget Setup:** Set your overall spending limit at the start of the session.
* **Add Expenses:** Quickly log daily expenses, which are automatically added to your running total.
* **View Total Expenses:** Check the cumulative amount spent so far.
* **Check Remaining Budget:** Calculate how much money you have left and receive an instant alert if you have exceeded your budget.
* **Interactive Menu:** Easy-to-navigate terminal menu loop until you choose to exit.

## Prerequisites

* **Python 3.x** installed on your system.

## Installation & Usage

1. Save your Python code to a file named `expense_tracker.py`.
2. *(Important Note)* Fix the capitalization typo on **Line 1** of your script before running it:
   * Change `Print("================================")` to `print("================================")` (Python is case-sensitive, so `Print` with a capital `P` will throw a `NameError`).
3. Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
   ```bash
   python expense_tracker.py
   ```

## Example Usage

```text
================================
     STUDENT EXPENSE TRACKER
================================
Enter your monthly budget: 5000

1. Add Expense
2. View Total Expenses
3. Check Remaining Budget
4. Exit

Enter your choice: 1
Enter today's expense: 250
Expense added successfully!

1. Add Expense
2. View Total Expenses
3. Check Remaining Budget
4. Exit

Enter your choice: 3
Remaining budget: Rs. 4750.0
You are within your budget!
```

## Future Improvements

If you plan to expand this project, consider adding:
* **Data Persistence:** Save expenses to a `.txt` or `.csv` file so data isn't lost when the program closes.
* **Expense Categories:** Tag expenses (e.g., Food, Travel, Books) to see where most of your money goes.
* **Input Validation:** Use `try-except` blocks to prevent the program from crashing if a user enters letters instead of numbers.