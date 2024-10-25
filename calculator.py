import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Calculator")

        # Input fields
        self.label1 = tk.Label(root, text="Enter the first number :")
        self.label1.pack(pady=5)

        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=5)

        self.label2 = tk.Label(root, text="Enter the second number:")
        self.label2.pack(pady=5)

        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=5)

        # Operation selection
        self.label3 = tk.Label(root, text="Select operation:")
        self.label3.pack(pady=15)

        self.operation_var = tk.StringVar(value="add")
        self.operations = ["add", "subtract", "multiply", "divide"]
        for operation in self.operations:
            tk.Radiobutton(root, text=operation.capitalize(), variable=self.operation_var, value=operation).pack()

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=20)

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            operation = self.operation_var.get()
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
