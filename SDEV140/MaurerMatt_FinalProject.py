#!/usr/bin/env python3

"""

Author:  Matt Maurer
Date written: 04/27/25
Assignment:   Final Project
Short Desc:   Time Tracker

"""

import tkinter as tk
from tkinter import ttk
import datetime

window = tk.Tk()
window.geometry("300x350")
window.title("DayTime")
tree = ttk.Treeview(window, columns=("Desc", "Time"), show="headings")

class Job:
	def __init__(self, description, time):
		self.description = description
		self.time = time
	
def getToday():
	# get today in the calendar
	today = datetime.datetime.now()
	# format the date to be more human friendly
	friendlyToday = today.strftime("%B %d, %Y")
	return friendlyToday

def clockOut():
	# Save the current list of jobs to a file
	print("save to file")

def saveTime(descriptionField, hourField, minField, saveWindow):
	desc = descriptionField.get()
	hour = hourField.get()
	minute = minField.get()
	
	if not (desc and (hour.isdigit() or minute.isdigit())):
		return  # basic validation
	
	# Combine hour and minute to display
	total_time = f"{hour}h {minute}m"
	
	# Create a job entry and add it to the list
	job = Job(desc, total_time)
	timesheet.append(job)
	tree.insert("", tk.END, values=(job.description, job.time))
	
	# Clear input fields
	descriptionField.delete(0, tk.END)
	hourField.delete(0, tk.END)
	minField.delete(0, tk.END)
	
	# Close the entry window
	saveWindow.destroy()
	
def createEntry():
	# Create the new entry window
	saveWindow = tk.Toplevel()
	saveWindow.title("New Entry")
	saveWindow.geometry("215x290")
	
	tk.Label(saveWindow, text="Add New Entry Below:").grid(row=0, column=0, padx=10, pady=5)
	
	tk.Label(saveWindow, text="Description").grid(row=1, column=0, padx=10, pady=5)
	descriptionField = tk.Entry(saveWindow)
	descriptionField.grid(row=2, column=0, padx=10, pady=5)
	
	
	tk.Label(saveWindow, text="Hours").grid(row=3, column=0, padx=10, pady=5)
	hourField = tk.Entry(saveWindow)
	hourField.grid(row=4, column=0, padx=10, pady=5)
	
	tk.Label(saveWindow, text="Minutes").grid(row=5, column=0, padx=10, pady=5)
	minField = tk.Entry(saveWindow)
	minField.grid(row=6, column=0, padx=10, pady=5)
	
	saveButton = tk.Button(saveWindow, text="Save", command=lambda: saveTime(descriptionField, hourField, minField, saveWindow)
	)
	saveButton.grid(row=7, column=0, padx=10, pady=5)
	

mainLabel = tk.Label(window, text=getToday(), padx=5, pady=10)
entryButton = tk.Button(window, text="New Entry", command=createEntry)
clockoutButton = tk.Button(window, text="Clock Out / Save", command=clockOut)


# Define column headings
tree.heading("Desc", text="Desc")
tree.heading("Time", text="Time")

# Define columns' widths (optional)
tree.column("Desc", width=200)
tree.column("Time", width=100)

# Add data
timesheet = []
for row in timesheet:
	tree.insert("", tk.END, values=row)

# Layout the main window
mainLabel.grid(row=0, column=0, columnspan = 2)
tree.grid(row=1, column=0, columnspan = 2)
entryButton.grid(row=2, column=0, columnspan = 2, padx=10, pady=5)
clockoutButton.grid(row=4, column=0, columnspan = 2, padx=10, pady=25)


window.mainloop()
