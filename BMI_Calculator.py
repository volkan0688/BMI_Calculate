from tkinter import *

window = Tk()
window.title("BMI Calculator (by Volkan)")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20, background="orange")

# BMI Index
def bmi_calcutale():
    weight_return = my_entry_weight.get()
    height_return = my_entry_height.get()

    if not weight_return or not height_return:
        label_result.config(text="Hatalı giriş yaptınız!\nLütfen tüm alanları doldurun.")
    else:
        try:
            weight_user = int(weight_return)
            height_user = int(height_return) / 100
            bmi = round((weight_user / (height_user ** 2)), 2)
            if bmi < 15:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\nÇok ciddi derecede düşük kilolusunuz.")
            elif bmi >= 15 and bmi <= 16:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\nCiddi derecede düşük kilolusunuz.")
            elif bmi > 16 and bmi <= 18.5:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\nDüşük kilolusunuz.")
            elif bmi > 18.5 and bmi <= 25:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\nNormal (sağlıklı) kilolusunuz.")
            elif bmi > 25 and bmi <= 30:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\nFazla kilolusunuz.")
            elif bmi > 30 and bmi <= 35:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\n1. dereceden (hafif) obezsiniz.")
            elif bmi > 35 and bmi <= 40:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\n2. dereceden (ciddi) obezsiniz.")
            else:
                label_result.config(text=f"Vücut Kitle Endeksiniz: {bmi}\n3. dereceden (çok ciddi) obezsiniz.")
        except ValueError:
            label_result.config(text="Hatalı giriş yaptınız!\nLütfen geçerli bir sayı girin.")
# Weight label
my_label_weight = Label(text="Kilonuz (kg)")
my_label_weight.config(bg="orange", font=('Helvetica', 13, 'italic'))
my_label_weight.config(fg="black")
my_label_weight.config(padx=10, pady=10)
my_label_weight.pack()

# Weight entry
my_entry_weight = Entry(width=20)
my_entry_weight.config(font=('Helvetica', 13, 'italic'))
my_entry_weight.pack()
my_entry_weight.focus()

# Height label
my_label_height = Label(text="Boyunuz (cm)")
my_label_height.config(bg="orange", font=('Helvetica', 13, 'italic'))
my_label_height.config(fg="black")
my_label_height.config(padx=10, pady=10)
my_label_height.pack()

# Height entry
my_entry_height = Entry(width=20)
my_entry_height.config(font=('Helvetica', 13, 'italic'))
my_entry_height.pack()

# Button
def button_clicked():
    bmi_calcutale()

button = Button(text="Hesapla", command=button_clicked, font=('Helvetica', 13, 'italic'))
button.place(x=155, y=150)

# Label Result
label_result = Label(text="")
label_result.config(bg="orange", font=('Helvetica', 13, 'italic'))
label_result.config(fg="black")
label_result.config(padx=20, pady=10)
label_result.place(x=30, y=200)

window.mainloop()
