# Youtube-Tutorial: https://www.youtube.com/watch?v=gdDI_GhIRGo

import tkinter
from tkinter import BOTH, X, Y, ttk
from tkinter import messagebox

# def enter_data():
#     accepted = accept_var.get()
    
#     if accepted=="Accepted":
#         # User info
#         firstname = manufacturer_entry.get()
#         lastname = model_entry.get()
        
#         if firstname and lastname:
#             title = title_combobox.get()
#             age = amount_spinbox.get()
#             nationality = location_combobox.get()
            
#             # Course info
#             registration_status = reg_status_var.get()
#             numcourses = numcourses_spinbox.get()
#             numsemesters = numsemesters_spinbox.get()
            
#             print("First name: ", firstname, "Last name: ", lastname)
#             print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
#             print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
#             print("Registration status", registration_status)
#             print("------------------------------------------")
#         else:
#             tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
#     else:
#         tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack(expand=True, fill=Y)

# Saving User Info
user_input_frame =tkinter.LabelFrame(frame, text="Anlage 1")
user_input_frame.grid(row= 0, column=0, padx=20, pady=10)

manufacturer_label = tkinter.Label(user_input_frame, text="Hersteller")
manufacturer_label.grid(row=0, column=0)
model_label = tkinter.Label(user_input_frame, text="Modellname")
model_label.grid(row=0, column=2)

manufacturer_entry = tkinter.Entry(user_input_frame, width=50)
model_entry = tkinter.Entry(user_input_frame, width=50)
manufacturer_entry.grid(row=0, column=1, sticky="ew")
model_entry.grid(row=0, column=3)

# title_label = tkinter.Label(user_info_frame, text="Anzahl")
# title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
# title_label.grid(row=0, column=4)
# title_combobox.grid(row=0, column=5)

amount_label = tkinter.Label(user_input_frame, text="Anzahl")
amount_spinbox = tkinter.Spinbox(user_input_frame, width=5, from_=1, to=100)
amount_label.grid(row=0, column=4)
amount_spinbox.grid(row=0, column=5)

location_label = tkinter.Label(user_input_frame, text="Standort")
location_combobox = ttk.Combobox(user_input_frame, values=["Schleswig-Holstein A", "Schleswig-Holstein B", "Schleswig-Holstein C", "Schleswig-Holstein D", "Schleswig-Holstein E", "Hamburg"])
location_label.grid(row=1, column=0)
location_combobox.grid(row=1, column=1, sticky="ew")

for widget in user_input_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# # Saving Course Info
# courses_frame = tkinter.LabelFrame(frame)
# courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# registered_label = tkinter.Label(courses_frame, text="Registration Status")

# reg_status_var = tkinter.StringVar(value="Not Registered")
# registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
#                                        variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

# registered_label.grid(row=0, column=0)
# registered_check.grid(row=1, column=0)

# numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses")
# numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
# numcourses_label.grid(row=0, column=1)
# numcourses_spinbox.grid(row=1, column=1)

# numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
# numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
# numsemesters_label.grid(row=0, column=2)
# numsemesters_spinbox.grid(row=1, column=2)

# for widget in courses_frame.winfo_children():
#     widget.grid_configure(padx=10, pady=5)

# # Accept terms
# terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
# terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# accept_var = tkinter.StringVar(value="Not Accepted")
# terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
#                                   variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
# terms_check.grid(row=0, column=0)

# # Button
# button = tkinter.Button(frame, text="Enter data", command= enter_data)
# button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()