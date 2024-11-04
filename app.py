# Import module 
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import math

######
# TODO
# fix resize lag and font jiggle

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # setup root window
        self.geometry("200x250+800+400")
        self.title("Calculator")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.mainframe = tk.Frame(self)
        self.mainframe.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=2)
        self.mainframe.rowconfigure(2, weight=10)
        self.top_frame = TopFrame(self.mainframe)
        self.entry_frame = EntryFrame(self.mainframe)
        self.button_frame = ButtonsFrame(self.mainframe, top_var=self.top_frame.top_var, entry_var=self.entry_frame.entry_var, root=self.mainframe)
        
        ###############################
        # Keyboard Controls
        # TODO
        # bind str-c, copy result?
        bindings = {
        "0": self.button_frame.zero_btn,
        "1": self.button_frame.one_btn,
        "2": self.button_frame.two_btn,
        "3": self.button_frame.three_btn,
        "4": self.button_frame.four_btn,
        "5": self.button_frame.five_btn,
        "6": self.button_frame.six_btn,
        "7": self.button_frame.seven_btn,
        "8": self.button_frame.eight_btn,
        "9": self.button_frame.nine_btn,
        "(": self.button_frame.open_parenthesis_btn,
        ")": self.button_frame.close_parenthesis_btn,
        "<plus>": self.button_frame.plus_btn,
        "<minus>": self.button_frame.minus_btn,
        "<asterisk>": self.button_frame.multiply_btn,
        "<slash>": self.button_frame.divide_btn,
        "<Return>": self.button_frame.equal_btn,
        "<comma>": self.button_frame.comma_btn,
        "<BackSpace>": self.button_frame.backspace_btn,
        "<Delete>": self.button_frame.clear_entry_btn,
        "<Control-c>": self.button_frame.copy_entry_btn
        }
        
        for text, command in bindings.items():
            self.bind(text, command)

class TopFrame(tk.Frame):
    def __init__(self, mainframe):
        tk.Frame.__init__(self, mainframe)
        self.top_font = tkFont.Font(size=10, family="Arial")
        self.top_frame = tk.Frame(mainframe)
        self.top_frame.grid(row=0, column=0, sticky="nsew", pady=(10, 0))
        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_var = tk.StringVar()
        self.top_label =  ttk.Label(self.top_frame, textvariable=self.top_var, font=self.top_font, anchor="e")
        self.top_label.grid(row=0, column=0, sticky="nsew")
        self.top_frame.bind("<Configure>", self.resize)


    def resize(self, *args, **kwargs):
        height = self.top_frame.winfo_height()
        width = self.top_frame.winfo_width()
        width_req = self.top_frame.winfo_reqwidth()
        value = int(max(height/2.5, 8))

        if width_req > width*0.9:
            value = int(value - value/5)
            self.top_font.configure(size=value)
        elif width_req < width*0.7:
            self.top_font.configure(size=value)

class EntryFrame(tk.Frame):
    def __init__(self, mainframe):
        tk.Frame.__init__(self, mainframe)
        self.entry_font = tkFont.Font(size=16, family="Arial")

        self.entry_frame = tk.Frame(mainframe)
        self.entry_frame.grid(row=1, column=0, sticky="nsew")
        self.entry_frame.rowconfigure(0, weight=1)
        self.entry_frame.columnconfigure(0, weight=1)

        self.entry_var = tk.StringVar()
        self.entry_var.set("0")
        
        self.entry_label =  ttk.Label(self.entry_frame, textvariable=self.entry_var, font=self.entry_font, anchor="e")
        self.entry_label.grid(row=0, column=0, sticky="nsew")
        self.entry_label.rowconfigure(0, weight=1)
        self.entry_label.columnconfigure(0, weight=1)

        self.entry_frame.bind("<Configure>", self.resize)

    def resize(self, *args, **kwargs):
        height = self.entry_frame.winfo_height()
        width = self.entry_frame.winfo_width()
        width_req = self.entry_frame.winfo_reqwidth()
        value = int(max(height/2, 10))

        if width_req > width*0.9:
            value = int(value - value/5)
            self.entry_font.configure(size=value)
        elif width_req < width*0.7:
            self.entry_font.configure(size=value)

