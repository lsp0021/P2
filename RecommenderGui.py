#Author: Kartikey
# Latest modified date: 4/30/2024
# Description: GUI for project2


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class RecommenderGui:
    pass


class RecommenderGUI:
    def __init__(self):
        self.Recommender = RecommenderGui()

        # Create main window
        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")
        self.main_window.geometry("1200x800")

        # Create notebook
        self.notebook = ttk.Notebook(self.main_window)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Create tabs
        self.create_movie_tab()
        self.create_tv_show_tab()
        self.create_book_tab()
        self.create_search_tab()
        self.create_recommendation_tab()

        # Create buttons
        self.create_buttons()

    def create_movie_tab(self):
        movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(movie_tab, text="Movies")
        # Add widgets for displaying movie data

    def create_tv_show_tab(self):
        tv_show_tab = ttk.Frame(self.notebook)
        self.notebook.add(tv_show_tab, text="TV Shows")
        # Add widgets for displaying TV show data

    def create_book_tab(self):
        book_tab = ttk.Frame(self.notebook)
        self.notebook.add(book_tab, text="Books")
        # Add widgets for displaying book data

    def create_search_tab(self):
        search_tab = ttk.Frame(self.notebook)
        self.notebook.add(search_tab, text="Search")
        # Add widgets for searching movies and TV shows

    def create_recommendation_tab(self):
        recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(recommendation_tab, text="Recommendations")
        # Add widgets for getting recommendations

    def create_buttons(self):
        button_frame = tk.Frame(self.main_window)
        button_frame.pack()

        # Create buttons
        load_shows_button = tk.Button(button_frame, text="Load Shows", command=self.load_shows)
        load_shows_button.grid(row=0, column=0)

        load_books_button = tk.Button(button_frame, text="Load Books", command=self.load_books)
        load_books_button.grid(row=0, column=1)

        load_associations_button = tk.Button(button_frame, text="Load Associations", command=self.load_associations)
        load_associations_button.grid(row=0, column=2)

        credit_info_button = tk.Button(button_frame, text="Credit Info", command=self.credit_info_box)
        credit_info_button.grid(row=0, column=3)

        quit_button = tk.Button(button_frame, text="Quit", command=self.main_window.quit)
        quit_button.grid(row=0, column=4)

    def load_shows(self):
        # Implement loading shows
        pass

    def load_books(self):
        # Implement loading books
        pass

    def load_associations(self):
        # Implement loading associations
        pass

    def credit_info_box(self):
        # Implement credit info dialog
        pass

    def search_shows(self):
        # Implement search for movies and TV shows
        pass

    def search_books(self):
        # Implement search for books
        pass

    def get_recommendations(self):
        # Implement getting recommendations
        pass


def main():
    gui = RecommenderGUI()
    gui.main_window.mainloop()


if __name__ == "__main__":
    main()
