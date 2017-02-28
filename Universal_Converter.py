"""
This is the project of PSIT subject
This app is the Universal Converter
use for coverting one unit to other unit in each measurement.
===========================================================
Author: Phanuwat Sutthinarodom 56070102
        Natthanan Kunchokwanit 57070035
Language: Python 2.7
===========================================================
Last Update: 14/12/2557
"""
from Tkinter import *
import tkMessageBox, ttk
class Application(Frame):
    """Create the application"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_menubar()
        self.create_widgets()

    def create_menubar(self):
        """Create the menubar"""
        self.menubar = Menu(self)
        #Create about menu
        about_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About this program", command=self.aboutmenu)
        about_menu.add_separator() #Create the separator between 2 sub class
        about_menu.add_command(label="Creator", command=self.creator)
        #Create help menu
        help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="How to use the program", command=self.helpmenu)
        self.master.config(menu=self.menubar)

    def helpmenu(self):
        """Show the help"""
        tkMessageBox.showinfo("How to use this program", "1. Choose the measurements.\n2. Enter the current unit.\n3. Select the current value.")
   
    def aboutmenu(self):
        """Show the about of this program"""
        tkMessageBox.showinfo("About This Program", "The project of PSIT subject in 2014.\nThis program is unit converter program.")
    
    def creator(self):
        """Show the creators"""
        tkMessageBox.showinfo("Creators", "Phanuwat Sutthinarodom 56070102\nNatthanan Kunchokwanit 57070035")

    def callback(self):
        """Show the message to ask user to quit the program"""
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()

    def create_widgets(self):
        """Create widgets in the window"""
        root.title("Universal Converter")
        root.resizable(False, False)
        root.config(bg="white")
        head_frame = Frame(root, bd=3, bg="Navy", relief=GROOVE)
        Label(head_frame, text="UNIVERSAL CONVERTER", font=("Trebuchet MS", 24, "bold"), fg="White", bg="Navy").pack(pady=50)
        head_frame.grid(row=0, column=0, columnspan=4, ipadx=20, sticky="ew")
        Label(root, text=" Choose the Converter ", font=("Trebuchet MS", 16, "bold"), fg="Navy", bg="White").grid(row=2, column=0, columnspan=4, ipadx=20, ipady=20)
        button_frame = Frame(root, bd=5, bg="Navy", relief=FLAT)
        self.measurements_list = ["Angle", "Area", "Bit Byte", "Density", "Electric Current", "Energy", "Force", "Fuel Consumption", "Length", "Mass", "Power", "Pressure", "Speed", "Temperature", "Time", "Volume"]
        self.measurements_dict = {"Angle": self.angle, "Area": self.area, "Bit Byte": self.bitbyte, "Density": self.density, "Electric Current": self.electriccurrent, "Energy": self.energy, "Force": self.force, "Fuel Consumption": self.fuelconsumption, "Length": self.length, "Mass": self.mass, "Power": self.power, "Pressure": self.pressure, "Speed": self.speed, "Temperature": self.temperature, "Time": self.time, "Volume": self.volume}
        for i in range(16):
            self.button = Button(button_frame, text=self.measurements_list[i], font=("Trebuchet MS", 12), width=13, fg="Navy", bg="White", relief=FLAT, overrelief=SOLID, bd=5, activebackground="Navy", activeforeground="White", command=self.measurements_dict[self.measurements_list[i]])
            self.button.grid(row=i/4+4, column=i%4, ipady=15, ipadx=15, padx=2, pady=2)
        button_frame.grid(row=3, column=0, columnspan=4, sticky="we", padx=5, pady=5)
        root.protocol("WM_DELETE_WINDOW", self.callback) #When user will quit, program will show you the messagebox

    def convert_window(self, measurements, main_unit, unit):
        """Create widget to converter window"""
        top = self.top = Toplevel(bg="Navy") #Create the new windows
        top.title(measurements) #window name
        style = ttk.Style()
        style.map("TCombobox", fieldbackground=[("readonly", "Navy")])
        style.configure("TCombobox", foreground="White", bg="Navy")
        style.configure("TSeparator", background="Navy")
        #Create the head label
        Label(top, text=measurements + " Converter", font=("Trebuchet MS", 20, "bold"), fg="white", bg="Navy").pack(pady=20)
        outer_input_frame = Frame(top, bg="White")
        input_frame = Frame(outer_input_frame, bg="White")
        #Set text box to get input from user
        Label(input_frame, text=" Enter the value", font=("Trebuchet MS", 11), fg="Navy", bg="White").grid(row=0, column=0, pady=5)
        self.v = DoubleVar()
        self.v.set(0)
        self.value = Entry(input_frame, textvariable=self.v, bg="Navy", fg="White")
        self.value.grid(row=1, column=0, padx=15, pady=5)
        ttk.Separator(input_frame, orient="horizontal").grid(row=0, column=1, rowspan=2, sticky="ns")
        #Create button for user to choose the unit        
        Label(input_frame, text="Select the unit", font=("Trebuchet MS", 11), fg="Navy", bg="White").grid(row=0, column=2, padx=20, pady=5)
        self.dropdown = ttk.Combobox(input_frame, state="readonly", values=unit, style="TCombobox")
        self.dropdown.grid(row=1, column=2, padx=15, pady=5)
        self.dropdown.set(main_unit)
        input_frame.pack(pady=20)
        outer_input_frame.pack(pady=10, padx=20)
        #Create the scroll bar        
        text_frame = Frame(top, bd=2, relief=GROOVE)
        yscrollbar = self.scrollbar = Scrollbar(text_frame)
        yscrollbar.pack(side=RIGHT, fill=Y)
        xscrollbar = self.scrollbar = Scrollbar(text_frame, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)
        self.text = Text(text_frame, wrap=NONE, width=45, height=15, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
        self.text.pack(fill=BOTH, expand=YES)
        yscrollbar.config(command=self.text.yview)
        xscrollbar.config(command=self.text.xview)
        text_frame.pack(fill=BOTH, side=BOTTOM, expand=YES, padx=5, pady=5)
        self.top.bind("<Key>", {"Angle": self.convert_angle, "Area": self.convert_area, "Bit Byte": self.convert_bitbyte, "Density": self.convert_density, "Electric Current": self.convert_electriccurrent, "Energy": self.convert_energy, "Force": self.convert_force, "Fuel Consumption": self.convert_fuelconsumption, "Length": self.convert_length, "Mass": self.convert_mass, "Power": self.convert_power, "Pressure": self.convert_pressure, "Speed": self.convert_speed, "Temperature": self.convert_temperature, "Time": self.convert_time, "Volume": self.convert_volume}[measurements])
        self.dropdown.bind("<<ComboboxSelected>>", {"Angle": self.convert_angle, "Area": self.convert_area, "Bit Byte": self.convert_bitbyte, "Density": self.convert_density, "Electric Current": self.convert_electriccurrent, "Energy": self.convert_energy, "Force": self.convert_force, "Fuel Consumption": self.convert_fuelconsumption, "Length": self.convert_length, "Mass": self.convert_mass, "Power": self.convert_power, "Pressure": self.convert_pressure, "Speed": self.convert_speed, "Temperature": self.convert_temperature, "Time": self.convert_time, "Volume": self.convert_volume}[measurements])
        self.top.bind("<Control_L>", self.copy)
        self.top.bind("<Control_R>", self.copy)

    def print_text(self, printer):
        """Print text"""
        self.text.configure(state="normal")
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
        self.text.configure(state="disabled")

    def copy(self, event):
        """Make text dont change"""
        return

    def angle(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Angle", "degree", ["arcminute", "arcsecond", "circle", "degree", "gon", "gradian", "mil(Nato)", "mil(Soviet Union)", "mil(Sweden)", "octant", "quadrant", "radian", "revolution", "sextant", "sign", "turn"])

    def convert_angle(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(degree)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"arcminute": 0.016667, "arcsecond": 0.000278, "circle": 360, "degree": 1.0, "gon": 0.9, "gradian": 0.9, "mil(Nato)": 0.05625, "mil(Soviet Union)": 0.06, "mil(Sweden)": 0.057143, "octant": 45.0, "quadrant": 90.0, "radian": 57.29578, "revolution": 360.0, "sextant": 60.0, "sign": 30.0, "turn": 360.0}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def area(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Area", "square meters", ["acres", "ares", "circular inches", "hectares", "hides", "roods", "square centimeters", "square feet(US & UK)", "square feet(US survey)", "square inches", "square kilometers", "square meters", "square miles", "square millimeters", "square of timber", "square rods or poles", "square yards", "townships"])

    def convert_area(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(square meters)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"acres": 4046.8564224, "ares" :100.0, "circular inches": 0.0005067, "hectares": 10000.0, "hides": 485000.0, "roods": 1011.7141056, "square centimeters": 0.0001, "square feet(US & UK)": 0.092803, "square feet(US survey)": 0.092803, "square inches": 0.000645, "square kilometers": 1000000.0, "square meters": 1.0, "square miles": 2589988.110336, "square millimeters": 0.000001, "square of timber": 9.280304, "square rods or poles": 25.29285264, "square yards": 0.83612736, "townships": 93239571.972}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def bitbyte(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Bit Byte", "megabytes", ["bits", "bytes", "exabits", "exabytes", "gigabits", "gigabytes", "kilobits", "kilobytes", "megabits", "megabytes", "petabits", "petabytes", "terabits", "terabytes"])

    def convert_bitbyte(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(megabytes)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"bits": 1.192093 * 10 ** -7, "bytes": 9.53674316 * 10 ** -7, "kilobits": 1.220703125 * 10 ** -4, "kilobytes": 9.765625 * 10 ** -4, "megabits": 0.125, "megabytes": 1.0, "gigabits": 128.0, "gigabytes": 1024.0, "terabits": 131072.0, "terabytes": 1048576.0, "petabits": 134217728.0, "petabytes": 1073741824.0, "exabits": 137438953472.0, "exabytes": 1099511627776.0}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def density(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Density", "kilograms/liter", ["grains/gallon(UK)", "grains/gallon(US)", "grams/cubic centimeters", "grams/liter", "grams/millimeters", "kilograms/cubic meters", "kilograms/liter", "megagrams/cubic meter", "milligrams/liter", "milligrams/millimeters", "ounces/cubic inch", "ounces/gallon(UK)", "ounces/gallon(US)", "pounds/cubic foot", "pounds/cubic inch", "pounds/gallon(UK)", "pounds/gallon(US)", "slugs/cubic foot", "tonnes/cubic meter", "tons(UK)/cubic yard", "tons(US)/cubic yard"])

    def convert_density(self,event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(kilograms/liter)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"grains/gallon(UK)": 0.0000143, "grains/gallon(US)": 0.000017, "grams/cubic centimeters": 1.0, "grams/liter": 0.001, "grams/millimeters": 1.0, "kilograms/cubic meters": 0.001, "kilograms/liter": 1.0, "megagrams/cubic meter": 1.0, "milligrams/millimeters": 0.001, "milligrams/liter": 0.000001, "ounces/cubic inch": 1.729994, "ounces/gallon(UK)": 0.006236, "ounces/gallon(US)": 0.007489, "pounds/cubic inch": 27.679904, "pounds/cubic foot": 0.016018, "pounds/gallon(UK)": 0.099776, "pounds/gallon(US)": 0.119826, "slugs/cubic foot": 0.515318, "tonnes/cubic meter": 1.0, "tons(UK)/cubic yard": 1.328939, "tons(US)/cubic yard": 1.186553}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def electriccurrent(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Electric Current", "ampere", ["EMU of current", "ESU of current", "abampere", "ampere", "biot", "centiampere", "coulomb/second", "franklin/second", "gaussian electric current", "gigaampere", "gilbert", "kiloampere", "megaampere", "microampere", "milliamp", "milliampere", "nanoampere", "picoampere", "siemens volt", "statampere", "teraampere", "volt/ohm", "watt/volt", "weber/henry"])

    def convert_electriccurrent(self, event):
        try:
            #Compare other unit to one unit(ampere)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"abampere": 10.0, "ampere": 1.0, "biot": 10.0, "centiampere": 0.01, "coulomb/second": 1.0, "EMU of current": 10.0, "ESU of current": 3.335641 * 10 ** -10, "franklin/second": 3.335641 * 10 ** -10, "gaussian electric current": 3.335641 * 10 ** -10, "gigaampere": 1.0 * 10 ** 9, "gilbert": 0.79577472, "kiloampere": 1000.0, "megaampere": 1000000.0, "microampere": 0.000001, "milliampere": 0.001, "milliamp": 0.001, "nanoampere": 1.0 * 10 ** -9, "picoampere": 1.0 * 10 ** 12, "siemens volt": 1.0,  "statampere": 3.335641 * 10 ** -10, "teraampere": 1.0 * 10 ** 12, "volt/ohm": 1.0, "watt/volt": 1.0, "weber/henry": 1.0}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def energy(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Energy", "joules", ["Btu(mean)", "Btu(th)", "calories(15C)", "calories(20C)", "calories(IT)", "calories(food)", "calories(mean)", "calories(th)", "centigrade heat units", "electron volts", "ergs", "foot poundals", "foot-pound force", "gigajoules", "horsepower hours", "inch-pound force", "joules", "kilocalories(IT)", "kilocalories(th)", "kilogram-force meters", "kilojoules", "kilowatt hours", "megajoules", "newton meters", "therms", "watt hours", "watt seconds"])

    def convert_energy(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(joules)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"Btu(th)": 1054.35, "Btu(mean)": 1055.87, "calories(IT)": 4.1868, "calories(th)": 4.184, "calories(mean)": 4.19002, "calories(15C)": 4.1858, "calories(20C)": 4.1819, "calories(food)": 4186.0, "centigrade heat units": 1900.4, "electron volts": 1.60219 * 10 ** -19, "ergs": 1.0 * 10 ** -7, "foot-pound force": 1.355818, "foot poundals": 0.04214, "gigajoules": 1.0 * 10 ** 9, "horsepower hours": 2684520.0, "inch-pound force": 0.112985, "joules": 1.0, "kilocalories(IT)": 4186.8, "kilocalories(th)": 4184.0, "kilogram-force meters": 9.80665, "kilojoules": 1000.0, "kilowatt hours": 3600000.0, "megajoules": 1.0 * 10 ** 6, "newton meters": 1.0, "therms": 105505585.257348, "watt seconds": 1.0, "watt hours" : 3600.0}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def force(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Force", "newtons", ["dynes", "kilograms force", "kilonewtons", "kips", "meganewtons", "newtons", "poundals", "pounds force", "sthene", "tonnes force", "tons force(UK)", "tons force(US)"])

    def convert_force(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(newtons)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"dynes": 0.00001, "kilograms force": 9.80665, "kilonewtons": 1000.0, "kips": 4448.222, "meganewtons": 1.0 * 10 ** 6, "newtons": 1.0, "pounds force": 4.448222, "poundals": 0.138255, "sthene": 1000.0, "tonnes force": 9806.65, "tons force(UK)": 9964.016418, "tons force(US)": 8896.443231}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def fuelconsumption(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Fuel Consumption", "liters/100 kilometer", ["car(2014 US Average)", "gallon(UK)/100 miles", "gallon(US)/100 miles", "kilometer/liter", "liters/100 kilometer", "liters/meter", "miles/gallon(UK)", "miles/gallon(US)"])

    def convert_fuelconsumption(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(liters/100 kilometer)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            if current_value != 0:
                unit_comp = {"car(2014 US Average)": 9.260417, "gallon(UK)/100 miles": 2.824809, "gallon(US)/100 miles": 2.352146, "kilometer/liter": 100.0 / (current_value ** 2), "liters/100 kilometer": 1.0, "liters/meter": 100000.0, "miles/gallon(UK)": 282.480936 / (current_value ** 2), "miles/gallon(US)": 235.214583 / (current_value ** 2)}
            else: #In case current_value == 0, it will error coz number division by zero.
                unit_comp = {"car(2014 US Average)": 1.0, "gallon(UK)/100 miles": 1.0, "gallon(US)/100 miles": 1.0, "kilometer/liter": 1.0, "liters/100 kilometer": 1.0, "liters/meter": 1.0, "miles/gallon(UK)": 1.0, "miles/gallon(US)": 1.0}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def length(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Length", "meters", ["Scandinavian mile", "angstroms", "au", "barleycorns", "cables", "centimeters", "chains", "decimeters", "ells", "ems", "fathoms", "feet(UK & US)", "feet(US survey)", "furlongs", "hands", "hectometers", "inches", "kilometers", "links", "light years", "meters", "micrometers", "mil", "miles(UK & US)", "miles(nautical, UK)", "miles(nautical, international)", "millimeters", "nanometers", "parsecs", "pica", "picometers", "rods", "spans", "thou", "yards"])

    def convert_length(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(meters)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"angstroms": 10 ** -10, "au": 149598550000.0, "barleycorns": 0.008467, "cables": 182.88, "centimeters": 0.01, "chains": 20.11684, "decimeters": 0.1, "ells": 0.875, "ems" : 0.004233, "fathoms": 1.8288, "feet(UK & US)": 0.3048,  "feet(US survey)": 0.304801, "furlongs": 201.168, "hands": 0.1016, "hectometers": 100.0, "inches": 0.0254, "kilometers": 1000.0, "light years": 9460528405000000.0, "meters": 1.0, "micrometers": 0.000001, "mil": 0.0000254, "miles(UK & US)": 1609.344, "miles(nautical, international)": 1852.0, "miles(nautical, UK)": 1853.184, "millimeters": 0.001, "nanometers": 10 ** -9, "parsecs": 30856776000000000.0, "picometers": 10 ** -12, "Scandinavian mile": 10000.0, "thou": 0.0000254, "yards": 0.9144, "links": 0.2011684, "pica": 0.00423333, "rods": 5.0292, "spans": 0.2286}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def mass(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Mass", "kilograms", ["Earth masses", "Solar masses", "carats", "cental", "decagrams", "femtograms", "grains", "grams", "hectograms", "hundredweights", "kilograms", "kilotonnes", "megatonnes", "micrograms", "milligrams", "nanograms", "ounces(US & UK)", "ounces(precious metals)", "picograms", "pounds(US & UK)", "pounds(precious metals)", "slugs", "stones", "tonnes(metric)", "tons(UK)", "tons(US)"])

    def convert_mass(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(kilograms)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"Earth masses": 5.97219e+24, "Solar masses": 1.9890000000000002e+30, "carats": 0.0002, "cental": 45.359237, "decagrams": 0.01, "femtograms": 1e-18, "grains": 6.479891000000001e-05, "grams": 0.001, "hectograms": 0.1, "hundredweights": 50.802345, "kilograms": 1.0, "kilotonnes": 1000000.0, "megatonnes": 1000000000.0, "micrograms": 1e-09, "milligrams": 1e-06, "nanograms": 1e-12, "ounces(US & UK)": 0.02835, "ounces(precious metals)": 0.031103, "picograms": 1e-15, "pounds(US & UK)": 0.453592, "pounds(precious metals)": 0.373242, "slugs": 14.593903, "stones": 6.350293, "tonnes(metric)": 1000.0, "tons(UK)": 1016.046909, "tons(US)": 907.18474}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def power(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Power", "joules/second", ["Btu/hour", "Btu/minute", "Btu/second", "calories(th)/hour", "calories(th)/minute", "calories(th)/second", "foot pounds-force/minute", "foot pounds-force/second", "gigawatts", "horsepowers(electric)", "horsepowers(international)", "horsepowers(metric)", "horsepowers(water)", "joules/hour", "joules/minute", "joules/second", "kilocalories(th)/hour", "kilocalories(th)/minute", "kilogram-force meters/hour", "kilograms-force meters/minute", "kilowatts", "megawatts", "petawatts", "terawatts", "watts"])

    def convert_power(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(joules/second)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"Btu/hour": 0.293071, "Btu/minute": 17.584267, "Btu/second": 1055.056, "calories(th)/hour": 0.001162, "calories(th)/minute": 0.069733, "calories(th)/second": 4.184, "foot pounds-force/minute": 0.022597, "foot pounds-force/second": 1.35582, "gigawatts": 1000000000.0, "horsepowers(electric)": 746.0, "horsepowers(international)": 745.699872, "horsepowers(metric)": 735.4988, "horsepowers(water)": 746.043, "joules/hour": 0.000278, "joules/minute": 0.016667, "joules/second": 1.0, "kilocalories(th)/hour": 1.162222, "kilocalories(th)/minute": 69.733333, "kilogram-force meters/hour": 0.002724, "kilograms-force meters/minute": 0.163444, "kilowatts": 1000.0, "megawatts": 1000000.0, "petawatts": 1000000000000000.0, "terawatts": 1000000000000.0, "watts": 1.0}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def pressure(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Pressure", "pascals", ["atm", "bars", "centimeters mercury", "centimeters water", "feet of water", "hectopascals", "inches of mercury", "inches of water", "kilogram-force/sq.centimeter", "kilogram-force/sq.meter", "kilonewtons/sq.meter", "kilonewtons/sq.millimeter", "kilopascals", "kips/sq.inch", "meganewtons/sq.meter", "meganewtons/sq.millimeter", "meters of water", "millibars", "millimeters of mercury", "millimeters of water", "newtons/sq.centimeter", "newtons/sq.meter", "newtons/sq.millimeter", "pascals", "poundals/sq.foot", "pounds-force/sq.foot", "pounds-force/sq.inch", "tonnes-force/sq.cm", "tonnes-force/sq.meter", "tons(UK)-force/sq.foot", "tons(UK)-force/sq.inch", "tons(US)-force/sq.foot", "tons(US)-force/sq.inch", "torr"])

    def convert_pressure(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(pascals)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"atm": 101325.0, "bars": 100000.0, "centimeters mercury": 1333.22, "centimeters water": 98.0665, "feet of water": 2989.06692, "hectopascals": 100.0, "inches of mercury": 3386.388, "inches of water": 249.08891, "kilogram-force/sq.centimeter": 98066.5, "kilogram-force/sq.meter": 9.80665, "kilonewtons/sq.meter": 1000.0, "kilonewtons/sq.millimeter": 1000000000.0, "kilopascals": 1000.0, "kips/sq.inch": 6894760.0, "meganewtons/sq.meter": 1000000.0, "meganewtons/sq.millimeter": 1000000000000.0, "meters of water": 9806.65, "millibars": 100.0, "millimeters of mercury": 133.322, "millimeters of water": 9.80665, "newtons/sq.centimeter": 10000.0, "newtons/sq.meter": 1.0, "newtons/sq.millimeter": 1000000.0, "pascals": 1.0, "poundals/sq.foot": 1.44816, "pounds-force/sq.foot": 47.88, "pounds-force/sq.inch": 6894.757, "tonnes-force/sq.cm": 98066500.0, "tonnes-force/sq.meter": 9806.65, "tons(UK)-force/sq.foot": 107251.0, "tons(UK)-force/sq.inch": 15444280.0, "tons(US)-force/sq.foot": 95760.0, "tons(US)-force/sq.inch": 13789500.0, "torr": 133.322}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def speed(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Speed", "meters/second", ["Mach number", "Nm/24hr", "centimeters/minute", "centimeters/second", "feet/hour", "feet/minute", "feet/second", "inches/minute", "inches/second", "kilometers/hour", "kilometers/second", "knots", "meters/hour", "meters/minute", "meters/second", "miles/hour", "miles/minute", "miles/second", "nautical miles/hour", "speed of light", "speed of sound", "yards/hour", "yards/minute", "yards/second"])

    def convert_speed(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(meters/second)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"Mach number": 340.2933, "Nm/24hr": 0.021435, "centimeters/minute": 0.000167, "centimeters/second": 0.01, "feet/hour": 8.5e-05, "feet/minute": 0.00508, "feet/second": 0.3048, "inches/minute": 0.000423, "inches/second": 0.0254, "kilometers/hour": 0.277778, "kilometers/second": 1000.0, "knots": 0.514444, "meters/hour": 0.000278, "meters/minute": 0.016667, "meters/second": 1.0, "miles/hour": 0.44704, "miles/minute": 26.8224, "miles/second": 1609.344, "nautical miles/hour": 0.514444, "speed of light": 299790000.0, "speed of sound": 343.0, "yards/hour": 0.000254, "yards/minute": 0.01524, "yards/second": 0.9144}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def temperature(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Temperature", "Celsius", ["Celsius", "Fahrenheit", "Kelvin", "Rankine", "Reaumur", "Newton", "Romer", "Delisle"])

    def convert_temperature(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(celsius) then compare that unit to celsius
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"Celsius": current_value * 1.0, "Fahrenheit": (current_value - 32) / 1.8, "Kelvin": current_value - 273.15, "Reaumur": current_value / 0.8, "Rankine": (current_value - 491.67) / 1.8, "Newton": current_value / 0.33, "Romer": (current_value - 7.5) / 0.525, "Delisle": 100 - current_value * 0.66666667}
            new_value={"Celsius": unit_comp[current_unit], "Fahrenheit": unit_comp[current_unit] * 1.8 + 32, "Kelvin": unit_comp[current_unit] + 273.15, "Reaumur": unit_comp[current_unit] * 0.8, "Rankine": unit_comp[current_unit] * 1.8 + 491.67, "Newton": unit_comp[current_unit] * 0.33, "Romer": unit_comp[current_unit] * 0.525 + 7.5, "Delisle": (100 - unit_comp[current_unit]) * 1.5}
            printer = "Value is invalid."
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(new_value[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def time(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Time", "seconds", ["centuries", "days", "decades", "femtoseconds", "fortnights", "hours", "microseconds", "millenia", "milliseconds", "minutes", "months(Common)", "months(Synodic)", "nanoseconds", "picoseconds", "quarters(Common)", "seconds", "shakes", "weeks", "years(Average Gregorian)", "years(Common)", "years(Julian)", "years(Leap)", "years(Tropical)"])

    def convert_time(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(seconds)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"centuries": 3153600000.0, "days": 86400.0, "decades": 315360000.0, "femtoseconds": 1e-15, "fortnights": 1209600.0, "hours": 3600.0, "microseconds": 1e-06, "millenia": 31536000000.0, "milliseconds": 0.001, "minutes": 60.0, "months(Common)": 2628000.0, "months(Synodic)": 2551442.8896, "nanoseconds": 1e-09, "picoseconds": 1e-12, "quarters(Common)": 7884000.0, "seconds": 1.0, "shakes": 1e-08, "weeks": 604800.0, "years(Average Gregorian)": 31556952.0, "years(Common)": 31536000.0, "years(Julian)": 31557600.0, "years(Leap)": 31622400.0, "years(Tropical)": 31556925.216}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

    def volume(self):
        """Call the convert_window function and send the identity data"""
        self.convert_window("Volume", "cubic decimeters", ["acre foot", "barrels", "bushels(UK)", "bushels(US)", "centiliters", "cubic centimeters", "cubic decameters", "cubic decimeters", "cubic feet", "cubic inches", "cubic kilometers", "cubic meters", "cubic mile", "cubic millimeters", "cubic yards", "cups", "deciliters", "dram", "dram(imperial)", "fluid ounces(US)", "fluid ounces(imperial)", "gallons(US,dry)", "gallons(US,liquid)", "gallons(imperial)", "gill(US)", "gill(imperial)", "liters", "liters(1901-1964)", "microliters", "milliliters", "nanoliters", "picoliters", "pints(US,dry)", "pints(US,liquid)", "pints(imperial)", "quarts(UK,dry)", "quarts(US,liquid)", "quarts(imperial)", "table spoons", "tea spoons"])

    def convert_volume(self, event):
        """Return the converted value and new unit."""
        try:
            #Compare other unit to one unit(cubic decimeters)
            current_value, current_unit = float("0" + str(self.v.get())), self.dropdown.get()
            unit_comp = {"acre foot": 1233481.837548, "barrels": 158.987295, "bushels(UK)": 36.36872, "bushels(US)": 35.23907, "centiliters": 0.01, "cubic centimeters": 0.001, "cubic decameters": 1000000.0, "cubic decimeters": 1.0, "cubic feet": 28.316847, "cubic inches": 0.016387, "cubic kilometers": 1000000000000.0, "cubic meters": 1000.0, "cubic mile": 4168181825000.0, "cubic millimeters": 1e-06, "cubic yards": 764.554858, "cups": 0.236588, "deciliters": 0.1, "dram": 0.003697, "dram(imperial)": 0.003552, "fluid ounces(US)": 0.029574, "fluid ounces(imperial)": 0.028413, "gallons(US,dry)": 4.404884, "gallons(US,liquid)": 3.785412, "gallons(imperial)": 4.54609, "gill(US)": 0.118294, "gill(imperial)": 0.142065, "liters": 1.0, "liters(1901-1964)": 1.000028, "microliters": 1e-06, "milliliters": 0.001, "nanoliters": 1e-09, "picoliters": 1e-12, "pints(US,dry)": 0.55061, "pints(US,liquid)": 0.473176, "pints(imperial)": 0.568261, "quarts(UK,dry)": 1.101221, "quarts(US,liquid)": 0.946353, "quarts(imperial)": 1.136523, "table spoons": 0.014787, "tea spoons": 0.004929}
            value_comp, printer = current_value * unit_comp[current_unit], ""
            unit_list = sorted(unit_comp.keys())
            unit_list.remove(current_unit)
            for unit in unit_list:
                printer += "To %s " % unit + " " * (max([len(i) for i in unit_list]) - len(unit)) + str(value_comp / unit_comp[unit]) + ["", "\n"][unit_list[-1] != unit]
        except ValueError: #In case user enter the other type of value, not Int or Float
            printer = "Value is invalid."
        self.print_text(printer)

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()