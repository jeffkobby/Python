from tkinter import *


class UnitConverter:
    def __init__(self):
        self.window = Tk()
        self.window.title("Unit Converter")
        self.window.minsize(width=250, height=300)
        self.window.config(pady=20, padx=20)
        self.radio_variable = IntVar()
        self.radio_value = 0

        self.unit_entry = Entry(width=10)
        self.unit_entry.grid(row=0, column=1)

        self.unit_label = Label(text="from")
        self.unit_label.grid(row=0, column=2)

        self.is_equal = Label(text="is equal")
        self.is_equal.grid(row=1, column=0)

        self.converted_unit = Label(text="0")
        self.converted_unit.grid(row=1, column=1)

        self.convert_to = Label(text="to")
        self.convert_to.grid(row=1, column=2)

        self.calculate_button = Button(text="Calculate", command=self.change_conversion)
        self.calculate_button.grid(row=2, column=1)

        self.convert_to_km = Radiobutton(text="Miles to Kilometers", value=1, variable=self.radio_variable,
                                         command=self.change_conversion)
        self.convert_to_km.grid(row=3, column=1)

        self.convert_to_kg = Radiobutton(text="Pounds to Kilograms", value=2, variable=self.radio_variable,
                                         command=self.change_conversion)
        self.convert_to_kg.grid(row=4, column=1)

    def change_conversion(self):
        self.radio_value = self.radio_variable.get()
        if self.radio_value == 1:
            self.unit_label.config(text="miles")
            self.convert_to.config(text="km")
            self.calculate_button.config(command=self.miles_to_km)

        if self.radio_value == 2:
            self.unit_label.config(text="lbs")
            self.convert_to.config(text="kg")
            self.calculate_button.config(command=self.lb_to_kg)

    def miles_to_km(self):
        entry = float(self.unit_entry.get())
        km = entry * 1.609
        self.converted_unit.config(text=round(km))

    def lb_to_kg(self):
        entry = float(self.unit_entry.get())
        kg = entry / 2.205
        self.converted_unit.config(text=round(kg))


unit_converter = UnitConverter()
print(unit_converter.change_conversion())
unit_converter.window.mainloop()
