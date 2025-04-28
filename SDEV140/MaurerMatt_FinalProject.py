#!/usr/bin/env python3

"""

Author:  Matt Maurer
Date written: 04/27/25
Assignment:   Final Project
Short Desc:   Time Tracker

"""

import tkinter as tk
import datetime
	
def getToday():
	# get today in the calendar
	today = datetime.datetime.now()
	# format the date to be more human friendly
	friendlyToday = today.strftime("%B %d, %Y")
	return friendlyToday

def saveTime():
	print("save")

def createEntry():
	# Create a new top-level window
	saveWindow = tk.Toplevel()
	saveWindow.title("New Entry")
	saveWindow.geometry("300x200")
	
	# Add a label in the new window
	timeLabel = tk.Label(saveWindow, text="Add Time Below (in hours)")
	timeField = tk.Entry()
	
	saveButton = tk.Button(saveWindow, text="Save", command=saveTime)
	timeLabel.grid(row=0, column=0, columnspan = 2)
	saveButton.grid(row=1, column=0, columnspan = 2)
	
window = tk.Tk()
window.geometry("300x600")
window.title("Time Tracker")


mainLabel = tk.Label(window, text=getToday(), padx=5, pady=10, anchor = "w", width=35)
entryButton = tk.Button(window, text="New Entry", command=createEntry)

mainLabel.grid(row=0, column=0, columnspan = 2)
entryButton.grid(row=5, column=0, padx=10, pady=5)


window.mainloop()
