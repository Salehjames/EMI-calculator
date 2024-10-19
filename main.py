# EMI Calculator
# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
from fpdf import FPDF

# main window created
window = Tk()
window.geometry("1000x700")
window.title("EMI Calculator")

# variable defined
firstclick1 = True
firstclick2 = True
firstclick3 = True
firstclick4 = True
firstclick5 = True
firstclick6 = True
cal_emi = 0

# defined function for start button
def def_start():
    def on_el_click(event):
        """function that gets called whenever entryl is clicked"""
        global firstclick1
        if firstclick1: # if this is the first time theu clicked it 
            firstclick1 = False
            e1.delete(0, "end") # delete all the text in the entry

def on_e2_click(event):
    """function that gets called whenever entry2 is clicked"""
    global firstclick2
    if firstclick2:
        firstclick2 = False
        e2.delete(0, "end")

def on_e3_click(event):
    """function that gets called whenever entry3 is clicked"""
    global firstclick3
    if firstclick3:   # if this is the first time they clicked  it
        firstclick3 = False
        e3.delete(0, "end")  # delete all the text on the entry

def on_e4_click(event):
    """function that gets called whenever entry4 is clicked"""
    global firstclick4
    if firstclick4:   # if this is the first time they clicked it
        firstclick4 = False
        e4.delete(0, "end")  # delete all the text on the entry

def on_e5_click(event):
    """function that gets called whenever entry5 is clicked"""
    global firstclick5
    if firstclick5:   # if this is the first time they clicked it
        firstclick5 = False
        e5.delete(0, "end")  # delete all the text on the entry

def on_e6_click(event):
    """function that gets called whenever entry6 is clicked"""
    global firstclick6
    if firstclick6:    # if this is the first time they clicked it
        firstclick6 = False
        e6.delete(0, "end")  # delete all the text on the entry

# function for generating and saving the PDF
def def_PDF():
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "", 20)
    pdf.set_text_color(0, 0, 0)
    pdf.image('images/EMI_pdf.png', x=0, y=0, w=210, h=297)
    pdf.text(55, 129, e1.get())
    pdf.text(70, 142, e2.get())
    pdf.text(60, 155, e3.get())
    pdf.text(78, 197, str(e4.get()))
    pdf.text(96, 210, str(e5.get()))
    pdf.text(93, 223, str(e6.get()))
    pdf.text(91, 264, str(cal_emi))
    pdf.output('EMI_Calculated.pdf')
    mbox.showinfo("PDF Status", "PDF Generated and Saved Successfully.")

    # function for calculating the EMI
    def def_cal():
        global cal_emi
        p = int(e4.get())
        r = int(e5.get())
        n = int(e6.get())
        cal_emi = p * (r / 1200) * ((1 + r / 1200) ** n) / (((1 + r / 1200) ** n) - 1)
        mbox.showinfo("EMI DETAILS", "Your Monthly Payment : " + str(cal_emi))

    # function for getting user details
    def def_details():
        mbox.showinfo("User Details", "Name : " + str(e1.get()) + "\n\nMobile No. : " + str(e2.get()) + "\n\nEmail ID : " + str(e3.get()))

    # new frame created
    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    # for top label
    start1 = tk.Label(f1, text="EMI CALCULATOR", font=("Arial", 50), fg="magenta")
    start1.place(x=180, y=10)

    # created entry for Name
    l1 = Label(f1, text='Name', font=("Arial", 25), fg="brown")
    l1.place(x=100, y=140)
    e1 = Entry(f1, width=30, border=2, font=("Arial", 22), bg="light yellow")
    e1.insert(0, 'Enter Your Name...')
    e1.bind('', on_e1_click)
    e1.place(x=300, y=143)

    
