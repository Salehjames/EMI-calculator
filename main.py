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

    e1 = Entry(window, width=30, font=("Arial", 15))
    e1.insert(0, 'Enter Loan Amount')
    e1.bind('<FocusIn>', on_el_click)

    e2 = Entry(window, width=30, font=("Arial", 15))
    e2.insert(0, 'Enter Interest Rate')
    e2.bind('<FocusIn>', on_e2_click)

    def on_e3_click(event):
        """function that gets called whenever entry3 is clicked"""