import tkinter as tk

class ManDayCalculatorGUI(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Man Day Calculator")
    self.geometry("300x200")
    
    self.organization_size_label = tk.Label(self, text="Organization size:")
    self.organization_size_label.pack()
    self.organization_size_var = tk.StringVar(self)
    self.organization_size_var.set("small")
    self.organization_size_menu = tk.OptionMenu(self, self.organization_size_var, "small", "medium", "large")
    self.organization_size_menu.pack()
    
    self.complexity_label = tk.Label(self, text="Complexity:")
    self.complexity_label.pack()
    self.complexity_var = tk.StringVar(self)
    self.complexity_var.set("low")
    self.complexity_menu = tk.OptionMenu(self, self.complexity_var, "low", "medium", "high")
    self.complexity_menu.pack()
    
    self.additional_requirements_label = tk.Label(self, text="Additional requirements:")
    self.additional_requirements_label.pack()
    self.additional_requirements_var = tk.StringVar(self)
    self.additional_requirements_var.set("none")
    self.additional_requirements_menu = tk.OptionMenu(self, self.additional_requirements_var, "none", "design and development", "higher risk activities")
    self.additional_requirements_menu.pack()
    
    self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
    self.calculate_button.pack()
    
    self.result