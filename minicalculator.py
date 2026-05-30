import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        
        # --- COLOR PALETTE CONFIGURATION ---
        self.bg_main = "#f4f5f7"        # Light background for the window
        self.bg_display = "#ffffff"     # White background for the display screen
        self.fg_display = "#1e293b"     # Dark slate text for readability
        
        self.root.configure(bg=self.bg_main)
        self.expression = ""
        
        # Display Screen
        self.display = tk.Entry(
            root, 
            font=("Helvetica", 24), 
            bd=0, 
            insertwidth=4, 
            width=14, 
            borderwidth=0, 
            justify="right",
            bg=self.bg_display,
            fg=self.fg_display
        )
        self.display.grid(row=0, column=0, columnspan=5, ipady=30, padx=15, pady=15, sticky="nsew")
        
        # Configure grid weights for responsiveness
        for i in range(7):
            root.rowconfigure(i, weight=1)
        for i in range(5):
            root.columnconfigure(i, weight=1)
            
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('sin', 1, 0, '#e2e8f0'), ('cos', 1, 1, '#e2e8f0'), ('tan', 1, 2, '#e2e8f0'), ('^', 1, 3, '#e2e8f0'), ('⌫', 1, 4, '#ef4444'),
            ('ln', 2, 0, '#e2e8f0'), ('log', 2, 1, '#e2e8f0'), ('π', 2, 2, '#e2e8f0'), ('√', 2, 3, '#e2e8f0'), ('/', 2, 4, '#3b82f6'),
            ('7', 3, 0, '#ffffff'), ('8', 3, 1, '#ffffff'), ('9', 3, 2, '#ffffff'), ('(', 3, 3, '#e2e8f0'), ('*', 3, 4, '#3b82f6'),
            ('4', 4, 0, '#ffffff'), ('5', 4, 1, '#ffffff'), ('6', 4, 2, '#ffffff'), (')', 4, 3, '#e2e8f0'), ('-', 4, 4, '#3b82f6'),
            ('1', 5, 0, '#ffffff'), ('2', 5, 1, '#ffffff'), ('3', 5, 2, '#ffffff'), ('C', 5, 3, '#ef4444'), ('+', 5, 4, '#3b82f6'),
            ('0', 6, 0, '#ffffff'), ('.', 6, 1, '#ffffff'), ('+/-', 6, 2, '#ffffff'), ('=', 6, 3, '#3b82f6', 2)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            bg_color = btn[3]
            colspan = btn[4] if len(btn) == 5 else 1
            
            fg_color = "#ffffff" if bg_color in ['#3b82f6', '#ef4444'] else "#1e293b"
            action = lambda x=text: self.on_button_click(x)
            
            button = tk.Button(
                self.root, 
                text=text, 
                bg=bg_color, 
                fg=fg_color, 
                font=("Helvetica", 16, "bold" if bg_color in ['#3b82f6', '#ef4444'] else "normal"), 
                borderwidth=0,
                activebackground="#cbd5e1",
                command=action
            )
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                expr = self.expression.replace('^', '**').replace('π', str(math.pi))
                if 'sin' in expr or 'cos' in expr or 'tan' in expr or 'log' in expr or 'ln' in expr or '√' in expr:
                    expr = expr.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
                    expr = expr.replace('log', 'math.log10').replace('ln', 'math.log').replace('√', 'math.sqrt')
                self.expression = str(eval(expr))
            except Exception:
                self.expression = "Error"
        elif char == '+/-':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
        else:
            if self.expression == "Error":
                self.expression = ""
            if char in ['sin', 'cos', 'tan', 'log', 'ln', '√']:
                self.expression += char + "("
            else:
                self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)