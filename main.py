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
    
