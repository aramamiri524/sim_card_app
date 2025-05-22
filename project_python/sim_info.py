from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *

sim_list = read_from_file("sims.dat")

#بارگذاری داده ها در جدول
def load_data(sim_list):
    sim_list = read_from_file("sims.dat")
    for row in table.get_children():
        table.delete(row)

    for sim in sim_list:
        table.insert("", END, values=sim)

#بازنشانی فرم(آیدی جدید تولید میشود و بقیه ی موارد خالی یا صفر میشوند ،جدول دوباره باز نشانی میشود)
def reset_form():
    id.set(len(sim_list) + 1)
    number.set("")
    operator.set("")
    price.set(0)
    charge.set(0)
    owner.set("")
    load_data(sim_list)

#ذخیره سازی اطلاعات جدید
def save_btn_click():
    sim = (id.get(), number.get(), operator.get(), price.get(), charge.get(), owner.get())
    errors = sim_validator(sim)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Sim card saved")
        sim_list.append(sim)
        write_to_file("sims.dat", sim_list)
        reset_form()

#انتخاب ردیف از جدول برای ویرایش و بررسی
def table_select(x):
    selected_sim = table.item(table.focus())["values"]
    if selected_sim:
        id.set(selected_sim[0])
        number.set(selected_sim[1])
        operator.set(selected_sim[2])
        price.set(selected_sim[3])
        charge.set(selected_sim[4])
        owner.set(selected_sim[5])

#تابع ویرایش
def edit_btn_click():
    pass

#تابع حذف
def remove_btn_click():
    pass

#یک پنجره اصلی با عنوان و اندازه مشخص ساخته میشود
window = Tk()
window.title("Sim Card Registration")
window.geometry("780x320")

# تعریف و جایگذاری فایلها
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

Label(window, text="Number").place(x=20, y=60)
number = StringVar()
Entry(window, textvariable=number).place(x=80, y=60)

Label(window, text="Operator").place(x=20, y=100)
operator = StringVar()
Entry(window, textvariable=operator).place(x=80, y=100)

Label(window, text="Price").place(x=20, y=140)
price = IntVar()
Entry(window, textvariable=price).place(x=80, y=140)

Label(window, text="Charge").place(x=20, y=180)
charge = IntVar()
Entry(window, textvariable=charge).place(x=80, y=180)

Label(window, text="Owner").place(x=20, y=220)
owner = StringVar()
Entry(window, textvariable=owner).place(x=80, y=220)

# Table
table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Number")
table.heading(3, text="Operator")
table.heading(4, text="Price")
table.heading(5, text="Charge")
table.heading(6, text="Owner")

for i in range(1, 7):
    table.column(i, width=100)

table.bind("<<TreeviewSelect>>", table_select)
table.place(x=300, y=20)

# Buttons
Button(window, text="Save", width=8, command=save_btn_click).place(x=20, y=270)
Button(window, text="Edit", width=8, command=edit_btn_click).place(x=110, y=270)
Button(window, text="Remove", width=8, command=remove_btn_click).place(x=200, y=270)
Button(window, text="Clear", width=8, command=reset_form).place(x=20, y=240, width=190)

reset_form()
window.mainloop()
