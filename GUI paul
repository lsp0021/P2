#Author: Kartikey and Paul
# Latest modified date: 5/2/24
# Description: GUI for project2

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Recommender import Recommender
#importing all necessary files and classes

class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()
        #instantiating Recommend() and putting it into self.recommender

        # Creating a main window
        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")
        self.main_window.geometry("1200x800")
        #dimensions and title as given

        # Creating notebook tab for main window
        self.notebook = ttk.Notebook(self.main_window)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Create note book tabs for movie, tv, book, search show, search book, and reccomendation
        self.create_movie_tab()
        self.create_tv_show_tab()
        self.create_book_tab()
        self.create_show_search_tab()
        self.create_book_search_tab()
        self.create_recommendation_tab()

        # Create buttons for load show, book, association, credit, and quit
        self.create_buttons()

        self.main_window.mainloop()
        #run mainloop

    def create_movie_tab(self):
        movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(movie_tab, text="Movies")
        #adding the tab with title movies

        # Add widgets for displaying movie data
        self.movieText = tk.Text(movie_tab, width=130, height=20)
        self.movieText.grid(row=0, column=0, padx=10, pady=10)
        self.movieText.insert(tk.END, "Movie Data")
        self.movieText.config(state=tk.DISABLED)
        #text box set to disabled for displaying the movie data

        self.moveieStats = tk.Text(movie_tab,width=130,height=15)
        self.moveieStats.grid(row=1, column=0, padx=10, pady=0)
        self.moveieStats.insert(tk.END,"Movie Stats")
        self.moveieStats.config(state=tk.DISABLED)
        #textbox set to disabled for displaying the stast


    def create_tv_show_tab(self):
        tv_show_tab = ttk.Frame(self.notebook)
        self.notebook.add(tv_show_tab, text="TV Shows")
        #adding the tv show tab with appropriate title

        # Add widgets for displaying TV show data
        self.tvText = tk.Text(tv_show_tab, width=130, height=20)
        self.tvText.grid(row=0, column=0, padx=10, pady=10)
        self.tvText.insert(tk.END, "TV Data")
        self.tvText.config(state=tk.DISABLED)
        #creating textbox for tv data to be entered

        self.tvStats = tk.Text(tv_show_tab, width=130, height=15)
        self.tvStats.grid(row=1, column=0, padx=10, pady=0)
        self.tvStats.insert(tk.END, "TV Stats")
        self.tvStats.config(state=tk.DISABLED)
        #creatin tv stats box for stats to be entered

    def create_book_tab(self):
        book_tab = ttk.Frame(self.notebook)
        self.notebook.add(book_tab, text="Books")
        #creating a notebook tab for books

        # Add widgets for displaying book data
        self.bookText = tk.Text(book_tab, width=130, height=20)
        self.bookText.grid(row=0, column=0, padx=10, pady=10)
        self.bookText.insert(tk.END, "Book Data")
        self.bookText.config(state=tk.DISABLED)
        #text book for book data to be loaded into

        self.bookStats = tk.Text(book_tab, width=130, height=15)
        self.bookStats.grid(row=1, column=0, padx=10, pady=0)
        self.bookStats.insert(tk.END, "Book Stats")
        self.bookStats.config(state=tk.DISABLED)
        #textbox for book stats to be loaded into

    def create_show_search_tab(self):
        search_tab = ttk.Frame(self.notebook)
        self.notebook.add(search_tab, text="Movie & TV Search")
        #new notebook tab for searching shows or movies &tv

        # Add widgets for searching movies and TV shows
        searchLabel = ttk.Label(search_tab, text="Search Media")
        searchLabel.pack()
        #label for combobox media type
        self.media_type_combobox_shows_search = ttk.Combobox(search_tab, values=["Movie", "TV Show"])
        self.media_type_combobox_shows_search.pack()
        #combobox for media type selection of shows

        title_entry_label = tk.Label(search_tab, text="Title Entry:")
        title_entry_label.pack()
        self.title_entry_shows_search = ttk.Entry(search_tab, width=50)
        self.title_entry_shows_search.pack()
        #entry box for title of show for search, with label

        director_entry_label = tk.Label(search_tab, text="Director Entry:")
        director_entry_label.pack()
        self.director_entry_shows_search = ttk.Entry(search_tab, width=50)
        self.director_entry_shows_search.pack()
        # entry box for director of show for search, with label

        actor_entry_label = tk.Label(search_tab, text="Actor Entry:")
        actor_entry_label.pack()
        self.actor_entry_shows_search = ttk.Entry(search_tab, width=50)
        self.actor_entry_shows_search.pack()
        # entry box for actor in show for search, with label

        genre_entry_label = tk.Label(search_tab, text="Genre Entry:")
        genre_entry_label.pack()
        self.genre_entry_shows_search = ttk.Entry(search_tab, width=50)
        self.genre_entry_shows_search.pack()
        # entry box for genre of show for search, with label

        search_button = ttk.Button(search_tab, text="Search",
                        command=lambda: self.search_shows())
        search_button.pack()
        #search button that commands a call to the search_shows() function

        self.searchShowText = tk.Text(search_tab, width=150, height=20)
        self.searchShowText.pack()
        self.searchShowText.insert(tk.END, "Movie & TV Search Data")
        self.searchShowText.config(state=tk.DISABLED)
        #a texbox are to show results of the search set to uneditable

    def create_book_search_tab(self):
        search_tab = ttk.Frame(self.notebook)
        self.notebook.add(search_tab, text="Book Search")
        #creating a new notebook tab for book searches

        # Add widgets for searching movies and TV shows
        searchLabel = ttk.Label(search_tab, text="Search Books")
        searchLabel.pack()
        #label to say search for books

        title_entry_label = tk.Label(search_tab, text="Title Entry:")
        title_entry_label.pack()
        self.title_entry_book_search = ttk.Entry(search_tab, width=50)
        self.title_entry_book_search.pack()
        #label and entry box to search by title

        author_entry_label = tk.Label(search_tab, text="Author Entry:")
        author_entry_label.pack()
        self.author_entry_book_search = ttk.Entry(search_tab, width=50)
        self.author_entry_book_search.pack()
        #label and entry box to search by author

        publisher_entry_label = tk.Label(search_tab, text="Publisher Entry:")
        publisher_entry_label.pack()
        self.publisher_entry_book_search = ttk.Entry(search_tab, width=50)
        self.publisher_entry_book_search.pack()
        #label and entry box to search by publisher

        search_button = ttk.Button(search_tab, text="Search",
                                   command=lambda: self.search_books())
        search_button.pack()
        #button that commands a call to the search_books() function

        self.searchBookText = tk.Text(search_tab, width=150, height=20)
        self.searchBookText.pack()
        self.searchBookText.insert(tk.END, "Book Search Data")
        self.searchBookText.config(state=tk.DISABLED)
        #textbox for search results with default text set to uneditable

    def create_recommendation_tab(self):
        recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(recommendation_tab, text="Recommendations")
        #creating a new notebook tab for reccomnedations

        # Add widgets for getting recommendations
        recommendationLabel = ttk.Label(recommendation_tab,text="Reccomneded Media")
        recommendationLabel.pack()
        #adding a label for reccomendations

        self.media_type_combobox_recommend = ttk.Combobox(recommendation_tab, values=["Movie", "TV Show", "Book"])
        self.media_type_combobox_recommend.pack()
        #adding a combobox for selecting either movie, tv, or book

        title_entry_label = tk.Label(recommendation_tab, text="Title Entry:")
        title_entry_label.pack()
        self.title_entry_recommend = ttk.Entry(recommendation_tab, width=50)
        self.title_entry_recommend.pack()
        #entry box and label for title of media

        recommend_btn = ttk.Button(recommendation_tab, text="Get Recommendations", command= lambda: self.get_recommendations())
        recommend_btn.pack()
        #button that commands a call to the get_recommendations() function

        self.recommendationText = tk.Text(recommendation_tab, width=130, height=20)
        self.recommendationText.pack()
        self.recommendationText.insert(tk.END,"Reccomendation Data")
        self.recommendationText.config(state=tk.DISABLED)
        #textbox with space to put recommendations

    def create_buttons(self):
        button_frame = tk.Frame(self.main_window)
        button_frame.pack()
        #creating the button frame

        # Create buttons
        load_shows_button = tk.Button(button_frame, text="Load Shows", command=self.load_shows)
        load_shows_button.grid(row=0, column=0)
        #creating a button on the bottom to load shows that calls the function load_shows

        load_books_button = tk.Button(button_frame, text="Load Books", command=self.load_books)
        load_books_button.grid(row=0, column=1)
        #creating a button on the bottom to load books that calls the function load_books

        load_associations_button = tk.Button(button_frame, text="Load Associations", command=self.load_associations)
        load_associations_button.grid(row=0, column=2)
        #creating a button on the bottom to load associations that calls the function load_associations

        credit_info_button = tk.Button(button_frame, text="Credit Info", command=self.credit_info_box)
        credit_info_button.grid(row=0, column=3)
        #creating a button on the bottom to show the creator credits that calls the credit_info_box function

        quit_button = tk.Button(button_frame, text="Quit", command=self.main_window.quit)
        quit_button.grid(row=0, column=4)
        #creating a button on the bottom to quit the window that calls the main_window_quit function

    def load_shows(self):
        # Implement loading shows
        self.recommender.loadShows()
        #loading in the shows ie tv and movies

        #************movie************
        self.movieList=self.recommender.getMovieList()
        self.movieText.config(state=tk.NORMAL)
        self.movieText.delete(1.0,tk.END)
        self.movieText.insert(tk.END, self.movieList)
        self.movieText.config(state=tk.DISABLED)
        #entering the movie list into the movie textbox by making the box
        # editable, inserting the list, then closing the box to edits

        count_movie, rating_count_movie, average_duration_movie, max_director_movie, max_actor_movie, max_genre_movie = self.recommender.getMovieStats()
        #setting all of our variables to the movie stats function

        movie_stats = "Ratings:\n"
        for rating1, count_current1 in rating_count_movie.items():
            percent1 = count_current1 * 100 / count_movie
            movie_stats += f"{rating1}  {percent1:.2f}%\n"
            #iterating through the ratings to get percentages of different audience ratings

        movie_stats = movie_stats + (f"\nAverage Movie Duration: {average_duration_movie} mins\n\n"
                                     f"Most Prolific Director: {max_director_movie}\n\n"
                                     f"Most Prolific Actor: {max_actor_movie}\n\nMost Frequent Genre: {max_genre_movie}\n\n")
        #adding to our ratings, we add stats for duration, director, actor, and genre

        self.moveieStats.config(state=tk.NORMAL)
        self.moveieStats.delete(1.0,tk.END)
        self.moveieStats.insert(tk.END,movie_stats)
        self.moveieStats.config(state=tk.DISABLED)
        #entering the movie stats all at once into the movie stats textbox by making the box
        # editable, inserting the list, then closing the box to edits

        #************tv************
        #very similar to the movie
        self.tvList = self.recommender.getTVList()
        self.tvText.config(state=tk.NORMAL)
        self.tvText.delete(1.0, tk.END)
        self.tvText.insert(tk.END, self.tvList)
        self.tvText.config(state=tk.DISABLED)
        # entering the tv list into the tv textbox by making the box
        # editable, inserting the list, then closing the box to edits


        count_tv, rating_count_tv, average_duration_tv,max_actor_tv, max_genre_tv = self.recommender.getTVStats()

        tv_stats = "Ratings:\n"
        for rating2, count_current2 in rating_count_tv.items():
            percent2 = count_current2 * 100 / count_tv
            tv_stats += f"{rating2}  {percent2:.2f}%\n"
            #iterating through the ratings to get percentages of different audience ratings

        tv_stats = tv_stats + (f"\nAverage TV Seasons: {average_duration_tv}\n\nMost Prolific Actor: {max_actor_tv}\n\n"
                               f"Most Frequent Genre: {max_genre_tv}\n\n")
        #adding to our ratings, we add stats for seasons, actor, and genre

        self.tvStats.config(state=tk.NORMAL)
        self.tvStats.delete(1.0, tk.END)
        self.tvStats.insert(tk.END, tv_stats)
        self.tvStats.config(state=tk.DISABLED)
        #entering the tv stats all together into the tv stats textbox by making the box
        # editable, inserting the list of stats, then closing the box to edits

    def load_books(self):
        # Implement loading books
        self.recommender.loadBooks()
        #loading in the books files

        #books
        self.bookList = self.recommender.getBookList()
        self.bookText.config(state=tk.NORMAL)
        self.bookText.delete(1.0, tk.END)
        self.bookText.insert(tk.END, self.bookList)
        self.bookText.config(state=tk.DISABLED)
        #getting the list of books then showing it in the book textbox
        # by opening, inserting, then closing the box

        average_page_book, max_author_book, max_publisher_book = self.recommender.getBookStats()
        #calling our getBookStats() function and saving all of the returned variables

        book_stats = (f"\nAverage Page Count: {average_page_book:.0f}\n\nMost Prolific Author: {max_author_book}\n\n"
                    f"Most Frequent Publisher: {max_publisher_book}\n\n")
        #adding all the variables to one string

        self.bookStats.config(state=tk.NORMAL)
        self.bookStats.delete(1.0, tk.END)
        self.bookStats.insert(tk.END, book_stats)
        self.bookStats.config(state=tk.DISABLED)
        #adding our variables string to the book stats textbox by
        # opening, inserting, then closing the box

    def load_associations(self):
        # Implement loading associations
        self.recommender.loadAssociations()
        #simple loading the associations,
        # we do not need to display since they are only used for reccomendations

    def credit_info_box(self):
        # Implement credit info dialog
        creditInfo = ("Created by: "
                      "\nSugi Lu, "
                      "Kartikey Singh, & "
                      "Paul Leible"
                      "\non 5/2/2024")
        messagebox.showinfo("Credit Info",creditInfo)
        #simply creating a showinfo message box with all of our names in it


    def search_shows(self):
        # Implement search for movies and TV shows
        type = self.media_type_combobox_shows_search.get()
        title = self.title_entry_shows_search.get()
        director = self.director_entry_shows_search.get()
        actor = self.actor_entry_shows_search.get()
        genre = self.genre_entry_shows_search.get()
        #getting all of our search parameters from the entry boxes we created
        # within the search shows notebooke tab

        searchTextNew = self.recommender.searchTVMovies(type,title,director,actor,genre)
        #calling the search tv & movies function and putting the results into a new text string

        self.searchShowText.config(state=tk.NORMAL)
        self.searchShowText.delete(1.0,tk.END)
        self.searchShowText.insert(tk.END,searchTextNew)
        self.searchShowText.config(state=tk.DISABLED)
        #adding the new text string results into the results text box
        # by opening, inserting, then closing the text box

    def search_books(self):
        # Implement search for books
        title = self.title_entry_book_search.get()
        author = self.author_entry_book_search.get()
        publisher = self.publisher_entry_book_search.get()
        #getting all of our search parameters from the entry boxes

        searchTextNew = self.recommender.searchBooks(title, author, publisher)
        #calling the searchBooks() function with our parameters

        self.searchBookText.config(state=tk.NORMAL)
        self.searchBookText.delete(1.0, tk.END)
        self.searchBookText.insert(tk.END, searchTextNew)
        self.searchBookText.config(state=tk.DISABLED)
        #entering the search results into the results textbox
        # by opening, inserting, then closing

    def get_recommendations(self):
        # Implement getting recommendations
        type = self.media_type_combobox_recommend.get()
        title = self.title_entry_recommend.get()
        #getting our user entries from the combobox and entrybox

        recommendTextNew = self.recommender.getRecommendations(type,title)
        #calling the getRecommendations() with our user entries

        self.recommendationText.config(state=tk.NORMAL)
        self.recommendationText.delete(1.0, tk.END)
        self.recommendationText.insert(tk.END, recommendTextNew)
        self.recommendationText.config(state=tk.DISABLED)
        #inserting the recommendations results into the results text box
        # by opening, inserting, then closing

def main():
    guiMain = RecommenderGUI()
    #instantiating the main GUI class

main()
#calling and running main
