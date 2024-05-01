# Author: Kartikey, Suqi Lu, Paul
# Latest modified date: 5/1/2024
# Description: GUI for project2

from Recommender import Recommender
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RecommenderGUI:
    def __init__(self):
        self.Recommender = Recommender()

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

        # create two text area. One is list, other is stats summary
        self.MovieList_area = tk.Text(movie_tab, wrap=tk.WORD)
        self.MovieStat_area = tk.Text(movie_tab, wrap=tk.WORD)

        self.MovieList_area.grid(row=0, column=0, sticky="nsew")

        # Create a Scrollbar and attach it to text_area
        scrollbar = tk.Scrollbar(movie_tab, orient="vertical", command=self.MovieList_area.yview)

        # Configure the Text widget to scroll with the Scrollbar
        self.MovieList_area.configure(yscrollcommand=scrollbar.set)

        self.MovieStat_area.grid(row=1, column=0, sticky="nsew")

        # Configure the row weights to allocate space percentages
        movie_tab.grid_rowconfigure(0, weight=7)  # 60% of the space
        movie_tab.grid_rowconfigure(1, weight=3)  # 40% of the space
        movie_tab.grid_columnconfigure(0, weight=1)  # Ensure the column expands to fill the tab

        # minimum sizes for minimum requirement for visibility
        self.MovieList_area.grid_propagate(False)
        self.MovieStat_area.grid_propagate(False)

        self.notebook.add(movie_tab, text="Movies")

        # Add widgets for displaying movie data

    def create_tv_show_tab(self):
        tv_show_tab = ttk.Frame(self.notebook)

        # create two text area. One is list, other is stats summary
        self.TVShowList_area = tk.Text(tv_show_tab, wrap=tk.WORD)
        self.TVShowStat_area = tk.Text(tv_show_tab, wrap=tk.WORD)

        self.TVShowList_area.grid(row=0, column=0, sticky="nsew")

        # Create a Scrollbar and attach it to text_area
        scrollbar = tk.Scrollbar(tv_show_tab, orient="vertical", command=self.TVShowList_area.yview)

        # Configure the Text widget to scroll with the Scrollbar
        self.TVShowList_area.configure(yscrollcommand=scrollbar.set)

        self.TVShowStat_area.grid(row=1, column=0, sticky="nsew")

        # Configure the row weights to allocate space percentages
        tv_show_tab.grid_rowconfigure(0, weight=7)  # 60% of the space
        tv_show_tab.grid_rowconfigure(1, weight=3)  # 40% of the space
        tv_show_tab.grid_columnconfigure(0, weight=1)  # Ensure the column expands to fill the tab

        # minimum sizes for minimum requirement for visibility
        self.TVShowList_area.grid_propagate(False)
        self.TVShowList_area.grid_propagate(False)

        self.notebook.add(tv_show_tab, text="TV Shows")
        # Add widgets for displaying TV show data

    def create_book_tab(self):
        book_tab = ttk.Frame(self.notebook)

        # create two text area. One is list, other is stats summary
        self.BookList_area = tk.Text(book_tab, wrap=tk.WORD)
        self.BookStat_area = tk.Text(book_tab, wrap=tk.WORD)

        self.BookList_area.grid(row=0, column=0, sticky="nsew")

        # Create a Scrollbar and attach it to text_area
        scrollbar = tk.Scrollbar(book_tab, orient="vertical", command=self.BookList_area.yview)

        # Configure the Text widget to scroll with the Scrollbar
        self.BookList_area.configure(yscrollcommand=scrollbar.set)

        self.BookStat_area.grid(row=1, column=0, sticky="nsew")

        # Configure the row weights to allocate space percentages
        book_tab.grid_rowconfigure(0, weight=7)  # 60% of the space
        book_tab.grid_rowconfigure(1, weight=3)  # 40% of the space
        book_tab.grid_columnconfigure(0, weight=1)  # Ensure the column expands to fill the tab

        # minimum sizes for minimum requirement for visibility
        self.BookList_area.grid_propagate(False)
        self.BookStat_area.grid_propagate(False)
        
        self.notebook.add(book_tab, text="Books")
        # Add widgets for displaying book data

    def create_search_tab(self):

        # adding search movie/TV Show tab
        search_show_tab = ttk.Frame(self.notebook)

        # Upper part of search
        search_show_upper =  tk.Frame(search_show_tab)

        search_ShowType_Frame = tk.Frame(search_show_upper)
        showType_options = ["Movie", "TV Show"]
        self.search_ShowType_Label = tk.Label(search_ShowType_Frame, text=" Type: ")
        self.search_ShowType_box = ttk.Combobox(search_ShowType_Frame, values=showType_options)

        search_ShowTitle_Frame = tk.Frame(search_show_upper)
        self.search_ShowTitle_Field = tk.Entry(search_ShowTitle_Frame, width=40)
        self.search_ShowTitle_Label = tk.Label(search_ShowTitle_Frame, text=" Title: ")

        search_ShowDirector_Frame = tk.Frame(search_show_upper)
        self.search_ShowDirector_Field = tk.Entry(search_ShowDirector_Frame, width=40)
        self.search_ShowDirector_Label= tk.Label(search_ShowDirector_Frame, text=" Director: ")

        search_ShowActor_Frame = tk.Frame(search_show_upper)
        self.search_ShowActor_Field = tk.Entry(search_ShowActor_Frame, width=40)
        self.search_ShowActor_Label = tk.Label(search_ShowActor_Frame, text=" Actor: ")

        search_ShowGenre_Frame = tk.Frame(search_show_upper)
        self.search_ShowGenre_Field = tk.Entry(search_ShowGenre_Frame, width=40)
        self.search_ShowGenre_Label = tk.Label(search_ShowGenre_Frame, text=" Genre: ")

        self.search_searchShow_button = tk.Button(search_show_upper, text="Search", command=self.search_shows)

        # Packing the widgets in their single frame
        
        self.search_ShowType_Label.pack(side=tk.LEFT)
        self.search_ShowType_box.pack(side=tk.LEFT)

        self.search_ShowTitle_Label.pack(side=tk.LEFT)
        self.search_ShowTitle_Field.pack(side=tk.LEFT)
        
        self.search_ShowDirector_Label.pack(side=tk.LEFT)
        self.search_ShowDirector_Field.pack(side=tk.LEFT)

        self.search_ShowActor_Label.pack(side=tk.LEFT)
        self.search_ShowActor_Field.pack(side=tk.LEFT)

        self.search_ShowGenre_Label.pack(side=tk.LEFT)
        self.search_ShowGenre_Field.pack(side=tk.LEFT)

        # Packing search part widgets to upper frame
        search_ShowType_Frame.pack(side=tk.TOP, fill=tk.X)
        search_ShowTitle_Frame.pack(side=tk.TOP, fill=tk.X)
        search_ShowDirector_Frame.pack(side=tk.TOP, fill=tk.X)
        search_ShowActor_Frame.pack(side=tk.TOP, fill=tk.X)
        search_ShowGenre_Frame.pack(side=tk.TOP, fill=tk.X)
        self.search_searchShow_button.pack(side=tk.LEFT, fill=tk.NONE, expand=False)
        
        # Lower part of search. Display the search shows list based on the keyword
        search_show_lower = tk.Frame(search_show_tab)
        self.search_ShowList_area = tk.Text(search_show_lower, wrap=tk.WORD)
        self.search_ShowList_area.pack(fill=tk.BOTH, expand=True)

        # Packing upper and lower parts
        search_show_upper.pack(side=tk.TOP, fill=tk.X)  # Fill X direction, allow expanding
        search_show_lower.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Fill both and expand

        self.notebook.add(search_show_tab, text="Search Movies/TV")



        # add search Book tab
        search_book_tab = ttk.Frame(self.notebook)

        # Upper part of search
        search_book_upper =  tk.Frame(search_book_tab)

        search_BookTitle_Frame = tk.Frame(search_book_upper)
        self.search_BookTitle_Field = tk.Entry(search_BookTitle_Frame, width=40)
        self.search_BookTitle_Label = tk.Label(search_BookTitle_Frame, text=" Title: ")

        search_BookAuthor_Frame = tk.Frame(search_book_upper)
        self.search_BookAuthor_Field = tk.Entry(search_BookAuthor_Frame, width=40)
        self.search_BookAuthor_Label= tk.Label(search_BookAuthor_Frame, text=" Author: ")
        
        search_BookPublisher_Frame = tk.Frame(search_book_upper)
        self.search_BookPublisher_Field = tk.Entry(search_BookPublisher_Frame, width=40)
        self.search_BookPublisher_Label = tk.Label(search_BookPublisher_Frame, text=" Publisher: ")

        self.search_searchBook_button = tk.Button(search_book_upper, text="Search", command=self.search_books)

        # Packing the widgets in their single frame
        
        self.search_BookTitle_Label.pack(side=tk.LEFT)
        self.search_BookTitle_Field.pack(side=tk.LEFT)

        self.search_BookAuthor_Label.pack(side=tk.LEFT)
        self.search_BookAuthor_Field.pack(side=tk.LEFT)
        
        self.search_BookPublisher_Label.pack(side=tk.LEFT)
        self.search_BookPublisher_Field.pack(side=tk.LEFT)

        # Packing search part widgets to upper frame
        search_BookTitle_Frame.pack(side=tk.TOP, fill=tk.X)
        search_BookAuthor_Frame.pack(side=tk.TOP, fill=tk.X)
        search_BookPublisher_Frame.pack(side=tk.TOP, fill=tk.X)
        self.search_searchBook_button.pack(side=tk.LEFT, fill=tk.NONE, expand=False)
        
        # Lower part of search. Display the search shows list based on the keyword
        search_book_lower = tk.Frame(search_book_tab)
        self.search_BookList_area = tk.Text(search_book_lower, wrap=tk.WORD)
        self.search_BookList_area.pack(fill=tk.BOTH, expand=True)

        # Packing upper and lower parts
        search_book_upper.pack(side=tk.TOP, fill=tk.X)  # Fill X direction, allow expanding
        search_book_lower.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Fill both and expand

        self.notebook.add(search_book_tab, text="Search Books")


    def create_recommendation_tab(self):
        recommendation_tab = ttk.Frame(self.notebook)

        # Upper part of search
        search_rec_upper =  tk.Frame(recommendation_tab)

        RecType_options = ["Movie", "TV Show", "Book"]
        
        search_recType_Frame = tk.Frame(search_rec_upper)
        self.search_recType_box = ttk.Combobox(search_recType_Frame, values=RecType_options)
        self.search_recType_Label = tk.Label(search_recType_Frame, text="Type")

        search_recTitle_Frame = tk.Frame(search_rec_upper)
        self.search_recTitle_Field = tk.Entry(search_recTitle_Frame, width=40)
        self.search_recTitle_Label = tk.Label(search_recTitle_Frame, text="Title")

        self.search_rec_button = tk.Button(search_rec_upper, text="Get Recommendation", command=self.get_recommendations)

        # Packing the widgets in their single frame
        
        self.search_recType_Label.pack(side=tk.LEFT)
        self.search_recType_box.pack(side=tk.LEFT)

        self.search_recTitle_Label.pack(side=tk.LEFT)
        self.search_recTitle_Field.pack(side=tk.LEFT)

        # Packing search part widgets to upper frame
        search_recType_Frame.pack(side=tk.TOP, fill=tk.X)
        search_recTitle_Frame.pack(side=tk.TOP, fill=tk.X)
        self.search_rec_button.pack(side=tk.LEFT, fill=tk.NONE, expand=False)
        
        # Lower part of search. Display the search shows list based on the keyword
        search_rec_lower = tk.Frame(recommendation_tab)
        self.search_recList_area = tk.Text(search_rec_lower, wrap=tk.WORD)
        self.search_recList_area.pack(fill=tk.BOTH, expand=True)

        # Packing upper and lower parts
        search_rec_upper.pack(side=tk.TOP, fill=tk.X)  # Fill X direction, allow expanding
        search_rec_lower.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Fill both and expand

        self.notebook.add(recommendation_tab, text="Recommendations")

    def create_pieChart(self):
        pieChart_tab = ttk.Frame(self.notebook)

        self.notebook.add(pieChart_tab, text="Pie Chart")

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
        self.Recommender.loadShows()

        # clean the original area
        self.TVShowList_area.delete("1.0", tk.END)
        self.TVShowStat_area.delete("1.0", tk.END)
        self.MovieList_area.delete("1.0", tk.END)
        self.MovieStat_area.delete("1.0", tk.END)

        self.TVShowList_area.insert(tk.END, self.Recommender.getTVList())
        self.MovieList_area.insert(tk.END, self.Recommender.getMovieList())

        # insert movie list stats
        count, rating_count, average_duration, most_director, most_actor, most_genre = self.Recommender.getMovieStats()

        stat = "Ratings:\n"

        for rating, count_current in rating_count.items():

            percent = count_current * 100/ count
            stat += f"{rating}  {percent:.2f}\n"
            
        stat += f"\nAverage Movie Duration: {average_duration}\n\n"
        stat += f"Most Prolific Director: {most_director}\n\n"
        stat += f"Most Prolific Actor: {most_actor}\n\n"
        stat += f"Most Frequent Genre: {most_genre}\n\n"

        self.MovieStat_area.insert(tk.END, stat)

        # insert TV Show list stats
        count, rating_count, average_duration, most_actor, most_genre = self.Recommender.getTVStats()

        stat = "Ratings:\n"

        for rating, count_current in rating_count.items():

            percent = count_current * 100/ count
            stat += f"{rating}  {percent:.2f}\n"
            
        stat += f"\nAverage Number of Seasons: {average_duration} seasons\n\n"
        stat += f"Most Prolific Actor: {most_actor}\n\n"
        stat += f"Most Frequent Genre: {most_genre}\n\n"

        self.TVShowStat_area.insert(tk.END, stat)

       
    def load_books(self):
        self.Recommender.loadBooks()

        # clean the original area
        self.BookList_area.delete("1.0", tk.END)
        self.BookStat_area.delete("1.0", tk.END)

        self.BookList_area.insert(tk.END, self.Recommender.getBookList())
        
        average_page, most_author, most_publisher = self.Recommender.getBookStats()

        stat = f"Average Page Count: {average_page:.2f}\n\n"
        stat += f"Most Prolific Author: {most_author}\n\n"
        stat += f"Most Prolific Publisher: {most_publisher}\n"
        
        self.BookStat_area.insert(tk.END, stat)

    def load_associations(self):
        self.Recommender.loadAssociations()

    def credit_info_box(self):
        creditInfo = ("Created by: "
                      "\nSugi Lu, "
                      "Kartikey Singh, & "
                      "Paul Leible"
                      "\non 5/2/2024")
        messagebox.showinfo("Credit Info",creditInfo)

    def search_shows(self):
        message = self.Recommender.searchTVMovies(self.search_ShowType_box.get(), self.search_ShowTitle_Field.get(), self.search_ShowDirector_Field.get(), self.search_ShowActor_Field.get(),self.search_ShowGenre_Field.get())
        self.search_ShowList_area.delete("1.0", tk.END)
        self.search_ShowList_area.insert(tk.END, message)

    def search_books(self):
        message = self.Recommender.searchBooks(self.search_BookTitle_Field.get(), self.search_BookAuthor_Field.get(), self.search_BookPublisher_Field.get())
        self.search_BookList_area.delete("1.0", tk.END)
        self.search_BookList_area.insert(tk.END, message)

    def get_recommendations(self):
        message = self.Recommender.getRecommendations(self.search_recType_box.get(), self.search_recTitle_Field.get())
        self.search_recList_area.delete("1.0", tk.END)
        self.search_recList_area.insert(tk.END, message)


def main():
    gui = RecommenderGUI()
    gui.main_window.mainloop()


if __name__ == "__main__":
    main()