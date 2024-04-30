#Author: Paul
# Latest modified date: 4/26/2024
# Description: The back-end function of the Recommender.
import tkinter

import Recommender
import Recommender as rec
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RecommenderGUI():
    def __init__(self):
        self.__recommender = rec.Recommender()
        self.__main_window = tk.Tk()
        self.__main_window.title("Reccomender")
        self.__main_window.geometry("1200x600")
        #setting up window
        self.__notebook = ttk.Notebook(self.__main_window)
        #set up notebook

        #movies tab
        self.__movieTab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__movieTab, text="Movies")

        self.__movieText = tk.Text(self.__movieTab,wrap=tk.WORD,width=100,height=25)
        self.__movieText.pack(padx=10,pady=10)
        self.__movieText.insert(tk.END,"no moive data")
        self.__movieText.config(state=tk.DISABLED)

        #tv tab
        self.__tvTab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tvTab, text="TV shows")

        self.__tvText = tk.Text(self.__tvTab, wrap=tk.WORD, width=100, height=25)
        self.__tvText.pack(padx=10, pady=10)
        self.__tvText.insert(tk.END, "no TV show data")
        self.__tvText.config(state=tk.DISABLED)

        #book tab
        self.__bookTab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__bookTab, text="books")

        self.__bookText = tk.Text(self.__bookTab, wrap=tk.WORD, width=100, height=25)
        self.__bookText.pack(padx=10, pady=10)
        self.__bookText.insert(tk.END, "no book data")
        self.__bookText.config(state=tk.DISABLED)

        #search tab
        self.__searchTab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__searchTab, text="Search Movies & TV Shows")

        self.__searchLabel = ttk.Label(self.__searchTab, text="Search:")
        self.__searchLabel.grid(row=0, column=0, padx=10, pady=10)
        self.__searchEntry = ttk.Entry(self.__searchTab, width=50)
        self.__searchEntry.grid(row=1, column=1, padx=10, pady=10)
        self.__searchButton = ttk.Button(self.__searchTab, text="Search", command=print(1))
        self.__searchButton.grid(row=0, column=2, padx=10, pady=10)
        self.media_type_combobox = ttk.Combobox(self.__searchTab, values=["Movie", "TV Show"])
        self.media_type_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.__searchText = tk.Text(self.__searchTab, width=100, height=20)
        self.__bookText.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.__searchText.insert(tk.END, "Enter search criteria and click 'Search'.")
        self.__searchText.config(state=tk.DISABLED)

        self.__notebook.pack()

        self.__main_window.mainloop()


RecommenderGUI()
