#!/usr/bin/env python3

"""

Author:  Matt Maurer
Date written: 04/27/25
Assignment:   Final Project
Short Desc:   Time Tracker

"""

#importing neccessary additions
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import messagebox
from tkinter import filedialog

#creating initial window
window = tk.Tk()
window.geometry("322x425")
window.title("DayTime")
tree = ttk.Treeview(window, columns=("Desc", "Time"), show="headings")
totalLabel = tk.Label(window, text="Total Time : 0h 0m", padx=5, pady=10)
totalTime = 0
timesheet = []

#defining class
class Job:
	def __init__(self, description, time):
		self.description = description
		self.time = time

#defining method to return a human friendly date
def getToday():
	# get today in the calendar
	today = datetime.datetime.now()
	# format the date to be more human friendly
	friendlyToday = today.strftime("%B %d, %Y")
	return friendlyToday

#defining method to update the total time
def getTotal():
	# get master time count
	global totalTime
	
	totalHours = totalTime // 60
	totalMin = totalTime % 60
	totalLabel.config(text="Total Time : " + f"{totalHours}h {totalMin}m")
	
#defining method to write the current timesheet to a file
def clockOut():
	# Save the current list of jobs to a file
	print("save to file")
	filepath = filedialog.asksaveasfilename(
			defaultextension=".txt",
			filetypes=[("Text Files", "*.txt")],
			title="Timesheet")
	
	if filepath:
		with open(filepath, "w") as file:
			file.write("My Timesheet" + "\n")
			for job in timesheet:
				file.write(job.description + " - " + job.time + "\n")
		print(f"Timesheet saved to {filepath}")
	
#defining method to delete an erroroneously entered entry
def deleteEntry():
	selectedEntry = tree.selection()
	if selectedEntry:
		tree.delete(selectedEntry)
		
		index = tree.index(selectedEntry)
		if index < len(timesheet):
			del timesheet[index]

#defining a method to save the currently entered job
def saveTime(descriptionField, hourField, minField, saveWindow):
	desc = descriptionField.get()
	hourInput = hourField.get()
	minuteInput = minField.get()
	
	# doing basic validation
	if not (desc and (hourInput.isdigit() or minuteInput.isdigit())):
		messagebox.showerror("Invalid Entry", "Please check your values and try again.")
		return
	#making sure input is numerical
	if hourInput.isdigit():
		hour = hourField.get()
	else:
		messagebox.showerror("Invalid Entry", "Please check your values and try again.")
		
	if minuteInput.isdigit():
		minute = minField.get()
	else:
		messagebox.showerror("Invalid Entry", "Please check your values and try again.")
	
	hour = int(hourInput)
	minute = int(minuteInput)
	
	#making sure input is logical
	if hour < 0 or hour > 23:
		messagebox.showerror("Invalid Entry", "Hour must be between 0 and 23")
		return
	
	if minute < 0 or minute > 59:
		messagebox.showerror("Invalid Entry", "Minutes must be between 0 and 59.")
		return
	
	if not desc:
		messagebox.showerror("Invalid Entry", "Please enter a description.")
		return
	
	global totalTime
	totalTime = totalTime + ((int(hour) * 60) + int(minute))
	
	# Combine hour and minute to display
	totalTimeDisplay = f"{hour}h {minute}m"
	
	# Create a job entry and add it to the list
	job = Job(desc, totalTimeDisplay)
	timesheet.append(job)
	tree.insert("", tk.END, values=(job.description, job.time))
	
	# Clear input fields
	descriptionField.delete(0, tk.END)
	hourField.delete(0, tk.END)
	minField.delete(0, tk.END)
	
	getTotal()
	
	# Close the entry window
	saveWindow.destroy()
	
#creating the new entry window
def createEntry():
	# Create the new entry window
	saveWindow = tk.Toplevel()
	saveWindow.title("New Entry")
	saveWindow.geometry("350x245")
	
	tk.Label(saveWindow, text="Add New Entry Below:").grid(row=0, column=0, padx=15, pady=10, sticky="w")
	img3 = tk.PhotoImage(file="plus.png")
	img3 = img3.subsample(8, 8)
	add = tk.Label(saveWindow, image=img3)
	add.image = img3
	add.grid(row=0, column=1, padx=15, pady=10, sticky="e")
	
	tk.Label(saveWindow, text="Description").grid(row=1, column=0, padx=10, pady=5, columnspan=2)
	descriptionField = tk.Entry(saveWindow, width=35)
	descriptionField.grid(row=2, column=0, padx=10, pady=5, columnspan=2)
	
	tk.Label(saveWindow, text="Hours").grid(row=3, column=0, padx=10, pady=5)
	hourField = tk.Entry(saveWindow, width=15)
	hourField.grid(row=4, column=0,padx=5, pady=5)
	
	tk.Label(saveWindow, text="Minutes").grid(row=3, column=1, padx=10, pady=5)
	minField = tk.Entry(saveWindow, width=15)
	minField.grid(row=4, column=1, padx=5, pady=5)
	
	saveButton = tk.Button(saveWindow, text="Save Entry", command=lambda: saveTime(descriptionField, hourField, minField, saveWindow)
	)
	saveButton.grid(row=5, column=0, padx=10, pady=5, columnspan=2)
	
#setting up the main window
mainLabel = tk.Label(window, text=getToday(), padx=5, pady=10)
entryButton = tk.Button(window, text="New Entry", command=createEntry)
clockoutButton = tk.Button(window, text="Clock Out / Save", command=clockOut)
deleteButton = tk.Button(window, text="Delete Selected", command=deleteEntry)

#set the titles for each column in the table
tree.heading("Desc", text="Desc")
tree.heading("Time", text="Time")

#set the width of each column in the table
tree.column("Desc", width=200)
tree.column("Time", width=100)

img2 = tk.PhotoImage(file="calendar.png")
img2 = img2.subsample(6, 6)
calendar = tk.Label(window, image=img2)

# Add data
for row in timesheet:
	tree.insert("", tk.END, values=row)

# Layout the main window
mainLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")
calendar.grid(row=0, column=1, padx=10, pady=5, sticky="e")
tree.grid(row=1, column=0, columnspan = 2, padx=10, pady=5)
entryButton.grid(row=2, column=0, padx=0, pady=5)
deleteButton.grid(row=2, column=1, padx=0, pady=5)
totalLabel.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
clockoutButton.grid(row=5, column=0, columnspan = 2, padx=10, pady=5)


window.mainloop()
