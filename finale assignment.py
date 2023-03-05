# import the tkinter library.
from tkinter import*

# Calculate the BMI and round the output into 3 decimal places.
def calculate():
    weight_value = float(weight_entry.get())
    height_value = float(height_entry.get())
    bmi = weight_value/height_value**2
    if bmi<=18.5:
        output.config(text=f"{round(bmi,3)} Under weight")
    elif bmi<=24.9:
        output.config(text=f"{round(bmi,3)} Normal weight")
    elif bmi<=29.9:
        output.config(text=f"{round(bmi,3)} Overweight")
    else:
        output.config(text=f"{round(bmi,3)} Obese")

# Clear the user input data in the fields.
def clear():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    output.config(text="")
    
# create the main window
root = Tk()
root.title("UTAS BMI CALCULATOR")
root.geometry("550x400")
root.config(bg="green")

# create user instructions label 
title= Label(text="Instruction to the user: enter weight in kg, and height in cm", font=30)
title.place(x=10, y=10)
title["bg"]="green"

# create the weight label and weight input area
weight_label = Label(root, text="Weight", font=30)
weight_label.place(x=80,y= 70)
weight_label["bg"]="green"

weight_entry = StringVar()
weight_entry = Entry(root, width=35)
weight_entry.place(x= 140, y=70)

# create the height label and height input area
height_label = Label(root, text="Height", font=30)
height_label.place(x=80, y=120)
height_label["bg"]= "green"

height_entry = StringVar()
height_entry = Entry(root, width= 35)
height_entry.place(x= 140, y=120)

# create the output label output display area
output_label = Label(root, text="BMI", font=30)
output_label.place(x= 420,y= 40)
output_label["bg"]="green"

output = Label(root, font= 30)
output.place(x=380, y= 65, width= 150, height= 200)

# create the buttons to compute the body mass index
calculate_button = Button(root, text="Calculate BMI", command=calculate, font=20, width= 30)
calculate_button.place(x=80, y= 180)

clear_button = Button(root, text="Clear", command=clear, font= 20, width=30)
clear_button.place(x=80, y= 230)

#run the main loop
root.mainloop()

