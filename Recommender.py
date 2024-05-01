# Author: Suqi Lu
# Latest modified date: 4/26/2024
# Description: The back-end function of the Recommender. 

from Book import Book
from Show import Show
import tkinter
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os

class Recommender():

    def __init__(self):
        """
        This constructor create 3 empty dictionary which store the movie/TV show, book and associations
        """
        self.__book_dict = {}
        self.__show_dict = {}
        self.__ass_dict = {}

    def loadBooks(self):
        """
        This function load the book information from user input file
        """

        # read the file, if file is not exist, ask for file name until the file is existed
        while 1:
            filepath = filedialog.askopenfilename(title="", initialdir=os.getcwd())

            if os.path.exists(filepath):
                break
            else:
                print("The file is not exist")
                continue
        
        # Make a copy, if it encounter error, then back up
        copy = self.__book_dict.copy()
        self.__book_dict = {}

        try:
            with open(filepath, "r") as file:
                next(file)

                for line in file:
                    line = line.strip().split(",")

                    if len(line) != 11:
                        raise ValueError("The input file is not the standard shows input file")
                    
                    id = line[0]
                    title = line[1]
                    authors = line[2]
                    average_rate = line[3]
                    isbn = line[4]
                    isbn13 = line[5]
                    language_code  = line[6]
                    num_pages = line[7]
                    num_ratings = line[8]
                    publication_date = line[9]
                    publisher = line[10]

                    newBook = Book(id, title, average_rate, authors, isbn, isbn13, language_code, num_pages, num_ratings, publication_date, publisher)

                    self.__book_dict[id] = newBook
        except Exception as e:

            # if encounter any error, set the dictionary as last copy of data
            self.__book_dict = copy
            print(e)
    
    def loadShows(self):
        """
        This function load the Movie/TV Show informations from user input file
        """

        # read the file
        while 1:
            filepath = filedialog.askopenfilename(title="", initialdir=os.getcwd())

            if os.path.exists(filepath):
                break
            else:
                print("The file is not exist")
                continue

        # Make a copy, if it encounter error, then back up
        copy = self.__show_dict.copy()
        self.__show_dict = copy

        try:
            with open(filepath, "r", encoding='utf-8') as file:
                next(file)

                for line in file:
                    line = line.strip().split(",")

                    if len(line) != 13:
                        raise ValueError("The input file is not the standard shows input file")
                    
                    id = line[0]
                    type = line[1]
                    title = line[2]
                    directors = line[3]
                    cast = line[4]
                    average_rate = line[5]
                    country_code = line[6]
                    date_added = line[7]
                    year_released = line[8]
                    rating = line[9]
                    duration = line[10]
                    genres = line[11]
                    description = line[12]

                    newShow = Show(id, title, average_rate, type, directors, cast, country_code, date_added, year_released, rating, duration, genres, description)

                    self.__show_dict[id] = newShow
        except Exception as e:

            # if encounter any error, set the dictionary as last copy of data
            self.__show_dict = copy
            print(e)

    def loadAssociations(self):
        """
        This function load the Associations informations from user input file
        """

        # read the file
        while 1:
            filepath = filedialog.askopenfilename(title="", initialdir=os.getcwd())

            if os.path.exists(filepath):
                break
            else:
                print("The file is not exist")
                continue

        # Make a copy, if it encounter error, then back up
        copy = self.__ass_dict.copy()
        self.__ass_dict = {}

        try:
            with open(filepath, "r") as file:

                for line in file:
                    line = line.strip().split(",")

                    if len(line) != 2:
                        raise ValueError("The input file is not the standard shows input file")
                        
                    id1 = line[0]
                    id2 = line[1]

                    # store id1 and id2
                    if id1 in self.__ass_dict:
                        if id2 in self.__ass_dict[id1]:
                            self.__ass_dict[id1][id2] += 1
                        else:
                            self.__ass_dict[id1][id2] = 1
                    else:
                        self.__ass_dict[id1] = {}
                        self.__ass_dict[id1][id2] = 1
                    
                    # reversal store
                    if id2 in self.__ass_dict:
                        if id1 in self.__ass_dict[id2]:
                            self.__ass_dict[id2][id1] += 1
                        else:
                            self.__ass_dict[id2][id1] = 1
                    else:
                        self.__ass_dict[id2] = {}
                        self.__ass_dict[id2][id1] = 1

        except Exception as e:

            # if encounter any error, set the dictionary as last copy of data
            self.__ass_dict = copy
            print(e)

    def getMovieList(self):
        """
        This function return list of Movies

        Returns:
        message(String): the movie list
        """

        # the max length of each columns
        maxTitle = 5
        maxRuntime = 7

        # update max length
        for id, movie in self.__show_dict.items():

            if movie.get_type_show().lower() == "movie":
                title = movie.get_title()
                duration = movie.get_duration()

                if maxTitle < len(title):
                    maxTitle = len(title)
                
                if maxRuntime < len(duration):
                    maxRuntime = len(duration)

        # add one space for padding
        maxTitle = maxTitle + 1
        maxRuntime = maxRuntime + 1

        # print header
        message = modifyInfo("Title ", maxTitle)
        message += modifyInfo("Runtime ", maxRuntime) + "\n"
        
        # print information of each movie
        for id, movie in self.__show_dict.items():

            if movie.get_type_show().lower() == "movie":

                title = movie.get_title()
                duration = movie.get_duration()

                message += modifyInfo(title, maxTitle)
                message += modifyInfo(duration, maxRuntime) +"\n"
        
        return message

    def getBookList(self):
        """
        This function return list of all Books

        Returns:
        message(String): the book list
        """

        # the max length of each columns
        maxTitle = 5
        maxAuthor = 9

        # update max length
        for id, book in self.__book_dict.items():

            title = book.get_title()
            authors = book.get_authors()

            if maxTitle < len(title):
                maxTitle = len(title)
                
            if maxAuthor < len(authors):
                maxAuthor = len(authors)
        
        # add one space for padding
        maxTitle = maxTitle + 1
        maxAuthor = maxAuthor + 1

        # print header
        message = modifyInfo("Title ", maxTitle)
        message += modifyInfo("Author(s) ", maxAuthor) + "\n"

        # print information of books        
        for id, book in self.__book_dict.items():

            title = book.get_title()
            authors = book.get_authors()

            message += modifyInfo(title, maxTitle)
            message += modifyInfo(authors, maxAuthor) +"\n"
        
        return message
                
    def getTVList(self):
        """
        This function return list of all TV Shows

        Returns:
        message(String): the tv list
        """

        # the max length of each columns
        maxTitle = 5
        maxSeasons = 7

        # update max length
        for id, movie in self.__show_dict.items():

            if movie.get_type_show().lower() == "tv show":
                title = movie.get_title()
                seasons = movie.get_duration()

                if maxTitle < len(title):
                    maxTitle = len(title)
                
                if maxSeasons < len(seasons):
                    maxSeasons = len(seasons)
        
        # add one space for padding
        maxTitle = maxTitle + 1
        maxSeasons = maxSeasons + 1

        # print header
        message = modifyInfo("Title ", maxTitle)
        message += modifyInfo("Seasons ", maxSeasons) + "\n"
        
        # print tv shows inforamtions
        for id, movie in self.__show_dict.items():

            if movie.get_type_show().lower() == "tv show":

                title = movie.get_title()
                seasons = movie.get_duration()

                message += modifyInfo(title, maxTitle)
                message += modifyInfo(seasons, maxSeasons) +"\n"
        
        return message
    
    def getMovieStats(self):
        """
        This function return statistics regarding movies

        Returns:
        count(int): the number of TV shows
        rating_count(dictionary): the count of each type of rating. key is type, value is counts
        average_duration(float): the average duration of movies
        getMost(director_count)(string): the director who has directed the most movies
        getMost(actor_count)(string): the actor who has acted in the most movies
        getMost(genres_count)(string): the most frequent movie genre
        """
        
        rating_count = {} # count number of movie based on their rating
        director_count = {} # count who has directed the most movie
        actor_count = {} # count who has acted in the most movies
        genres_count = {} # count most frequent movie genre
        count = 0 # count how many movies
        average_duration = 0

        for id, movie in self.__show_dict.items():

            if movie.get_type_show().lower().strip() == "movie":
                
                count +=1

                addToDict(movie.get_rating(), rating_count)
                
                average_duration += int(movie.get_duration().split(" ")[0])

                stripAndSplit(movie.get_directors(), director_count)
                
                stripAndSplit(movie.get_actors(), actor_count)
                
                stripAndSplit(movie.get_genres(), genres_count)

        if count != 0:
            average_duration = average_duration / count
        
        # uncomment this for testsing 
    
        """
        message = "Ratings:"
        print(message)

        for rating, count_current in rating_count.items():

            percent = count_current * 100/ count
            message = f"{rating}  {percent:.2f}"
            print(message)
        
        print("Average duration: " + str(average_duration))
        
        print("most director: " + getMost(director_count))
        print("most actor: " + getMost(actor_count))
        print("most genres: " + getMost(genres_count))
        """
        
        return count, rating_count, average_duration, getMost(director_count), getMost(actor_count), getMost(genres_count)

    def getTVStats(self):
        """
        This function return statistics regarding TV Shows

        Returns:
        count(int): the number of TV shows
        rating_count(dictionary): the count of each type of rating
        average_duration(float): the average duration of tv show
        getMost(actor_count)(string): the most prolific actor of tv show
        getMost(genres_count)(string): the most frequent tv show genre
        """
        
        rating_count = {} # count number of movie based on their rating
        average_duration = 0 # count number of seasons
        actor_count = {} # count who has acted in the most tv shows
        genres_count = {} # count most frequent movie genre
        count = 0 # count how many movies
        
        # get informations
        for id, tvshow in self.__show_dict.items():

            if tvshow.get_type_show().lower() == "tv show":
                 
                count +=1

                addToDict(tvshow.get_rating(), rating_count)

                average_duration += int(tvshow.get_duration().split(" ")[0])
                
                stripAndSplit(tvshow.get_actors(), actor_count)
                
                stripAndSplit(tvshow.get_genres(), genres_count)
                
        if count != 0:
            average_duration = average_duration / count

        # uncomment this for testing 

        """
        message = "Ratings:"
        print(message)

        for rating, count_current in rating_count.items():

            percent = count_current * 100/ count
            message = f"{rating}  {percent:.2f}"
            print(message)

        print("average seasons: " + str(average_duration))
        print("most actor: " + getMost(actor_count))
        print("most tv: " + getMost(genres_count))
        """
        
        return count, rating_count, average_duration, getMost(actor_count), getMost(genres_count)
    
    def getBookStats(self):
        """
        This function return statistics regarding books

        Returns:
        average_page(float): average page count, didn't set up any decimals of precision
        getMost(author_count)(string): the author who has written the most books
        getMost(publisher_count)(string): the publisher who has published the most books
        """
        
        average_page = 0 # count average number of pages
        author_count = {} # count number of written book by one author
        publisher_count = {} # count number of tv shows
        count = 0 # count how many movies
        
        # get informations
        for id, book in self.__book_dict.items():
            
            count +=1

            average_page += int(book.get_num_pages())

            stripAndSplit(book.get_authors(), author_count)
            
            addToDict(book.get_publisher(), publisher_count)

        average_page = average_page / count

        # uncomment this for testing 

        """
        print("average pages: " + str(average_page))
        print("most author: " + getMost(author_count))
        print("most publisher: " + getMost(publisher_count))
        """
        
        return average_page, getMost(author_count), getMost(publisher_count)

    def searchTVMovies(self, type, title, directors, actor, genre):
        """
        This function search the Movie/TV Shows list which include the related information

        Parameters:
        type(string): the type of selected shows.
        title(string): the title from user's input
        directors(string): the directors from user's input
        actor(string): the actor from user's input
        genre(string): the genre from user's input

        Returns:
        message(string): the selected list of the shows
        """
        
        type = type.strip()
        # if no type is selected
        if type.lower() != "movie" and type.lower() != "tv show":
            messagebox.showerror(title="undefined media type", message="you need to select Movie of TV Show first")
            message = "No Results"
            return message
        
        # remove spaces
        type = type.lower()
        title = title.strip()
        directors = directors.strip()
        actor = actor.strip()
        genre = genre.strip()

        # If the strings representing title, director, actor, and genre are all empty, spawn ashowerror messagebox
        if title == "" and directors == "" and actor == "" and genre == "":
            messagebox.showerror(title="empty search", message="you need enter information for title, directory, actor and genre first")
            message = "No Results"
            return message
        
        # make a copy of originary dictionary
        dict_copy = {}

        # search the relative informations
        for id, object in self.__show_dict.items():

            if object.get_type_show().lower() != type:
                continue

            if title not in object.get_title():
                continue
            
            if directors not in object.get_directors():
                continue
            
            if actor not in object.get_actors():
                continue
            
            if genre not in object.get_genres():
                continue
            
            dict_copy[id] = object
        
        # set max length
        maxTitle = 5 
        maxDirector = 8
        maxActor = 5
        maxGenre = 5

        # search the max length
        for id, object in dict_copy.items():
            
            if len(object.get_title()) > maxTitle:
                maxTitle = len(object.get_title())

            if len(object.get_directors()) > maxDirector:
                maxDirector = len(object.get_directors())
            
            if len(object.get_actors()) > maxActor:
                maxActor = len(object.get_actors())
            
            if len(object.get_genres()) > maxGenre:
                maxGenre = len(object.get_genres())

        # adding 1 for space between columns
        maxTitle = maxTitle + 1
        maxDirector = maxDirector + 1
        maxActor = maxActor + 1
        maxGenre = maxGenre + 1

        # print out the message 
        message = modifyInfo("Title ", maxTitle)
        message += modifyInfo("Director ", maxDirector)
        message += modifyInfo("Actor ", maxActor)
        message += modifyInfo("Genre ", maxGenre) + "\n"

        for id, object in dict_copy.items():
            
            message += modifyInfo(object.get_title(), maxTitle)
            message += modifyInfo(object.get_directors(), maxDirector)
            message += modifyInfo(object.get_actors(), maxActor)
            message += modifyInfo(object.get_genres(), maxGenre) + "\n"

        return message

    def searchBooks(self, title, author, publisher):
        """
        This function search the books list which include the related information

        Parameters:
        title(string): the title from user's input
        author(string): the author from user's input
        publisher(string): the publisher from user's input
        
        Returns:
        message(string): the selected list of books
        """

        # remove spaces
        title = title.strip()
        author = author.strip()
        publisher = publisher.strip()

        # If the strings representing title, author, publisher are all empty, spawn ashowerror messagebox
        if title == "" and author == "" and publisher == "":
            messagebox.showerror(title="empty search", message="you need enter information for title, author, publisher first")
            message = "No Results"
            return message
        
        # make a copy of originary dictionary
        dict_copy = {}

        # search the relative informations
        for id, object in self.__book_dict.items():


            if title not in object.get_title():
                continue
            
            if author not in object.get_authors():
                continue
            
            if publisher not in object.get_publisher():
                continue
            
            dict_copy[id] = object

        # set max length
        maxTitle = 5 
        maxAuthor = 5
        maxPublisher = 9

        # search the max length
        for id, object in dict_copy.items():
            
            if len(object.get_title()) > maxTitle:
                maxTitle = len(object.get_title())

            if len(object.get_authors()) > maxAuthor:
                maxAuthor = len(object.get_authors())
            
            if len(object.get_publisher()) > maxPublisher:
                maxPublisher = len(object.get_publisher())
        
        # adding 1 for space between columns
        maxTitle = maxTitle + 1
        maxAuthor = maxAuthor + 1
        maxPublisher = maxPublisher + 1

        # print out the message 
        message = ""
        message += modifyInfo("Title", maxTitle)
        message += modifyInfo("Author ", maxAuthor)
        message += modifyInfo("Publisher ", maxPublisher) + "\n"

        for id, object in dict_copy.items():
            
            message += modifyInfo(object.get_title(), maxTitle)
            message += modifyInfo(object.get_authors(), maxAuthor)
            message += modifyInfo(object.get_publisher(), maxPublisher) + "\n"
    
        return message

    def getRecommendations(self, type, title):
        """
        This function search the books list which include the related information

        Parameters:
        type(string): the type of the media
        title(string): the title from user's input
        
        Returns:
        message(string): the recomendation list of books/TV shows/ Movie
        """

        type = type.strip().lower()
        title = title.lower()
        # if no type is selected
        if type != "movie" and type != "tv show" and type != "book":
            messagebox.showerror(title="undefined media type", message="you need to select Movie, TV Show or Book first")
            message = "No Results"
            return message
        
        dict_temp = {} # create a empty dictionary to store objects for avoiding repeat recommendation
        finded = 0 # if not finded, then spawn error messagebox

        if type == "movie" or type == "tv show":
            
            for id1, object1 in self.__show_dict.items():
                    
                    if title in object1.get_title().lower():
                        
                        finded = 1
                        for id2, object2 in self.__ass_dict[id1].items():

                            if id2 not in dict_temp:
                                
                                dict_temp[id2] = self.__book_dict[id2]

        elif type == "book":

            for id1, object1 in self.__book_dict.items():

                if title in object1.get_title().lower():

                    finded = 1

                    for id2, object2 in self.__ass_dict[id1].items():

                            if id2 not in dict_temp:
                                
                                dict_temp[id2] = self.__show_dict[id2]

        # if not find 
        if finded == 0:
                messagebox.showwarning(title="empty search", message="no recommendations for that title")
                message = "No Results"
                return message

        message = ""
        for id, object in dict_temp.items():

            message += object.getString()
            message += "\n\n"
            message += "*****************"
            message += "\n\n"
        
        return message

def addToDict(object, dict):
    """
    helper function to put object into dictionary
    """

    if object in dict:
        dict[object] += 1
    else:
        dict[object] = 1


def stripAndSplit(object, dict):
    """
    helper function for strip and split the information. Then add it to the dictionary
    """
    items = object.strip()
    if items != "":
        items = items.split("\\")
        for item in items:
            addToDict(item, dict)
    
def modifyInfo(info, len2):
    """
    helper function for adding infor and determine if it need adding extra space for padding

    Returns:
    message(string): the modified message after add extra space
    """
    message = info
    # add extra spaces
    if len(info) < len2:
        for i in range(len2 - len(info)):
            message += " "
    return message

def getMost(dict):
    """
    helper function for get most popular one

    Returns:
    most_object(string): the most popular one in a dictionary
    """

    most_object_count = 0
    most_object = ""

    for object, count_current in dict.items():

        if count_current > most_object_count:
            most_object_count = count_current
            most_object = object

    return most_object