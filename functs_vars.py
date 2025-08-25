from os import path, mkdir
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, TclError

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
wdir = path.join(path.dirname(__file__), 'Data')
date_format = "%d-%m-%Y"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def initialize_data_folder():
    if path.exists(wdir):
        print ("Data folder found")
    else:
        print ("Data folder not found, Creating...")
        mkdir(wdir)

def get_date(date_str):
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("invalid date format.")
        return ValueError