class ButtonsFrame(tk.Frame):
    def __init__(self, mainframe, entry_var, top_var, root):
        tk.Frame.__init__(self, mainframe)
        self.entry_var = entry_var
        self.top_var = top_var
        self.root = root
        self.button_style = ttk.Style()
        self.button_style.configure("MyButton.TButton", font=("Arial", 10), bold=True)

        self.button_frame = tk.Frame(mainframe)
        self.button_frame.grid(row=2, column=0, sticky="nsew")
        button_dict = {
            "π": self.pi_btn,
            "C": self.clear_btn,
            "CE": self.clear_entry_btn,
            "Back": self.backspace_btn,
            "√": self.square_root_btn,
            "(": self.open_parenthesis_btn,
            ")": self.close_parenthesis_btn,
            "/": self.divide_btn,
            "7": self.seven_btn,
            "8": self.eight_btn,
            "9": self.nine_btn,
            "*": self.multiply_btn,
            "4": self.four_btn,
            "5": self.five_btn,
            "6": self.six_btn,
            "-": self.minus_btn,
            "1": self.one_btn,
            "2": self.two_btn,
            "3": self.three_btn,
            "+": self.plus_btn,
            "+/-": self.plus_minus_btn,
            "0": self.zero_btn,
            ".": self.comma_btn,
            "=": self.equal_btn,
            }
        
        # span buttons on window size change
        # column
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)
        self.button_frame.columnconfigure(3, weight=1)
        # row
        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.rowconfigure(1, weight=1)
        self.button_frame.rowconfigure(2, weight=1)
        self.button_frame.rowconfigure(3, weight=1)
        self.button_frame.rowconfigure(4, weight=1)
        self.button_frame.rowconfigure(5, weight=1)

        # setup buttons layout
        row, column = 0, 0
        for button_pack in button_dict.items():
            symbol, cmd = button_pack
            if not column == 0 and column%4 == 0:
                row += 1
                column = 0
            self.btn = ttk.Button(self.button_frame, text=symbol, width=4, command=cmd, style="MyButton.TButton")
            self.btn.grid(row=row, column=column, sticky="nsew")
            column += 1
        self.button_frame.bind("<Configure>", self.resize)

    def resize(self, *args, **kwargs):
        height = self.btn.winfo_height()/3
        value = max(height, 10)
        self.button_style.configure("MyButton.TButton", font=("Arial", int(value)), bold=True)

    def copy_entry_btn(self, *args):
        entry_var = self.entry_var.get()
        self.clipboard_clear()
        self.clipboard_append(entry_var)
    
    def leading_zero(self, value, *args):
        if value.startswith("0") and "." not in value:
            return value[1:]
        else:
            return value
    
    def validate_entry_digits(self, value, *args):
        # This will run on every numeric button press, including plus/minus and comma(dot)
        top_var = self.top_var.get()
        # Ensure string is not empty
        if value == "":
            value = "0"
        # Validate string is a valid number
        try:
            value = float(value)
        except ValueError:
            print(f"Validation failed. Can't convert str to float. {value}")
            return False
        # clear top left over entry after equal
        if top_var.endswith(" = "):
            self.top_var.set("")
            self.entry_var.set("0")
        return True
    
    #########
    # Buttons
    # 1. btn top row
    def pi_btn(self):
        self.entry_var.set(math.pi)
    def clear_btn(self, *args):
        self.entry_var.set("0")
        self.top_var.set("")
    def clear_entry_btn(self, *args):
        self.entry_var.set("0")
    def backspace_btn(self, *args):
        entry_var = self.entry_var.get()
        if entry_var == "0":
            return
        else:
            entry_var = entry_var[0:-1]
            if entry_var == "":
                entry_var = "0"
            self.entry_var.set(entry_var)
    # 2. btn top row
    def square_root_btn(self, *args):
        value = self.entry_var.get()
        try:
            value = float(value)
        except ValueError as e:
            print(f"{e}: Could not convert value into float {value}")
        value = math.sqrt(value)
        self.entry_var.set(value)

    def open_parenthesis_btn(self, *args):
        button = "("
        top_var = self.top_var.get()

        if top_var.endswith(" = "):
            top_var = ""

        self.top_var.set(top_var + button)
        
    def close_parenthesis_btn(self, *args):
        button = ")"
        top_var = self.top_var.get()
        entry_var = self.entry_var.get()

        if top_var.endswith(" = "):
            print("test")
            top_var = ""

        open_count, close_count = 0, 0
        for x in top_var:
            if x == "(":
                open_count += 1
            elif x == ")":
                close_count += 1
        if close_count < open_count:
            self.top_var.set(top_var + entry_var + button)
            self.entry_var.set("0")
        else:
            return
    
    # Btn Operator 
    def divide_btn(self, *args):
        top_var = self.top_var.get()
        entry_var = self.entry_var.get()

        if top_var.endswith(" = "):
            top_var = ""
        self.top_var.set(top_var + f"{entry_var} / ")
        self.entry_var.set("0")
        
    def multiply_btn(self, *args):
        top_var = self.top_var.get()
        entry_var = self.entry_var.get()
        
        if top_var.endswith(" = "):
            top_var = ""
        self.top_var.set(top_var + f"{entry_var} * ")
        self.entry_var.set("0")

    def minus_btn(self, *args):
        top_var = self.top_var.get()
        entry_var = self.entry_var.get()

        if top_var.endswith(" = "):
            top_var = ""
        self.top_var.set(top_var + f"{entry_var} - ")
        self.entry_var.set("0")

    def plus_btn(self, *args):
        top_var = self.top_var.get()
        entry_var = self.entry_var.get()

        if top_var.endswith(" = "):
            top_var = ""

        self.top_var.set(top_var + f"{entry_var} + ")
        self.entry_var.set("0")

    def equal_btn(self, *args):
        top_var = self.top_var.get()
        entry_var = self.entry_var.get()

        try:
            result = eval(str(top_var + entry_var))
            self.entry_var.set(result)
            self.top_var.set(str(top_var + entry_var + " = "))
        except (SyntaxError,ValueError, ZeroDivisionError) as e:
            print(e, f"equal_btn: invalid syntax {top_var + entry_var}")

    # Btn row "+/-" and ","
    def plus_minus_btn(self, *args):
        entry_var = self.entry_var.get()
        if self.validate_entry_digits(entry_var):
            entry_var = float(entry_var)
            if entry_var < 0:
                entry_var = abs(entry_var)
            elif entry_var > 0:
                entry_var = -entry_var
            else:
                return
            self.entry_var.set(entry_var)

    def comma_btn(self, *args):
        entry_var = self.entry_var.get()
        button = "."
        if "." in entry_var:
            return
        self.entry_var.set(entry_var+button)

    # Btn numbers
    def zero_btn(self, *args):
        button = "0"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def one_btn(self, *args):
        button = "1"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def two_btn(self, *args):
        button = "2"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def three_btn(self, *args):
        button = "3"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def four_btn(self, *args):
        button = "4"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def five_btn(self, *args):
        button = "5"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def six_btn(self, *args):
        button = "6"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def seven_btn(self, *args):
        button = "7"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def eight_btn(self, *args):
        button = "8"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

    def nine_btn(self, *args):
        button = "9"
        if self.validate_entry_digits(self.entry_var.get()):
            self.entry_var.set(self.leading_zero(self.entry_var.get()+button))
        else:
            return

if __name__ == "__main__":
    App().mainloop()